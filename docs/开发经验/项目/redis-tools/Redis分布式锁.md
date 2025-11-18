<meta name="referrer" content="no-referrer"/>

# 一.分布式锁初步
## 1.set命令实现分布式锁
首先分布式锁是要设置过期时间的，如果不设置过期时间，发生死锁，分布式锁就会被一直占用。

但是如果使用setnx+设置过期时间，没办法保证原子性。**我们要让添加锁标志位 & 添加过期时间命令保证一个原子性，要么一起成功，要么一起失败**。

我们的添加锁原子命令就要登场了，从 Redis 2.6.12 版本起，提供了可选的 **字符串 set 复合命令。**

```plain
SET key value [expiration EX seconds|PX milliseconds] [NX|XX]
```

可选参数如下: **EX:** 设置超时时间，单位是秒。 **PX:** 设置超时时间，单位是毫秒。 **NX:** IF NOT EXIST 的缩写，只有 **KEY 不存在的前提下** 才会设置值。 **XX:** IF EXIST 的缩写，只有在 **KEY 存在的前提下** 才会设置值。

继续完善分布式锁的应用程序，代码如下:

```plain
public class RedisLock implements Lock {

    @Autowired
    StringRedisTemplate stringRedisTemplate;
    @Override
    public boolean tryLock(String lockKey, long timeoutSec) {
        // 获取线程标识
        String threadId = Thread.currentThread().getId()+"";
        // 获取锁并判断是否成功
        // setIfAbsent方法是原子的，只有一个线程能够获取到锁，对应redis的setNx命令
        return Boolean.TRUE.equals(
                stringRedisTemplate.opsForValue().setIfAbsent(lockKey, threadId, timeoutSec, TimeUnit.SECONDS));
    }

    @Override
    public void unlock(String lockKey) {
        //通过del删除锁
        stringRedisTemplate.delete(lockKey);
    }

}
```

## 2.线程ID + UUID作为锁的标识，在删除前检查标识是否一致 -- 解决线程阻塞后误删其他线程锁的问题
持有锁的线程1在锁的内部出现了阻塞，导致他的锁到期释放，这时其他线程，线程2来尝试获得锁，就拿到了这把锁，然后线程2在持有锁执行过程中，线程1反应过来，继续执行，而线程1执行过程中，走到了删除锁逻辑，此时就会把本应该属于线程2的锁进行删除，这就是误删别人锁的情况说明。

**总结：线程一阻塞，锁到期释放，线程二获得锁，线程一停止阻塞，误删线程二的锁。**

> 可能有同学有疑问，Thread.currentThread().getId()不是线程的唯一标识吗？但是的话**在分布式的环境下，不同结点的不同线程使用Thread.currentThread().getId()取到的值是有可能相同的**，也就是在分布式环境下，误删的情况是很可能存在的。
>

**解决方案：在删除的时候判断锁是不是自己的（看看想要删除的锁的Key与线程ID+UUID是否一致），一致才可以删除。**

```plain
public class RedisLock implements Lock {

    @Autowired
    StringRedisTemplate stringRedisTemplate;

    // 线程标识
    private static final String ID_PREFIX = UUID.randomUUID() + "-";

    @Override
    public boolean tryLock(String lockKey, long timeoutSec) {
        // 获取线程标示
        String threadId = ID_PREFIX + Thread.currentThread().getId();
        // 获取锁并判断是否成功
        // setIfAbsent方法是原子的，只有一个线程能够获取到锁，对应redis的setNx命令
        return Boolean.TRUE.equals(
                stringRedisTemplate.opsForValue().setIfAbsent(lockKey, threadId, timeoutSec, TimeUnit.SECONDS));
    }

    @Override
    public void unlock(String lockKey) {
        // 获取线程标示
        String threadId = ID_PREFIX + Thread.currentThread().getId();
        // 获取锁中的标示
        String id = stringRedisTemplate.opsForValue().get(lockKey);
        // 判断标示是否一致
        if(threadId.equals(id)) {
            // 释放锁
            stringRedisTemplate.delete(lockKey);
        }
    }

}
```

**这一版在线程的基础上增加UUID结合之前的线程ID作为线程标识，让不同线程取得相同锁的概率大大降低，从根源上解决并发情况下锁的误删行为。**

## 3.Lua脚本保证原子性进一步解决误删问题
更为极端的误删逻辑说明：

1. 线程1准备删除锁，已经验证了锁是属于自己的
2. 就在这个时刻，线程1的锁过期了
3. 线程2进来并获取了这个已过期的锁
4. 当线程1恢复执行时，它继续执行删除操作

然后线程1就错误地删除了线程2的锁。

> 在分布式环境中，UUID+线程ID作为锁的标识，不同线程获取到同一把锁的概率大幅降低，但是还是有可能发生。
>

**根本原因**： 

验证和删除之间存在时间窗口，这个窗口内可能发生锁状态改变。所以我们使用Lua脚本把条件判断和操作放在一起执行。

```plain
public class SimpleRedisLockV3 implements Lock {

    @Autowired
    StringRedisTemplate stringRedisTemplate;

    @Autowired
    RedissonClient redissonClient;

    private static final String ID_PREFIX = UUID.randomUUID() + "-";

    @Override
    public boolean tryLock(String lockKey, long timeoutSec) {
        // 获取线程标示
        String threadId = ID_PREFIX + Thread.currentThread().getId();
        // 获取锁并判断是否成功
        // setIfAbsent方法是原子的，只有一个线程能够获取到锁，对应redis的setNx命令
        return Boolean.TRUE.equals(
                stringRedisTemplate.opsForValue().setIfAbsent(lockKey, threadId, timeoutSec, TimeUnit.SECONDS));
    }

    private static final DefaultRedisScript<Long> UNLOCK_SCRIPT;

    static {
        UNLOCK_SCRIPT = new DefaultRedisScript<>();
        UNLOCK_SCRIPT.setLocation(new ClassPathResource("unlock.lua"));
        UNLOCK_SCRIPT.setResultType(Long.class);
    }

    @Override
    public void unlock(String lockKey) {
        // 调用lua脚本
        stringRedisTemplate.execute(
                UNLOCK_SCRIPT,
                Collections.singletonList(lockKey),
                ID_PREFIX + Thread.currentThread().getId());
    }


}
```

> Redis本身是单线程的，单客户端并不会造成线程问题。但是多客户端就会。
>

# 二.分布式锁提升
上面的分布式锁还具有以下的问题

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1740460219541-7e7f38c3-3ac6-435b-b146-1c1499d1136a.png)

## 1.可重入
**如果我们在一个获取锁之后执行的代码里面也要进行获取锁的操作（相当于要嵌套获取锁）。如果按照之前的方式就会有死锁的情况发生，因为你已经获取过一次了，不能再重复获取。**

这时候就要引入可重入锁。

synchronized和Lock锁都是可重入的。

在Lock锁中，他是借助于底层的一个voaltile的一个state变量来记录重入的状态的，比如当前没有人持有这把锁，那么state=0，假如有人持有这把锁，那么state=1，如果持有这把锁的人再次持有这把锁，那么会+1 。

对于synchronized而言，他在c语言代码中会有一个count，原理和state类似，也是重入一次就加一，释放一次就-1 ，直到减少成0 时，表示当前这把锁没有被人持有。 

【1】在V1中，使用TreadLocal来存储锁的计数，粗略实现了可重入功能。

加锁的逻辑：

暂时无法在飞书文档外展示此内容

解锁逻辑：

暂时无法在飞书文档外展示此内容

【2】ReentrantRedisLockV2中加入了Lua脚本，保证最终一致性

加锁逻辑：

暂时无法在飞书文档外展示此内容

解锁逻辑：

暂时无法在飞书文档外展示此内容

## 2.可重试
当获取锁失败怎么办，我们可以加入可重试机制重复获取锁。

这里主要是在加锁的时候加个循环，获取锁失败后间隔一段时间重复获取锁。

当然，也不能一直重试下去，中间要加入锁的最大重试时间和重试次数，每一次的时候进行判断是否超过最大重试时间和重复次数，如果超过，那就退出停止重试。

## 3.自动续约
简单说就是创建看门狗定时任务，每隔一段时间（这里我设置为原来过期时间的二分之一），重置超时时间（Expire命令）

## 4.主从一致性（本项目未作实现）
为了提高redis的可用性，我们会搭建集群或者主从，现在以主从为例

此时我们去写命令，写在主机上， 主机会将数据同步给从机，但是假设在主机还没有来得及把数据写入到从机去的时候，此时主机宕机，哨兵会发现主机宕机，并且选举一个slave变成master，而此时新的master中实际上并没有锁信息，此时锁信息就已经丢掉了。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1740460219438-ad9ba1f3-688a-4065-bf59-b340ebaae5e1.png)

为了解决这个问题，redission提出来了MutiLock锁，使用**这把锁咱们就不使用主从了，每个节点的地位都是一样的， 这把锁加锁的逻辑需要写入到每一个主丛节点上，只有所有的服务器都写入成功，此时才是加锁成功，假设现在某个节点挂了，那么他去获得锁的时候，只要有一个节点拿不到，都不能算是加锁成功，就保证了加锁的可靠性。**

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1740460219406-742f4e0f-20aa-48ec-958e-410b8278a86a.png)

那么MutiLock 加锁原理是什么呢？

**当我们去设置了多个锁时，redission会将多个锁添加到一个集合中，然后用while循环去不停去尝试拿锁，但是会有一个总共的加锁时间，这个时间是用需要加锁的个数 * 1500ms ，假设有3个锁，那么时间就是4500ms，假设在这4500ms内，所有的锁都加锁成功， 那么此时才算是加锁成功，如果在4500ms有线程加锁失败，则会再次去进行重试.**


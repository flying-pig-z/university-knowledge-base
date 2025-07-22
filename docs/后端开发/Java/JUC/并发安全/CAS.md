<meta name="referrer" content="no-referrer"/>

## 什么是CAS
CAS（Compare-And-Swap）是一种原子操作，用于在并发编程中实现无锁算法。

它是现代CPU硬件或软件支持的一种同步原语。

CAS操作的基本原理是：

1. 首先读取一个内存位置的当前值（旧值）
2. 计算新值
3. 尝试将新值写回该内存位置，但仅当该位置的值仍然等于旧值时才写入
4. 返回操作是否成功

CAS操作的主要特点：

+ 它是原子的，不可分割
+ 它可以在不使用互斥锁的情况下实现线程同步
+ 它是乐观的并发控制机制，假设冲突很少发生

Java中的原子类（如AtomicInteger、AtomicReference等）以及许多高性能并发数据结构都基于CAS操作实现。

## Mysql的CAS
以超卖问题举例：

```sql
BEGIN TRANSACTION;

-- 1. 读取当前值
SELECT stock INTO @current_stock FROM product WHERE id = 10 FOR UPDATE;

-- 2. 计算新值
SET @new_stock = @current_stock - 1;

-- 3. 条件更新
UPDATE product 
SET stock = @new_stock 
WHERE id = 10 AND stock = @current_stock;

-- 4. 检查是否成功
SELECT ROW_COUNT() INTO @success;

COMMIT;

-- @success值为1表示成功，0表示失败
```

## CAS的问题
乐观锁造成的问题主要有两个，一个是ABA，一个是写操作较多的时候会不断重试，占用CPU导致自旋。

### ABA
CAS的ABA问题是并发编程中的一个经典问题。

ABA问题是指在使用CAS操作进行无锁编程时可能出现的一种情况：一个线程读取了一个值A，然后另一个线程将这个值从A改为B，之后又改回A，而第**一个线程无法察觉到这个值曾经被改变过**。

具体来说，ABA问题发生的过程如下：

1. 线程1读取共享变量的值为A
2. 线程2将值从A修改为B，然后又修改回A  
3. 线程1恢复执行，比较当前值仍然是A，认为没有发生变化，但实际上已经发生了A→B→A的变化 

怎么解决ABA呢？最简单的就是版本号和时间戳。

+ 在每次更新值的同时，更新一个单调递增的版本号或时间戳
+ 实际比较的不仅是值本身，还包括这个版本号
+ 即使值本身变回原来的A，但版本号已经变化，因此能够检测到中间发生的修改

还是以mysql举例：

```sql
BEGIN TRANSACTION;
-- 1. 读取当前值和版本号
SELECT stock, version INTO @current_stock, @current_version FROM product WHERE id = 10 FOR UPDATE;

-- 2. 计算新值
SET @new_stock = @current_stock - 1;

-- 3. 条件更新 (包含版本检查)
UPDATE product 
SET stock = @new_stock, version = @current_version + 1
WHERE id = 10 AND stock = @current_stock AND version = @current_version;

-- 4. 检查是否成功
SELECT ROW_COUNT() INTO @success;
COMMIT;
-- @success值为1表示成功，0表示失败
```

### 自旋
如果写操作较多的时候，值经常改变，CAS的条件就经常不会满足，就会重试，这时候就会导致自旋。

这时候我们可以考虑使用悲观锁来解决。

## 优化
超卖这样的问题，在高并发写的情况下，乐观锁是不合适的。

我们可以利用update子句本身就含有行锁的特性，直接简化成：

```sql
UPDATE product 
SET stock = stock - 1
WHERE id = {id} AND stock > 0
```

但是实际的业务更加复杂，这种方法常常不适用，比如说要更新多个产品的库存。

```sql
UPDATE product SET stock = stock - 2 WHERE id = 101 AND stock >= 2
UPDATE product SET stock = stock - 1 WHERE id = 102 AND stock >= 1
```

如果涉及多个操作，多个操作的原子性也要保证。

这时候更适合使用加锁解决，如果写操作比较少，就用乐观锁；要不然就用悲观锁，然后加入Redis库存预扣减，消息队列，限流等措施优化。

## 补充：版本号机制
除了CAS，版本号也可以实现乐观锁。

一般是在数据表中加上一个数据版本号version字段。当数据被修改时，version值会加一。

A读数据的时候会先读取version值，等到要更新的时候和之前读取的version值比较，相等时候说明数据没有被修改，则进行更新；否则重试操作，知道成功更新。




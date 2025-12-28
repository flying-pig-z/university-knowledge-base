实际项目中，大多数简单同步场景用Synchronized就够了，只有需要高级特性时（**超时、可中断、公平性或多条件**）才考虑使用ReentrantLock。

ReentrantLock可以看做具有高级特性的Synchronized。

超时，可中断，公平性这些比较耳熟能详就不用讲了。什么是多条件呢？

多条件，就是多个Condition？

效果如下，await可以当条件不足是等待，临时释放锁。

singal可以唤醒在对应条件上等待的线程。

```java
Lock lock = new ReentrantLock(); // 一把锁
Condition condition1 = lock.newCondition(); // 第一个等待室
Condition condition2 = lock.newCondition(); // 第二个等待室

// 线程1
lock.lock(); // 首先获取锁
try {
    // 如果条件不满足
    condition1.await(); // 在condition1上等待，临时释放了锁
    // 被唤醒后重新获得锁，继续执行
} finally {
    lock.unlock(); // 最终释放锁
}

// 线程2
lock.lock(); // 获取同一把锁
try {
    // 做一些改变条件的操作
    condition1.signal(); // 唤醒在condition1上等待的线程
} finally {
    lock.unlock(); // 释放锁
}
```


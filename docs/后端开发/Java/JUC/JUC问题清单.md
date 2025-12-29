<meta name="referrer" content="no-referrer"/>

# 上
+ 什么是线程和进程?
+ Java 线程和操作系统的线程有啥区别？
+ 用户级线程和内核级线程有什么不同？Java现在是哪一个？
+ 常见的三种线程模型（一对一 多对一 多对多）
+ 请简要描述线程与进程的关系,区别及优缺点？
+ 如何创建线程？
+ 严格来说Java只有一种方式可以创建线程是什么？
+ 说说线程的生命周期和状态?
+ 说说线程的生命周期和状态?【6种】
+ 这些状态之间通过什么方法转换？
+ 什么是线程上下文切换?如果不切换会发生什么？
+ Thread#sleep() 方法和 Object#wait() 方法对比
+ 为什么 wait() 方法不定义在 Thread 中？
+ 可以直接调用 Thread 类的 run 方法吗？
+ 并发与并行的区别？
+ 同步和异步的区别？
+ 为什么要使用多线程?
+ 单核 CPU 支持 Java 多线程吗？怎么支持的？
+ 单核 CPU 上运行多个线程效率一定会高吗？
+ 使用多线程可能带来什么问题?
+ 如何理解线程安全和不安全？
+ 什么是线程死锁?
+ 如何检测死锁？
+ 如何预防和避免线程死锁?

# 中
## JMM
CPU为什么需要缓存？（缓存模型）

什么是指令重排序

jvm中指令重排序会引发什么问题吗

什么是JMM?为什么需要JMM？

Java的内存模型 -- 什么是主内存？什么是本地内存？

线程1和线程2要进行通信，要经历哪两个步骤？

为什么会造成数据不一致/线程安全问题？

一个变量如何从主内存拷贝到工作内存，如何从工作内存同步到主内存之间的实现细节，Java 内存模型定义来以下八种同步操作，哪八种？还有什么同步规则？

JVM和JMM内存模型有什么区别？

happens-before是什么？在JMM中的应用？

happens-before与常见规则（了解即可）

并发编程的三大特性 -- 原子性 可见性 有序性

## volatile关键字
volatile关键字的作用（集合内存模型说明）

volatile如何禁止指令重排序

为什么单例需要禁止指令重排序

volatile能保证原子性吗?

## 乐观锁和悲观锁
+ 什么是悲观锁？悲观锁有什么缺点？
+ 什么是乐观锁？
+ 如何实现乐观锁？
+ 版本号机制怎么实现?
+ Java中是怎么做到CAS的？
+ Atomic 原子类是用来干什么的？是乐观锁实现还是死悲观锁实现的？
+ 什么是自旋锁机制？为什么CAS操作通常和while循环搭配？
+ CAS算法存在的ABA问题是什么?ABA问题的解决思路是什么？
+ CAS自旋操作循环时间开销大怎么解决？
+ CAS只能保证一个共享变量的原子操作怎么解决？
+ synchronized 是什么？有什么用？
+ 早期版本的synchronized是怎么实现的？为什么是重量级锁？后来经过了什么优化？
+ synchronized修饰实例方法？修饰静态方法？修饰代码块分别起到了什么作用？
+ 构造方法可以用 synchronized 修饰么？构造方法内部可以使用synchronized代码块吗？构造方法本身是线程安全的吗？
+ synchronized 底层原理了解吗？synchronize同步语句块用到了那些指令？修饰方法用到了什么标识？
+ JDK1.6 之后的 synchronized 底层做了哪些优化？锁升级原理了解吗？
+ synchronized 的偏向锁为什么被废弃了？
+ synchronized 和 volatile 有什么区别？
+ ReentrantLock 是什么？
+ 公平锁和非公平锁有什么区别？
+ synchronized 和 ReentrantLock 有什么区别？ 
    - 两者都是可重入锁
    - synchronized 依赖于 JVM 而 ReentrantLock 依赖于 API
    - ReentrantLock 比 synchronized 增加了一些高级功能
+ 可中断锁和不可中断锁有什么区别？



> 不太重要的ReentrantReadWriteLock和StampedLock 
>

+ ReentrantReadWriteLock 是什么？
+ ReentrantReadWriteLock 适合什么场景？
+ 共享锁和独占锁有什么区别？
+ 线程持有读锁还能获取写锁吗？
+ 读锁为什么不能升级为写锁？



+ StampedLock 是什么？
+ StampedLock 的性能为什么比ReadWriteLock更好？
+ StampedLock 适合什么场景？
+ StampedLock 适合什么场景？
+ StampedLock 的底层原理了解吗？

# 下
+ ThreadLocal 有什么用？
+ ThreadLocal 的原理了解吗？本质上是什么？
+ 什么是ThreadLocalMap？ThreadLocalMap的key是什么？value是什么？是由每个线程维护的吗？
+ TreadLocal的数据结构是怎么样的？
+ TreadLocalMap的key是弱引用还是强应用？value呢ThreadLocal 内存泄露问题是为什么会导致呢？
+ 内存泄漏满足的两个条件
+ 如何避免内存泄漏的发生？
+ 如何跨线程传递 ThreadLocal 的值？
+ 什么是InheritableThreadLocal？什么是<font style="color:rgb(60, 60, 67);">TransmittableThreadLocal？哪一个可以支持线程池场景？两个原理分别是什么？</font>
+ <font style="color:rgb(60, 60, 67);">ThreadLocal的应用场景</font>
+ <font style="color:rgb(60, 60, 67);">什么是线程池?</font>
+ <font style="color:rgb(60, 60, 67);">为什么要用线程池？</font>
+ <font style="color:rgb(60, 60, 67);">创建线程池的两种方式？(都是Executor)</font>
+ <font style="color:rgb(60, 60, 67);">Executors创建的线程池的类型 -- FixedTreadPool SingleTreadExecutor CacheTreadPool ScheduledThreadPool分别是什么？</font>
+ <font style="color:rgb(60, 60, 67);">为什么线程池最好不要用Executors创建，而是通过ThreadPoolExecutor构造函数的方式创建？Executors创建有什么弊端？（四种线程池类型分别使用什么队列，有什么缺点）</font>
+ <font style="color:rgb(60, 60, 67);">线程池常见参数有哪些？如何解释？最重要的三个参数是什么？</font>
+ <font style="color:rgb(60, 60, 67);">ThreadPoolExecutor创建的线程池的核心线程会被回收吗？</font>
+ <font style="color:rgb(60, 60, 67);">线程池的拒绝策略有哪些？</font>
+ <font style="color:rgb(60, 60, 67);">如果不允许丢弃任务，应该选择哪个拒绝策略？</font>
+ <font style="color:rgb(60, 60, 67);">CallerRunsPolicy 拒绝策略有什么风险？如何解决？</font>
+ <font style="color:rgb(60, 60, 67);">线程池常用的阻塞队列有哪些？</font>
+ <font style="color:rgb(60, 60, 67);">线程池处理任务的流程了解吗？</font>
+ <font style="color:rgb(60, 60, 67);">线程池中线程异常后，销毁还是复用？</font>
+ <font style="color:rgb(60, 60, 67);">如何给线程池命名？</font>
+ <font style="color:rgb(60, 60, 67);">什么是上下文切换成本？如何设定线程池的大小（分为CPU密集和IO密集）？哪些任务属于CPU密集，哪些任务属于IO密集？</font>
+ <font style="color:rgb(60, 60, 67);">线程数更加严谨的公式是什么？</font>
+ <font style="color:rgb(60, 60, 67);">如何动态修改线程池的参数？</font>
+ <font style="color:rgb(60, 60, 67);">如何设计一个能够根据任务的优先级来执行的线程池？</font>
+ <font style="color:rgb(60, 60, 67);">Future 类有什么用？</font>
+ <font style="color:rgb(60, 60, 67);"></font>


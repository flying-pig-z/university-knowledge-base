<meta name="referrer" content="no-referrer"/>

> 整合自JavaGuide 小林coding
>

## 集合概述
+ JAVA集合主要由哪两个接口派生而来？
+ Collection接口的三个主要子接口是什么？
+ 说说list queue map set 四者对应的数据结构以及该数据结构的特点
+ Arraylist Linkedlist Vector是什么，之间有什么区别
+ Hashset LinkedHashSet TreeSet是什么，之间有什么区别
+ PriorityQueue DelayQueue ArrayDeque是什么，之间有什么区别
+ HashMap LinkedHashMap Hashtable TreeMap是什么？之间有什么区别
+ 怎么选用集合？
+ 为什么要使用集合？ --> 对比数组的好处

> 数据结构 数据类型灵活(泛型) 长度灵活可变 多样化的操作方式
>

> 数组使用泛型会编译错误，但是集合只能存储对象
>

## List
+ ArrayList 和 Array（数组）的区别？ -- 几乎同上
    - 会不会动态扩容或缩容？
    - 是否可以使用泛型？
    - 是否可以使用基本数据类型？
    - 是否有自带方法实现插入，删除，遍历等场景操作？
    - 是否需要创建时候指定大小？
+ ArrayList 和 Vector 的区别?（了解即可）
    - 线程安全 or 不安全?
+ Vector 和 Stack 的区别?（了解即可）
    - 线程安全 or 不安全
    - 两个分别代表什么数据类型？
+ ArrayList 可以添加 null 值吗？
+ ArrayList 插入和删除元素的时间复杂度？
+ LinkedList 插入和删除元素的时间复杂度？
+ LinkedList 为什么不能实现 RandomAccess 接口？
+ ArrayList 与 LinkedList 区别?
    - ArrayList是线程安全的吗？LinkedList呢？
    - 分别采用什么底层数据结构？
    - 插入和删除的复杂度是否受元素位置的影响?
    - 是否支持快速随机访问？
    - 内存空间占用哪个大？
+ 我们平时项目会用到LinkedList吗？LinkedList作者如何评价LinkedList的？
+ ArrayList的扩容机制？
+ 什么是fail-fast快速失败的思想？java.util包怎么践行快速失败的思想的？【乐观锁】
+ 什么是fail-safe安全失败的思想？什么是写时复制?这个在遍历操作的时候有什么缺点？
+ Java 的 CopyOnWriteArrayList 和 Collections.synchronizedList 有什么区别？ 分别有什么优缺点?

> 我实习本地内存很多就用CopyOnWriteArrayList，因为写时复制读取不用加锁比较快。
>

## Set
+ Comparable 和 Comparator 接口干什么用的？
+ Comparable 和 Comparator 分别是哪个包的？这两个接口什么方法用于排序？
+ 怎么自定义排序？
+ 无序性和不可重复性的含义是什么
+ 比较 HashSet、LinkedHashSet 和 TreeSet 三者的异同

> 一个是哈希表，一个是链表+哈希表，一个是红黑树
>

+ HashSet LinkedHashSet和TreeSet适用于什么场景？

## Queue
+ Queue 与 Deque 的区别?
    - Queue是单端队列还是双端队列？Deque呢？
    - Queue和Deque因为容量问题导致操作失败后处理方法有哪两种？
    - Deque有提供模拟栈的方法吗？
+ ArrayDeque 与 LinkedList 的区别
    - 两者都实现了Deque接口，有队列的功能。
    - ArrayDeque底层数据结构是怎么样的？LinkedList呢？
    - ArrayDeque可以存储NULL数据吗？LinkedList呢？
    - ArrayDeque的插入操作和LinkedList哪个块？
    - 哪个实现队列比较好？
    - ArrayDeque可以实现栈吗？
+ PriorityQueue是什么？和Queue的区别是什么？
+ 基于什么数据结构？底层使用什么类型存储数据？
+ PriorityQueue插入和删除是怎么操作数据结构的?复杂度是多少？
+ PriorityQueue是线程安全的吗？可以存储NULL 和 non-comparable 的对象吗
+ PriorityQueue默认是大顶堆还是小顶堆，怎么自定义元素优先级的先后？
+ 什么是 BlockingQueue？经常用于什么模型？为什么阻塞？
+ ArrayBlockingQueue 和 LinkedBlockingQueue 有什么区别？
    - 底层数据结构的实现？
    - 是否有界？
    - 锁是否分离？
    - 内存占用？

## Map
+ HashMap和HashTable的区别？
    - HashMap是线程安全的吗？Hashtable呢？
    - HashMap效率和Hashtable哪个高？为什么？
    - Hashtable的取代方案？
    - HashMap支持null key和null value吗？hashtable呢？
    - HashMap初始容量大小和每次扩充容量大小的不同？
    - 有没有红黑树优化？
    - 有没有哈希扰动函数
+ HashMap和HashSet区别
    - HashSet底层基于HashMap实现，几乎都是直接调用HashMap的方法
+ HashMap 和 TreeMap 区别
    - 底层数据结构的不同
    - TreeMap多了什么能力（排序 and 搜索）
+ HashSet插入相同的元素会发生什么？
+ HashMap的底层实现
+ HashMap 的长度为什么是 2 的幂次方？
+ HashMap 多线程操作导致死循环问题？
+ HashMap 为什么线程不安全？【数据覆盖】
+ HashMap的7种遍历方式
+ ConcurrentHashMap 和 Hashtable 的区别？
    - 底层数据结构分别是什么？
    - **实现线程安全的方式？**

> ConcurrentHashMap1.8之前：分段锁（Segment，继承自ReentrantLock）；1.8之后：使用 synchronized 和 CAS，锁粒度更细。  
Hashtable：一把锁synchronized
>

+ ConcurrentHashMap 能保证复合操作的原子性吗？



    - ****


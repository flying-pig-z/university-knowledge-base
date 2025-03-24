<meta name="referrer" content="no-referrer"/>

## Redis基础
+ 什么是Redis
+ Redis为什么快（内存 网络模型 通信协议 数据结构）
+ 除了Redis还有什么分布式缓存方案？
+ 说一下 Redis 和 Memcached 的区别和共同点
+ 为什么要用 Redis？
+ 怎么保证缓存一致性？
+ 什么是 Redis Module？有什么用？

## Redis应用
+ Redis 除了做缓存，还能做什么？
+ 如何基于 Redis 实现分布式锁？
+ 如何基于 Redis 实现消息队列？

> 三种方式：  
List(Queue)[没有广播]   
pub/sub[消息丢失 消息堆积]   
Stream[在 Redis 发生故障恢复后不能保证消息至少被消费一次]
>

+ 这三种结构有什么优缺点？
+ Redis 可以做搜索引擎么？
+ 如何基于 Redis 实现延时任务？两种方案哪个比较好？

## <font style="color:rgb(60, 60, 67);">Redis数据类型</font>
+ Redis 常用的数据类型有哪些？
+ String的应用场景有什么？
+ String 还是 Hash 存储对象数据更好呢？

> 1. 如果对象比较小且简单,优先使用String类型
> 2. 如果对象字段较多,且需要频繁对部分字段进行操作,使用Hash类型
> 3. 当需要对字段进行计数等原子操作时,优先使用Hash类型
> 4. 根据实际的业务访问模式和性能需求来选择,不要过度优化
>

+ String 的底层实现类型是什么？
+ SDS的五种方式
+ SDS相比于C语言中字符串的提升

> 加入len属性：  
防止缓冲区溢出 -- 根据 len 属性检查空间大小是否满足要求  
获取字符串长度的复杂度较低 -- 直接通过len获取即可  
二进制安全 -- 不用\0判断，而是通过len判断
>
> 减少内存分配次数 -- <font style="color:rgb(60, 60, 67);">SDS 实现了空间预分配和惰性空间释放两种优化策略</font>
>

+ List数据类型的底层实现是什么？
+ 用户购物车信息用String好，还是List好，还是Hash好？
+ 使用 Redis 实现一个排行榜怎么做？
+ Set 的应用场景是什么？
+ 使用 Set 实现抽奖系统怎么做？
+ 使用 Bitmap 统计活跃用户怎么做？
+ 使用 Bitmap 统计活跃用户怎么做？
+ 使用 HyperLogLog 统计页面 UV 怎么做？

## Redis数据类型底层数据结构（小林coding）
+ 五种基本数据类型对应的底层数据结构是什么？



+ SDS底层数据结构是怎么样的？
+ SDS相比于C语言的字符数组有什么优势？（也可以和c++中string比较一下）



+ Redis最早的List是什么结构？有什么缺点？



+ 压缩链表的结构是怎么样的？
+ 压缩链表的优点？（压缩）压缩链表的缺点？（连锁更新）
+ 什么是连锁更新？
+ redis采用什么方式来解决哈希冲突？



+ listpack的结构是怎么样的？为什么没有连锁更新的问题？



+ Redis中哈希表的结构是怎么样的？
+ Redis中是怎么解决哈希冲突的？
+ Redis的哈希表是怎么进行rehash的？什么是渐进式rehash？
+ rehash 触发条件是什么？ 



+ inset的结构是怎么样的
+ inset的优点 -- 为什么相比于哈希表节省内存？
+ intset的升级操作是怎么样的？
+ intset的升级是可逆的吗？



+ quicklist的结构是怎么样的？（通过quicklist的结构你就知道它为什么既能解决普通双向链表内存占用过大的问题，又能解决ziplist大规模连锁更新的问题了）



+ 跳表结构是怎么样的？
+ 跳表节点查询过程是怎么样的？查找复杂度是多少？
+ 跳表相邻两层节点的理想比例是多少？
+ <font style="color:rgb(44, 62, 80);">如果采用新增节点或者删除节点时，来调整跳表节点以维持比例的方法的话，会带来额外的开销。Redis采用什么巧妙的方式？</font>
+ <font style="color:rgb(44, 62, 80);">Redis定义的最高层数是多少？</font>
+ <font style="color:rgb(44, 62, 80);">为什么用跳表而不用平衡树？</font>

## Redis持久化
+ Redis的三种持久化机制？
+ 什么是RDB持久化？
+ RDB 创建快照时会阻塞主线程吗？
+ 执行快照时，数据能被修改吗？（小林coding）



+ 什么是 AOF 持久化？
+ 怎么开启AOF持久化？（在什么文件，通过什么命令）
+ AOF 工作基本流程图是怎样的？
+ 使用到了哪些Linux系统调用？
+ AOF 持久化方式有三种？（fsync的时机 -- 立即 后台线程每秒调用 系统定时调用）
+ <font style="color:rgb(60, 60, 67);">为了兼顾数据和写入性能，使用那种方式好？</font>
+ 什么是Multi Part AOF？在Multi Part AOF中，AOF文件被分为哪三种类型？
+ AOF 为什么是在执行完命令之后记录日志？有什么风险？
+ AOF重写是干什么的？你觉得叫什么比较好？
+ AOF重写是怎么压缩的？（小林coding）
+ AOF 重写缓冲区是干什么的？
+ 怎么开启AOF重写功能？BGREWRITEAOF 命令？<font style="color:rgb(60, 60, 67);">auto-aof-rewrite-min-size和auto-aof-rewrite-percentage配置项？</font>
+ 什么是AOF和RDB的校验机制？
+ 如何选择RDB和AOF？各有什么优缺点？

> RDB就相当于定期备份，AOF就相当于binlog日志。
>

## Redis线程模型
+ Redis主要是多线程还是单线程模型？
+ Redis 基于什么模式设计开发了一套高效的事件处理模型
+ 既然是单线程，那怎么监听大量的客户端连接呢？
+ 那 Redis6.0 之前为什么不使用多线程？
+ Redis6.0 引入多线程的目的是什么？
+ 引入多线程后执行命令是单线程还是多线程？
+ 怎么修改Redis的线程数
+ 官网建议开启多线程吗？多线程写性能提升大吗？
+ Redis的后台线程主要用来干什么？

## Redis内存管理
+ Redis 给缓存数据设置过期时间有什么用？
+ Redis 是如何判断数据是否过期的呢？
+ 常用的过期删除策略 -- 惰性删除 定期删除 延迟队列 定期删除分别是什么样的？
+ Redis 采用的那种删除策略呢？
+ 每次定期删除随机抽查数量是多少？
+ 如何控制定期删除的执行频率？
+ 什么是dynamic-hz
+ 为什么定期删除不是把所有过期 key 都删除呢？
+ 为什么 key 过期之后不立马把它删掉呢？(比如用延迟队列)这样不是会浪费很多内存空间吗？
+ 大量 key 集中过期怎么办？
+ Redis的默认最大内存阈值是多少？
+ Redis的6种内存淘汰策略？

## Redis事务
+ 什么是Redis事务，有什么特点？

> 打包多个请求，不会被中途打断，但是明明一次发送批量执行多个命令就可以了。
>

+ 如何使用 Redis 事务？
+ Redis事务有原子性和持久性吗？
+ Redis事务的缺陷？

## Redis 性能优化
+ 使用pipeline批量操作减少网络传输
+ 原生批量操作命令
+ pipeline和原生批量操作命令的区别？
+ pipeline和Redis事务的区别？
+ Lua脚本的特点
+ 怎么解决大量key集中过期的问题？
+ 什么是 bigkey？（String的value超过多大，复合类型的元素超过多少个）
+ bigkey 是怎么产生的？有什么危害（三个阻塞，客户端 网络 工作线程）？
+ 如何发现 bigkey？
    - Redis 自带的 --bigkeys 参数
    - 使用 Redis 自带的 SCAN 命令
    - 借助开源工具分析 RDB 文件
    - 借助公有云的 Redis 分析服务
+ 如何处理 bigkey？
    - hash拆分
    - 手动清理（SCAN+DEL）[删除也可以批量删除，延长删除]
    - 采用合适的数据结构
+ 什么是 hotkey？（每秒达到多少次）
+ hotkey 有什么危害？
+ 如何发现 hotkey？
    - Redis 自带的 --hotkeys 参数
    - 使用MONITOR 命令
    - 京东开源hotkey/公有云
+ 如何解决 hotkey？
    - 读写分离
    - 使用Redis Cluster
    - 二级缓存
+ Redis中大部分命令复杂度是多少？有哪些命令是O(n)复杂度？有哪些命令是O(n)意思的？
+ 如何设置耗时命令的阈值，如何设置耗时命令的最大记录条数。
+ 如何获取慢查询命令的内容？慢查询日志的每个条目都由哪六个值组成？
+ 什么是内存碎片?为什么会有 Redis 内存碎片? 如何清理 Redis 内存碎片？

## Redis 生产问题
+ 缓存穿透 缓存击穿 缓存雪崩是什么?解决方案是什么？
+ 如何保证缓存和数据库数据的一致性？
+ 哪些情况可能会导致 Redis 阻塞？

## Redis集群
1. 什么是 Sentinel？ 有什么用？
2. 什么是主观下线，客观下线？如何判断节点是否主观下线？Sentinel如何实现故障转移的？为什么建议部署多个sentinel节点？
3. Sentinel 如何选择出新的 master?
4. 如何从 Sentinel 集群中选择出 Leader ？
5. Sentinel 可以防止脑裂吗？



+ 什么是脑裂
+ 脑裂怎么避免？能完全避免吗？



+ 为什么需要redis cluster?解决了什么问题？为什么主从复制+Sentinel还不够？为什么不能只靠提高主机的硬件？是否内置了主从复制和Sentinel的功能?



+ 一个最基本的Redis Cluster架构是怎么样的？（三主三从）为什么每个master要有一个或多个slave？
+ Redis Cluster是如何分片的？怎么计算给定的key应该分布到哪个哈希槽中？
+ 为什么Redis Cluster的哈希槽是16384个？
+ 怎么做让 Redis Cluster 重新分配哈希槽？
+ Redis Cluster扩容期间可以提供服务吗？ASK重定向和MOVED重定向有什么区别？
+ Redis Cluster中的节点是怎么进行通信的？它是怎么内置实现Redis Cluster的功能的？

## Redis主从复制
+ 主从架构是怎么样的？什么是主从复制？
+ 复制流程大致是怎么样的？
+ 全量同步和增量同步的具体流程是怎么样的？
+ replication buffer和repl_backlog_buffer的区别？


### 为什么需要Redis Cluster
高并发场景下，Redis会遇到两大问题 -- 缓存数据量大 读写操作并发量大。

我们要多主多从，主从复制知识增加了从库，Sentinel只是实现了多种故障转移和监控进一步提高了可靠性。总而言之之前只有多从，只能处理读流量。

而Redis Cluster运用分片来实现多主，分散写流量和数据量。

那为什么不提高主机的硬件，要使用多主的架构呢？因为硬件有上限+提高硬件成本高+无法动态扩容和缩容。

而且Redis Cluster也内置了主从复制和Sentinel，无需单独部署Sentinel。

总结：

+ 可以横向扩展缓解写压力和存储压力，支持动态扩容和缩容；
+ 具备主从复制、故障转移（内置了Sentinel机制，无需单独部署Sentinel集群)等开箱即用的功能

### 一个最基本的Redis Cluster架构是怎么样的？
为了保证高可用，Redis Cluster至少需要3个master以及3个slave，也就是说每个 master 必须有1个 slave。

> slave默认是只读的，虽然可以通过配置设置成可读可写，但是不建议这么做。
>

集成主从复制和Cluster：master 和 slave 之间做主从复制实时同步数据。并且使用Cluster在master结点出现故障的时候，从slave结点中选择出一个slave代替master结点。

Redis Cluster 是去中心化的（各个节点基于Gossip进行通信），任何一个master出现故障，其它的master节点不受影响因为key找的是哈希槽而不是是Redis节点不过，Redis Cluster至少要保证宕机的master有一个 slave 可用。

如果宕机的 master 无 slave 的话，为了保障集群的完整性，保证所有的哈希槽都指派给了可用的master，整个集群将不可用这种情况下，还是想让集群保持可用的话可以将cluster-require-full-coverag这个参数设置成 no,cluster-require-full-coverage表示需要16384个slot都正常被分配的时候RedisCluster才可以对外提供服务。

我们添加新的master结点和删除master结点都会重新分配哈希槽。

### Redis Cluster是如何分片的？
Redis Cluster并没有使用一致性哈希，采用的是哈希槽分区，每一个键值对都属于一个 hash slot（哈希槽）。

Redis Cluster通常有16384个哈希槽，要计算给定key应该分布到哪个哈希槽中，我们只需要先对每个key计算CRC-16(XMODEM)校验码，然后再对这个校验码对16384(哈希槽的总数)取模，得到的值即是key对应的哈希槽。

哈希槽的计算公式如下：

```java
HASH_SLOT = CRC16(key) mod NUMER_OF_SLOTS
```

创建并初始化 Redis Cluster 的时候Redis会自动平均分配这16384个哈希槽到各个节点，不需要我们手动分配。女如果你想自己手动调整的话，RedisCluster也内置了相关的命令比如ADDSLOTSADDSLOTSRANGE（后面会详细介绍到重新分配哈希槽相关的命令)。

如果哈希槽确实是当前节点负责，那就直接响应客户端的请求返回结果，如果不由当前节点负责，就会返回- MOVED重定向错误，告知客户端当前哈希槽是由哪个节点负责，客户端向目标节点发送请求并更新缓存的哈希槽分配信息。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1739288783422-58134bf0-ee95-49fb-a0f9-12ff05ebb1a6.png)

这是因为RedisCluster内部可能会重新分配哈希槽比如扩容缩容的时候（后文中有详细介绍到RedisCluster的扩容和缩容问题），这就可能会导致客户端缓存的哈希槽分配信息会有误从上面的介绍中，我们可以简单总结出RedisCluster哈希槽分区机制的优点：解耦了数据和节点之间的关系，提升了集群的横向扩展性和容错性。

### 为什么Redis Cluster的哈希槽是16384个？
总结一下 Redis Cluster 的哈希槽的数量选择16384而不是65536的主要原因：

+ 哈希槽太大会导致心跳包太大，消耗太多带宽；

> 正常的心跳包会携带一个节点的完整配置，它会以幂等的方式更新日的配置这意味着心跳包会附带当前节点的负责的哈希槽的信息。假设哈希槽采用16384,则占空间 2k(16384/8)。假设哈希槽采用e65536,则占空间8k(65536/8)，这是令人难以接受的内存占用。
>

+ 哈希槽总数越少，对存储哈希槽信息的bitmap压缩效果越好；
+ RedisCluster的主节点通常不会扩展太多，16384个哈希槽已经足够用了

> 由于其他设计上的权衡，Redis Cluster不太可能扩展到超过1000个主节点
>

### Redis Cluster 如何重新分配哈希槽？
Redis Cluster中内置了命令

### Redis Cluster扩容期间可以提供服务吗？
**RedisCluster扩容和缩容本质是进行重新分片，动态迁移哈希槽。**

为了保证 Redis Cluster 在扩容和缩容期间依然能够对外正常提供服务，Redis Cluster提供了重定向机制，两种不同的类型：

+ **ASK重定向**：可以看做是临时重定向，后续查询仍然发送到旧节点。
+ **MOVED重定向**：可以看做是永久重定向，后续查询发送到新节点。

客户端向指定节点发送请求命令，从客户端的角度来看，ASK重定向是下面这样的：

1. 如果请求的key对应的哈希槽还在当前节点的话，就直接响应客户端的请求
2. 如果请求的key对应的哈希槽在迁移过程中，但是请求的key还未迁移走的话，说明当前节点任然可以处理当前请求，同样可以直接响应客户端的请求。
3. 如果客户端请求的key对应的哈希槽当前正在迁移至新的节点且请求的key已经被迁移走的话，就会返回-ASK重定向错误，告知客户端要将请求发送到哈希槽被迁移到的目标节点。-ASK重定向错误信息中包含请求key迁移到的新节点的信息。
4. 客户端收到（-ASK）重定向错误后，将会临时（一次性）重定向，自动向新节点发送一条ASKING命令。也就是说，接收到ASKING命令的节点会强制执行一次请求，下次再来需要重新提前发送ASKING命令。
5. 新节点在收到ASKING命令后可能会返回重试错误吴（TRYAGAIN），因为可能存在当前请求的key还在导入中但未导入完成的情况。
6. 客户端发送真正需要请求的命令。
7. ASK重定向并不会同步更新客户端缓存的哈希槽分配信息，也就是说，客户端对正在迁移的相同哈希槽的请求依然会发送到旧节点而不是新节点。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1739331013095-392d7f2f-f978-4b4e-a43d-150958d8fafa.png)如果客户端请求的key对应的哈希槽已经迁移完成的话，就会返回-MOVED重定向错误，告知客户端当前哈希槽是由哪个节点负责，客户端向新节点发送请求并更新缓存的哈希槽分配信息，后续查询将被发送到新节点。

### Redis Cluster中的节点是怎么进行通信的？
Redis Cluster 是一个典型的分布式系统，分布式系统中的各个节点需要互相通信。既然要相互通信就要遵循一致的通信协议，Redis Cluster 中的各个节点基于Gossip 协议来进行通信共享信息，每个Redis节点都维护了一份集群的状态信息。

Redis Cluster 的节点之间会相互发送多种 Gossip 消息：

+ MEET：在 Redis Cluster 中的某个 Redis 节点上执行 CLUSTER MEET ip port命令，可以向指定的Redis节点发送一条MEET信息，用于将其添加进 Redis Cluster 成为新的 Redis 节点。
+ PING/PONG：Redis Cluster 中的节点都会定时地向其他节点发送PING消息，来交换各个节点状态信息，检查各个节点状态，包括在线状态、疑似下线状态PFAIL和已下线状态FAIL。
+ FAlL：Redis Cluster 中的节点A发现B节点PFAIL，并且在下线报告的有效期限内集群中半数以上的节点将B节点标记为PFAIL，节点A就会向集群广播一条FAIL消息，通知其他节点将故障节点B标记为FAIL。
+ ..........

有了 Redis Cluster 之后，不需要专门部署 Sentinel 集群服务了。Redis Cluster相当于是内置了 Sentinel 机制，Redis Cluster 内部的各个 Redis 节点通过 Gossip 协议互相探测健康状态，在故障时可以自动切换。

> **Redis Sentinel原本很多操作主要由Sentinel负责，但是Redis Cluster包括发送PING/PONG监听状态，主从选举之类的操作，都是由各个节点负责的。**
>


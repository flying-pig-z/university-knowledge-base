<meta name="referrer" content="no-referrer"/>

### 堆内存设置
一般设置成服务器内存的一半。比如服务器内存是8G，堆内存就设置成4G

### 垃圾回收器选择
+ 单核使用Serial
+ 在意吞吐量使用Parallel
+ JDK8或11，内存小于4G，使用CMS，大于4G使用G1

> 根据机器分配的堆内存大小进行判断，一般来说，我们认为至少达到4G以上才可以用G1、ZGC等，通常要比如超过8G、16G这样效果才更好。
>

+ JDK17如果是一般内存(小于16G)用G1，超大内存用ZGC和Shenandoah（还有待验证）

### 添加必要的日志
因为以上配置都是根据业务大致分析出来的初始配置，所以我们一定是需要不断地调优的，那么必要的日志相关参数就要添加。如：

```plain
-XX:MaxGCPauseMillis=100：最大 GC 暂停时间为 100 毫秒，可以根据实际情况调整；
-XX:+HeapDumpOnOutOfMemoryError：当出现内存溢出时，自动生成堆内存快照文件；
-XX:HeapDumpPath=/path/to/heap/dump/file.hprof：堆内存快照文件的存储路径；
-XX:+PrintGC：输出 GC 信息；
-XX:+PrintGCDateStamps：输出 GC 发生时间；
-XX:+PrintGCTimeStamps：输出 GC 发生时 JVM 的运行时间；
-XX:+PrintGCDetails：输出 GC 的详细信息；
-Xlog:gc*:file=/path/to/gc.log:time,uptime:filecount=10,filesize=100M：将 GC 日志输出到指定文件中，可以根据需要调整日志文件路径、数量和大小
```

### GC优化 -- CMS
**参考文档：**[**从实际案例聊聊Java应用的GC优化**](https://tech.meituan.com/2017/12/29/jvm-optimize.html)

****

**GC对服务的影响 = (响应时间 + GC时间) × GC次数 / 总时间**

所以优化方向就两个：**降低单次GC时间** 或 **减少GC次数**。

####   Major GC和Minor GC频繁 -- 调整新生代和老年代大小
**参数基本策略（基于活跃数据大小）**

活跃数据 = Full GC后老年代占用空间（取多次平均值）

| 空间 | 倍数 |
| --- | --- |
| 总堆大小 | 3-4倍活跃数据 |
| 新生代 | 1-1.5倍活跃数据 |
| 老年代 | 2-3倍活跃数据 |
| 永久代 | 1.2-1.5倍Full GC后永久代占用 |


#### **高峰期Remark阶段耗时过长**
**CMS四个阶段**

1. **Init-mark（STW）**：标记GC ROOT直接关联对象，很快
2. **Concurrent-mark**：并发标记所有可达对象
3. **Remark（STW）**：重新扫描堆，标记并发期间引用变化的对象
4. **Concurrent-sweep**：并发清理

**问题根因——跨代引用**

+ 新生代对象可能持有老年代对象引用
+ Remark必须扫描整个堆（新生代+老年代）
+ 新生代对象越多，Remark耗时越长

解决方案添加参数 CMSScavengeBeforeRemark，这样就可以强制Remark前执行一次Minor GC

#### 固定内存大小，避免扩缩容
初始内存和最大内存一般设置的一样的，避免 JVM 在运行过程中频繁进行内存扩容和收缩操作，提高应用程序的性能和稳定性。

```plain
-Xms = -Xmx // 堆内存设置一样大
-XX:MaxNewSize = -XX:NewSize // 年轻代设置一样大
-XX:MetaSpaceSize = -XX:MaxMetaSpaceSize // 元空间设置一样大
```






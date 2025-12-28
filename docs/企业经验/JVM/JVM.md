### 堆内存设置
一般设置成服务器内存的一半，初始内存和最大内存一般设置的一样的，避免 JVM 在运行过程中频繁进行内存扩容和收缩操作，提高应用程序的性能和稳定性。

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

### 设置各区的大小 -- TODO
#### CMS
#### G1

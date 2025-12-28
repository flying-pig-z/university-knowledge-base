![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737299248678-702eca3f-2e22-4255-98f9-844501795df4.png)

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737299535770-089315b9-93d2-401f-93d2-577aa93f31b3.png)

这张图展示了 Java NIO 中多路复用的核心架构，下面是各个组件及其关系：

1. 最顶层的 Client

代表多个客户端连接，每个客户端都与一个独立的 Buffer 进行数据交互

2. Buffer (缓冲区)

是 Channel 与 Client 之间的数据缓冲区，所有数据都必须通过 Buffer 进行传输，用于临时存储要读取或写入的数据

3. Channel (通道)

表示一个打开的 IO 连接，与传统 IO 的 Stream 不同，Channel 是双向的，每个 Channel 对应一个 Buffer

4. Selector (选择器)

是整个架构的核心，所有 Channel 都注册(register)到 Selector 上，通过单线程监控多个 Channel 的 IO 事件。

5. Thread (线程)

底部的单个线程通过 select 调用，负责监控和处理所有注册的 Channel 上的事件。

工作流程：

1. 所有 Channel 都注册到 Selector 上
2. 单个线程通过 select() 调用监听所有 Channel
3. 当有 IO 事件发生时，Selector 会得到通知
4. 线程可以处理就绪的 Channel，从而实现多路复用

这种架构的优点：

+ 单线程管理多个连接，减少线程开销
+ 避免了传统的阻塞 IO 模型中的线程浪费
+ 提高了服务器的并发处理能力
+ 使用 Buffer 提供了更高效的数据处理机制

NIO通过 Selector 这个核心组件，实现了用更少的线程处理更多连接的目标。


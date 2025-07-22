<meta name="referrer" content="no-referrer"/>

TCP中的TIME WAIT状态是TCP连接关闭过程中的一个重要状态。当TCP连接主动关闭方发送最后一个ACK包后，该连接会进入TIME WAIT状态，并在这个状态下保持一段时间。

TIME WAIT状态的主要作用:

1. 确保最后一个ACK包能被成功接收。如果这个ACK包丢失，对方会重发FIN包，而处于TIME WAIT状态的一方可以重发ACK包。
2. 防止"延迟的数据包"干扰新连接。TIME WAIT状态确保所有可能延迟的数据包在新连接建立前都已经从网络中消失，避免旧连接的数据包被误认为是新连接的数据包。

TIME WAIT状态虽然有助于确保TCP连接的可靠关闭，但在高并发服务器环境中，大量的TIME WAIT连接会占用系统资源。为了解决这个问题，一些系统提供了配置选项来调整TIME WAIT超时时间或启用TIME WAIT重用。


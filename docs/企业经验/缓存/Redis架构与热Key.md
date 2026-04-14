<meta name="referrer" content="no-referrer"/>

## Redis架构
### 单机架构
![](https://cdn.nlark.com/yuque/0/2026/png/42768076/1768380966715-0709f079-d190-4351-8299-384527c5337f.png)

### 主从复制
![](https://cdn.nlark.com/yuque/0/2026/png/42768076/1768380998555-c85b05da-ea64-4eca-b06c-e91fb98d5cf4.png)

### 哨兵模式
![](https://cdn.nlark.com/yuque/0/2026/png/42768076/1768381028652-08a61eaf-62d3-462b-b0c8-5e9e57485de4.png)

### Cluster集群模式
![](https://cdn.nlark.com/yuque/0/2026/png/42768076/1768381051445-a310726a-6d28-4d34-ae38-7ff609d5bac8.png)

### 比较
![](https://cdn.nlark.com/yuque/0/2026/png/42768076/1768381083999-56c971a9-95f8-4f64-8e74-9b8bba49015c.png)

**主从架构只能一主多从，而不能多主多从，所以只能扩展读流量。**

**而且扩展是有上限的，因为只有一个主机，从机过多同步就是个问题。**

**Cluster是去中心化的，理论上没有上限。**

## 解决热点数据
Redis单机并发大概是几万。

比如某个商品信息存放在Redis中，然后并发很高，可能造成某个实例的CPU过高。

### 多级缓存
在Redis前面套一层本地缓存

### 主从
部署主从结构或者Cluster架构可以提升读流量/写流量上限

### 分桶
如果是在Cluster的架构下，数据会被分散在不同的节点，这时候配合分桶防止某些节点并发过大、

分桶就是将一个key拆分成多份/创建多个副本。

```plain
原始 key: product:1001
拆分为:
  product:1001:0  → Node A
  product:1001:1  → Node B
  product:1001:2  → Node C

客户端: hash(requestId) % 3 → 选择桶
```






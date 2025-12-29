<meta name="referrer" content="no-referrer"/>

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737164887428-983559f8-1ed1-45b7-84bd-9a845449e524.png)

像这样的购物车信息后String好，还是Hash好，还是List好呢？

对于购物车这种场景，建议使用 Hash 结构，原因如下：

1. **数据结构匹配度**：
+ Hash 结构的键值对完美匹配购物车中"商品ID-数量"的对应关系
+ 每个用户的购物车可以用一个 Hash 结构存储，key 为 `cart:{userId}`，field 为商品 ID，value 为商品数量
2. **操作便利性**：
+ 添加/更新商品数量：`HSET cart:1001 product:123 2`
+ 增加商品数量：`HINCRBY cart:1001 product:123 1`
+ 删除商品：`HDEL cart:1001 product:123`
+ 获取购物车所有商品：`HGETALL cart:1001`
+ 获取购物车商品总数：`HLEN cart:1001`
3. **性能考虑**：
+ **Hash 支持部分更新，不需要像 String 那样序列化整个购物车数据**
+ **相比 List，Hash 在查找和更新指定商品时更高效**

实际使用示例：

```plain
# 添加商品到购物车
HSET cart:1001 product:123 2 product:456 1

# 增加商品数量
HINCRBY cart:1001 product:123 1

# 获取指定商品数量
HGET cart:1001 product:123

# 获取整个购物车
HGETALL cart:1001

# 删除商品
HDEL cart:1001 product:456
```

为什么不选择其他结构：

**String 结构的劣势**：

+ 每次更新都需要序列化整个购物车数据
+ 无法针对单个商品进行原子性的增减操作
+ 并发情况下可能会出现数据不一致

**List 结构的劣势**：

+ 不适合存储键值对关系
+ 查找和更新指定商品较困难
+ 需要遍历整个列表来更新商品数量

因此，考虑到购物车场景的特点（频繁的商品添加、数量修改、单个商品删除等操作），Hash 结构是最合适的选择。

  



<meta name="referrer" content="no-referrer"/>

MyBatis 提供了两级缓存：一级缓存和二级缓存。

## 一级缓存（本地缓存）
1. 特点：

作用域为 SqlSession 级别，默认开启，无法关闭，存储在 SqlSession 对象中的 HashMap 里。

2. 工作机制：

同一个 SqlSession 中，执行相同的 SQL 查询时，第二次以后会直接从一级缓存获取。

如果发生下列情况，一级缓存会失效：

+ 执行了 SqlSession.clearCache()
+ 执行了增删改操作
+ SqlSession 关闭或提交事务
+ 手动清空缓存

## 二级缓存（全局缓存）
1. 特点：
+ 作用域为 namespace（mapper）级别
+ 默认关闭，需要手动配置开启
+ 可以被多个 SqlSession 共享
+ 生命周期与应用同步
2. 开启配置：

```xml
<!-- 全局配置文件中启用 -->
<settings>
    <setting name="cacheEnabled" value="true"/>
</settings>
<!-- mapper.xml中配置 -->
<cache/>
```

3. 详细配置选项：

```xml
<cache
  eviction="FIFO"
  flushInterval="60000"
  size="512"
  readOnly="true"/>
```

## 缓存查找顺序
先查找二级缓存，如果没找到，再查找一级缓存，都没找到，查询数据库。

## 使用建议
1. 一级缓存：

适合用于单线程环境，事务操作中可以提高性能，注意在分布式环境中可能造成数据不一致。

2. 二级缓存：

适合于读多写少的数据，注意实体类需要实现 Serializable 接口

在以下场景慎用：

+ 多表关联查询
+ 实时性要求高的数据
+ 分布式环境

## 自定义缓存
MyBatis 还支持自定义缓存实现：

```xml
<cache type="com.example.CustomCache"/>
```

自定义缓存类需要实现 Cache 接口：

```java
public interface Cache {
    String getId();
    void putObject(Object key, Object value);
    Object getObject(Object key);
    Object removeObject(Object key);
    void clear();
    int getSize();
}
```

## 注意事项
1. 性能考虑：
+ 一级缓存直接存在内存中，访问速度最快
+ 二级缓存需要序列化和反序列化，性能略低
2. 数据一致性：
+ 在多表操作时要特别注意缓存一致性问题
+ 分布式环境下建议使用专业的缓存中间件（如 Redis）
3. 缓存更新：
+ 增删改操作会导致相关缓存失效
+ 可以通过 flushCache 属性控制是否刷新缓存

通过合理使用 MyBatis 的缓存机制，可以显著提升应用性能，但要根据具体业务场景选择合适的缓存策略。在复杂的分布式系统中，可能需要考虑使用专业的缓存解决方案来替代 MyBatis 的二级缓存。



## 补充 --  SqlSession  
每次开启新事务时会创建新的 SqlSession，显式的调用openSession()方法也可以创建SqlSession。


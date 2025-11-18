<meta name="referrer" content="no-referrer"/>

软件系统的处理能力是有限的，为了防止流量过大让系统崩溃，我们要对系统进行限流来防止突如其来的大流量。

限流可能会导致用户的请求无法被正确处理或者无法立即被处理，不过，这往往也是权衡了软件系统的稳定性之后得到的最优解。

## 一.限流的粒度和方案
### 1.粗粒度限流 and 网关限流
**比较粗粒度的限流就是针对IP地址或者用户ID等进行限流。这种限流通常是在网关过滤器处实现的。**

如使用Spring Cloud Gateway的KeyResolver组件进行限流。 也可以整合Sentinel组件进行限流。

### 2.细粒度限流 and 业务侧限流
**而我们往往还需要在业务侧进行更加细粒度的限流，对某个方法，甚至某个方法的参数，甚至对某个热点参数进行更加精细的限流，以此来控制热点资源的访问。**

业务侧限流常使用的有Sentinel组件。 当然也可以用Redis+LUA脚本的方式定义限流注解，进行轻量级的限流。

为什么使用Redis+Lua的方式？ 主要有两点原因：

+ 减少了网络开销：我们可以利用 Lua 脚本来批量执行多条 Redis 命令，这些 Redis 命令会被提交到 Redis 服务器一次性执行完成，大幅减小了网络开销。
+ 原子性：一段 Lua 脚本可以视作一条命令执行，一段 Lua 脚本执行过程中不会有其他脚本或 Redis 命令同时执行，保证了操作不会被其他指令插入或打扰。

## 二.四种常见的限流算法（案例使用Redis+Lua实现）
### 1.固定窗口计数器算法
**固定窗口算法又叫做时间窗口算法。**

**其原理是规定固定大小的窗口，判断该窗口的请求是否达到规定的最大值。**

**在没有窗口/窗口过期后第一次请求会创建窗口。****比如窗口大小是1s，那窗口就固定在第一次创建该窗口后的那一秒，一秒之后过期。**

**然后我们会规定每个窗口的最大请求量，如果这个窗口的请求已经到达了这个量，那新的请求将不被允许。**

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1742781602783-ac251a1c-b1df-4a6b-9343-d02ae0121a65.png)

Redis实现固定窗口算法：

暂时无法在飞书文档外展示此内容

Redis的Lua脚本：

```plain
local rateLimitKey = KEYS[1];
local rate = tonumber(ARGV[1]);
local rateInterval = tonumber(ARGV[2]);

local allowed = 1;
local ttlResult = 0;
local currValue = redis.call('incr', rateLimitKey);
if (currValue == 1) then
    redis.call('expire', rateLimitKey, rateInterval);
    allowed = 1;
else
    if (currValue > rate) then
        allowed = 0;
        ttlResult = redis.call('ttl', rateLimitKey);
    end
end
return { allowed, ttlResult }
```

### 2.滑动窗口计数器算法
![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1742781602759-0fde09c0-15a6-4e78-97a9-6d1f947478b6.png)

**滑动窗口算法顾名思义就是窗口是滑动的，比如窗口大小是1s，那每次请求的窗口就是这次请求的的前一秒这段时间。**

**下面用Redis的set集合存放请求，如果超出前一秒的请求就进行删除。**

Redis实现滑动窗口算法：

暂时无法在飞书文档外展示此内容

Lua脚本：

```plain
-- 切换到单命令复制模式
redis.replicate_commands()

-- 定义键名和限流参数
local key = KEYS[1]
local window_size = tonumber(ARGV[1])  -- 窗口大小，单位为秒
local limit = tonumber(ARGV[2])       -- 限制的请求数

-- 获取当前时间戳
local current_time = tonumber(redis.call('TIME')[1])

-- 计算窗口的起始时间戳和结束时间戳
local window_start = current_time - window_size
local window_end = current_time

-- 删除窗口外的旧数据，保留窗口内的数据
redis.call('ZREMRANGEBYSCORE', key, '-inf', window_start)

-- 统计当前窗口内的请求数量
local current_count = redis.call('ZCARD', key)

-- 如果当前请求数量未超过限制，则增加当前请求的时间戳到有序集合中
if current_count < limit then
    redis.call('ZADD', key, current_time, current_time)
    redis.call('EXPIRE', key, window_size + 1)  -- 设置过期时间略大于窗口大小，确保过期时删除整个键
    return true
else
    return false  -- 修正拼写错误
end
```

### 3.令牌桶算法
我们有一个桶，里面存放着令牌，每次请求都会消耗一定数量的令牌，消耗完就不能继续请求。 但是桶中的令牌会以一定速率增加（不会大于桶的容量）。

比如一个桶有10滴水，每次请求都会消耗1滴水，但是桶每秒都会增加1滴水。如果请求速率大于消耗速率，那么总有一天会消耗完，只能等继续生成。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1742781602816-c546ac37-90e3-461f-8e6a-36d2b6974b7c.png)

Redis实现令牌桶算法思路：

暂时无法在飞书文档外展示此内容

```plain
-- 根据传入的KEYS和ARGV获取相应的键和参数
local tokens_key = KEYS[1] .. '_token'        -- 存储令牌数量的键名
local timestamp_key = KEYS[1] .. '_timestamp' -- 存储时间戳的键名

-- 从ARGV中获取参数并转换为数值
local bucketCapacity = tonumber(ARGV[1])       -- 令牌桶容量
local generateTokenRate = tonumber(ARGV[2])    -- 令牌生成速率
local consumeTokenPerReq = tonumber(ARGV[3])   -- 每次请求消耗的令牌数

-- 获取当前时间戳（秒级）
local now = redis.call('TIME')[1]

-- 计算填充时间和TTL
local fill_time = bucketCapacity / generateTokenRate
local ttl = math.floor(fill_time * 2)

-- 获取上存储的令牌数量，如果不存在则默次认为令牌桶容量
local last_tokens = tonumber(redis.call("get", tokens_key))
if last_tokens == nil then
    last_tokens = bucketCapacity
end

-- 获取上次刷新的时间戳，如果不存在则默认为0
local last_refreshed = tonumber(redis.call("get", timestamp_key))
if last_refreshed == nil then
    last_refreshed = 0
end

-- 计算时间间隔，上次还存在的令牌数+与上次时间间隔*生成速率=目前的令牌数（注意目前的令牌数最大为桶的容量）
local delta = math.max(0, now - last_refreshed)
local filled_tokens = math.min(bucketCapacity, last_tokens + (delta * generateTokenRate))

-- 判断当前请求是否允许（目前的令牌数是否大于等于请求需要消耗的令牌数量）
local allowed = 0
if filled_tokens >= consumeTokenPerReq then
    allowed = 1
end

-- 如果TTL大于0，则更新令牌数量和时间戳的键值对
if ttl > 0 then
    redis.call("setex", tokens_key, ttl, filled_tokens - consumeTokenPerReq)
    redis.call("setex", timestamp_key, ttl, now)
end

-- 返回允许的请求数和更新后的令牌数量
return allowed
```

### 4.漏桶算法
我们可以把发请求的动作比作成注水到桶中，我们处理请求的过程可以比喻为漏桶漏水。我们往桶中以任意速率流入水，以一定速率流出水。当水超过桶流量则丢弃，因为桶容量是不变的，保证了整体的速率。

如果想要实现这个算法的话也很简单，准备一个队列用来保存请求，然后我们按一定速率从队列中处理请求执行就好了（和消息队列削峰/限流的思想是一样的）。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1742781602778-61983e90-2ed4-4e0e-a2a8-2f1cd41c9c8e.png)

相比于令牌桶算法，漏桶算法处理流量速度固定，无法应对突然激增的流量，所以感觉这种方法进行限流不好。所以这里不做实现。

### 5.分桶限流算法(TODO)

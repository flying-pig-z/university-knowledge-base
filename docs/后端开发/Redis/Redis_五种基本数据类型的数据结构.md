<meta name="referrer" content="no-referrer"/>

## String (字符串)
底层实现：SDS (Simple Dynamic String)

### 与C语言字符串比较
与C字符串不同，包含长度信息，支持快速获取长度

+ 二进制安全，可以存储任何二进制数据。
+ 内存预分配机制，减少频繁内存分配
+ 惰性空间释放，避免频繁释放内存

> SDS和C++的String一样都是动态的，也都有长度信息
>

### List (列表)
底层实现：

+ 在Redis 3.2之前：
    - 数据量较少：压缩列表(ziplist)
    - 数据量较大：双向列表(linkedlist)
+ Redis 3.2之后：QuickList (快速列表) 

> QuickList 结合了linkedlist和ziplist的优点，将多个ziplist用双向指针连接起来，平衡了存储效率和操作性能。
>

### Hash (哈希)
底层实现：

+ ziplist(压缩列表)：当键值对较少且值较小时使用【默认键或值长度小于64字节且键值对数量超过512个】

> 例如，对于哈希表 { "name": "Tom", "age": 25 }：ZipList 中的条目将是：["name", "Tom", "age", "25"]
>
> 这时候复杂度其实是O(n)，小数据量并不需要哈希表优化，ziplist可以节省内存。
>

+ hashtable(哈希表)：当键值对数量较多或值较大时使用 

> 采用拉链法解决冲突，支持动态扩容和缩容
>

### Set (集合)
底层实现：

+ intset(整数集合)：当集合中的元素都是整数且数量较少时使用【默认小于512个】

> intset只能存储整数，而ziplist可以存储整数和字符串。
>
> 因为intset每个元素大小都一样，所以可以随机存储，查找某个数字查找的复杂度是O(logN)。
>
> 增删改的时候不会发生级联更新，但是会发生升级。
>

+ hashtable(哈希表)：当集合中包含非整数元素或元素数量较多时使用

### Sorted Set/ZSet (有序集合)
底层实现：

+ ziplist(压缩列表)：元素数量少且值较小时使用【默认小于512个】

> Sorted Set的每个元素实际上是按"元素-分数"交替存储的，所以和上面的哈希结构一样也是使用ziplist。
>
> 虽然是有序的，但是因为ziplist不支持随机访问，所以查询复杂度是O(n)。
>
> 但是对于 ZRANGE, ZREVRANGE和范围等命令则能更快的访问，而且也便于后面升级skiplist的时候不用再次排序。
>

+ skiplist(跳跃表)+hashtable： 
    - skiplist：保证有序性，提供O(logN)的平均查找复杂度
    - hashtable：保存member到score的映射，提供O(1)的查找性能

> ziplist和skiplist一样，都是需要维护一个有序的列表，当插入一个元素的时候，插入它该插入的位置。
>
> skiplist先走上层索引后走下层索引的方式可以实现更快的寻找。
>


<meta name="referrer" content="no-referrer"/>

Java中最常见的集合API其实就List Queue Map Set Stack这五种。

### Collection接口
基本操作方法：

+ `add(E element)`: 添加元素到集合中
+ `remove(Object o)`: 从集合中移除指定元素
+ `clear()`: 清空集合中的所有元素

> 基本增删操作
>

+ `isEmpty()`: 判断集合是否为空
+ `size()`: 返回集合中的元素个数

> 集合返回元素个数都是size()，而数组返回个数是length属性，而String是length()
>

元素查找方法：

+ `contains(Object o)`: 判断集合是否包含指定元素
+ `containsAll(Collection<?> c)`: 判断集合是否包含另一个集合的所有元素

> 注意是contains不是contain，包括map也是containsKey containsValue
>

集合操作方法：

+ `addAll(Collection<? extends E> c)`: 将另一个集合中的所有元素添加到当前集合
+ `removeAll(Collection<?> c)`: 移除当前集合中与指定集合相同的所有元素
+ `retainAll(Collection<?> c)`: 仅保留当前集合中与指定集合相同的元素
+ `toArray()`: 将集合转换为数组

遍历方法：

+ `iterator()`: 返回一个迭代器用于遍历集合
+ `forEach(Consumer<? super E> action)`: Java 8引入的用于遍历集合的方法

### List
以下是List接口独有的核心方法：

1. 位置相关的操作
+ `add(int index, E element)`: 在指定位置插入元素
+ `addAll(int index, Collection<? extends E> c)`: 从指定位置开始插入集合中的所有元素
+ `get(int index)`: 获取指定位置的元素
+ `set(int index, E element)`: 替换指定位置的元素
+ `remove(int index)`: 删除指定位置的元素
2. 搜索操作
+ `indexOf(Object o)`: 返回指定元素第一次出现的位置，不存在返回-1
+ `lastIndexOf(Object o)`: 返回指定元素最后一次出现的位置，不存在返回-1
3. 范围视图
+ `subList(int fromIndex, int toIndex)`: 返回列表中指定范围内的视图

### Queue
+ Queue 接口可以由 LinkedList 或 ArrayDeque 实现
+ 添加元素：offer or add
+ 删除元素：poll or remove
+ 查看头部元素但不移除：peek or element

### Map
1. 添加和修改元素
+ `put(K key, V value)`: 将指定的键值对添加到Map中。如果键已存在，则更新值并返回旧值
+ `putAll(Map<? extends K,? extends V> m)`: 将另一个Map中的所有键值对添加到当前Map中
2. 获取元素
+ `get(Object key)`: 根据键获取对应的值，如果键不存在返回null
+ `getOrDefault(Object key, V defaultValue)`: 获取键对应的值，如果键不存在则返回指定的默认值
3. 删除元素
+ `remove(Object key)`: 删除指定键的键值对，并返回对应的值
+ `clear()`: 清空Map中的所有元素
4. 查询操作
+ `containsKey(Object key)`: 判断是否包含指定的键
+ `containsValue(Object value)`: 判断是否包含指定的值
+ `isEmpty()`: 判断Map是否为空
+ `size()`: 返回Map中键值对的数量
5. 视图操作
+ `keySet()`: 返回所有键的Set集合
+ `values()`: 返回所有值的Collection集合
+ `entrySet()`: 返回所有键值对的Set集合
6. Java 8新增的方法
+ `merge(K key, V value, BiFunction<V,V,V> remappingFunction)`: 合并键值对
+ `compute(K key, BiFunction<K,V,V> remappingFunction)`: 计算并更新键对应的值
+ `computeIfAbsent(K key, Function<K,V> mappingFunction)`: 当键不存在时，计算并添加键值对
+ `computeIfPresent(K key, BiFunction<K,V,V> remappingFunction)`: 当键存在时，计算并更新值

### Set


### Collections
我来介绍一下Java中Collections工具类的常用方法，按照不同的功能类别来组织：

排序相关：

```java
// 对List进行排序（要求元素实现Comparable接口）
Collections.sort(list);  

// 使用自定义比较器排序
Collections.sort(list, comparator);

// 反转List中元素的顺序
Collections.reverse(list);

// 随机打乱List中的元素顺序
Collections.shuffle(list);
```

查找和替换：

```java
// 二分查找（要求List已排序）
int index = Collections.binarySearch(list, key);

// 返回集合中最大元素
T max = Collections.max(collection);

// 返回集合中最小元素
T min = Collections.min(collection);

// 统计指定元素在集合中出现的次数
int frequency = Collections.frequency(collection, element);

// 替换集合中所有的oldVal为newVal
Collections.replaceAll(list, oldVal, newVal);
```

集合操作：

```java
// 将源列表复制到目标列表
Collections.copy(dest, src);

// 用指定元素填充List
Collections.fill(list, obj);

// 返回空的不可变集合
List<T> emptyList = Collections.emptyList();
Set<T> emptySet = Collections.emptySet();
Map<K,V> emptyMap = Collections.emptyMap();

// 返回只包含一个元素的不可变集合
List<T> singletonList = Collections.singletonList(obj);
```

同步控制：

```java
// 将集合包装为线程安全的集合
List<T> syncList = Collections.synchronizedList(list);
Set<T> syncSet = Collections.synchronizedSet(set);
Map<K,V> syncMap = Collections.synchronizedMap(map);
```

不可变集合：

```java
// 返回不可修改的集合视图
List<T> unmodifiableList = Collections.unmodifiableList(list);
Set<T> unmodifiableSet = Collections.unmodifiableSet(set);
Map<K,V> unmodifiableMap = Collections.unmodifiableMap(map);
```

其他实用方法：

```java
// 交换List中指定位置的元素
Collections.swap(list, i, j);

// 返回集合中指定元素第一次出现的位置
int index = Collections.indexOfSubList(source, target);

// 返回两个集合的交集数量
int common = Collections.disjoint(collection1, collection2);
```

### String
1. 获取字符串信息类方法:
+ `length()` - 返回字符串长度
+ `isEmpty()` - 判断字符串是否为空
+ `charAt(int index)` - 返回指定位置的字符
+ `indexOf(String str)` - 返回字符串第一次出现的位置
+ `lastIndexOf(String str)` - 返回字符串最后一次出现的位置
2. 字符串比较类方法:
+ `equals(Object obj)` - 比较两个字符串内容是否相等
+ `equalsIgnoreCase(String str)` - 忽略大小写比较字符串
+ `compareTo(String str)` - 按字典顺序比较两个字符串
+ `startsWith(String prefix)` - 判断是否以指定字符串开头
+ `endsWith(String suffix)` - 判断是否以指定字符串结尾
3. 字符串操作类方法:
+ `substring(int beginIndex)` - 从指定位置截取到末尾
+ `substring(int beginIndex, int endIndex)` - 截取指定范围的子串
+ `concat(String str)` - 连接两个字符串
+ `replace(char oldChar, char newChar)` - 替换字符
+ `replaceAll(String regex, String replacement)` - 替换所有匹配的子串
+ `trim()` - 去除首尾空格
+ `toLowerCase()` - 转换为小写
+ `toUpperCase()` - 转换为大写
4. 字符串拆分与合并:
+ `split(String regex)` - 按照指定分隔符分割字符串
+ `join(CharSequence delimiter, CharSequence... elements)` - 使用分隔符将字符串数组连接

对字符串排序：

```java
String str = "dacbfe";
// 转换为字符数组
char[] chars = str.toCharArray();
// 排序字符数组
Arrays.sort(chars);
// 转回字符串
String sortedStr = new String(chars);
// 结果: "abcdef"
```






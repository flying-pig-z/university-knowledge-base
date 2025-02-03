<meta name="referrer" content="no-referrer"/>

> 来自AI
>

ArrayList 的扩容涉及几个关键点：

1. 初始容量
+ 当使用无参构造函数创建 ArrayList 时，会创建一个空数组 `DEFAULTCAPACITY_EMPTY_ELEMENTDATA`
+ 第一次添加元素时，会将容量扩展为默认值 10
+ 如果使用有参构造函数指定初始容量，则直接创建对应大小的数组
2. 扩容触发条件
+ 当添加元素时，如果当前元素个数 size 大于等于数组容量 capacity，就会触发扩容
+ 扩容通过 `grow()` 方法实现
3. 扩容过程

```java
private void grow(int minCapacity) {
    int oldCapacity = elementData.length;
    // 新容量 = 旧容量 + 旧容量/2，即扩容为原来的 1.5 倍
    int newCapacity = oldCapacity + (oldCapacity >> 1);
    // 如果新容量还不够，则直接使用需要的最小容量
    if (newCapacity - minCapacity < 0)
        newCapacity = minCapacity;
    // 如果新容量超过最大限制，则调用hugeCapacity()
    if (newCapacity - MAX_ARRAY_SIZE > 0)
        newCapacity = hugeCapacity(minCapacity);
    // 创建新数组并复制数据
    elementData = Arrays.copyOf(elementData, newCapacity);
}
```

4. 扩容特点
+ 每次扩容后容量变为原来的 1.5 倍
+ 使用 `Arrays.copyOf()` 复制数组，这是一个系统级别的复制操作，性能较好
+ 如果扩容后大小超过 `MAX_ARRAY_SIZE`（Integer.MAX_VALUE - 8），则可能抛出 OutOfMemoryError
5. 性能考虑
+ 扩容操作涉及创建新数组并复制数据，时间复杂度为 O(n)
+ 频繁扩容会影响性能，所以在已知数据量的情况下，建议使用有参构造函数指定初始容量
+ 也可以使用 `ensureCapacity()` 方法提前扩容，避免频繁扩容
6. 内存优化

```java
// 如果需要优化内存占用，可以使用 trimToSize() 方法
public void trimToSize() {
    modCount++;
    if (size < elementData.length) {
        elementData = (size == 0)
          ? EMPTY_ELEMENTDATA
          : Arrays.copyOf(elementData, size);
    }
}
```

使用建议：

1. 当明确知道需要存储的元素数量时，最好在创建 ArrayList 时就指定初始容量
2. 如果需要频繁在尾部添加元素，ArrayList 是个好选择
3. 如果需要频繁在中间插入或删除元素，考虑使用 LinkedList
4. 如果要优化内存占用，可以在操作完成后调用 trimToSize()


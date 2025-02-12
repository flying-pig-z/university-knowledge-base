<meta name="referrer" content="no-referrer"/>

## 数组
二分法：升序数组查找 

双指针：

链表中环的检测 and 中点查找 and 移除链表倒数第n个节点 and 寻找数组或链表中的重复元素 and 判定回文链表 and 滑动窗口的优化 and 求链表的第 k 个节点 and 三数之和 and 四数之和

三数之和：单循环+双指针（将O(N3)降为O(N2)）

四数之和：双层循环+双指针

## 链表
虚拟头指针简化对头结点的特殊处理，提高编码速度

检测环形链表 -- 快慢指针 or 哈希表

链表相交 -- 尾部对齐

## 哈希表/哈希集合
常见的三种哈希结构：

+ 数组
+ set（集合）
+ map（映射）

Hash集合常用于**快速判断一个元素是否出现不重复集合里**，Hash表常用于**不重复元素的统计**。 

**如果元素个数比较少 and 数组元素可知，那就直接使用数组。**

## 字符串
字符串问题实际上就是数组问题。

KMP算法 -- 检测字符串中有无某子字符串

字符串s是否由它的一个子串重复多次构成 -- s+s后去头元素和尾元素，检测其中是否还含有s，如果有就由它的一个子串重复多次构成

## 栈和队列
模拟题

前K个高频元素 -- 优先队列

## 二叉树
要不就递归，要不就层序遍历。

其实很多二叉树的题目层序遍历都能做，而且甚至更好理解。

有些题目比较适合用递归。

递归的话要记住递归三部曲：递归的定义，终止条件，递归中的流程。

而有些题目还要配合回溯，这类题目比较难。

## 回溯算法
> 练个几题其实不难
>

1. 回溯函数是基于递归的，所以回溯函数的三要素也一样。函数定义 返回条件 执行过程。
2. 剪枝优化：<font style="color:rgb(64, 64, 64);">许多分支在未完全展开前即可判定为无效，通过预判提前return终止无效递归。</font>
3. **<font style="color:rgb(64, 64, 64);">面对多种条件任意选择搭配，回溯就是解决这种问题，for循环就是遍历条件，然后backtracking函数之后进行条件的撤销，就达到了尝试不同条件的目的。</font>**
4. 模板如下：

```java
void backtracking(参数) {
    if (终止条件) {
        存放结果 or 其他操作;
        return;
    }

    // 这里可以利用startIndex防止重复选择之类的
    for (选择：各种可能的路) {
        处理节点;
        backtracking(参数); // 递归
        回溯，撤销处理结果
    }
}
```

5. 我们可以画决策树来更好的理清问题
6. 例如经典的组合问题，这时候回溯法解决的都是在集合中递归查找子集，集合的大小就构成了树的宽度，递归的深度就构成了树的深度。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737462402067-a4a3faa2-b1e7-4e62-91e9-5a52a33d41d1.png)

```java
    class Solution {
        List<List<Integer>> result = new ArrayList<>();
        LinkedList<Integer> subResult = new LinkedList<>();

        public List<List<Integer>> combine(int n, int k) {
            backtracking(n, k, 1);
            return result;
        }

        public void backtracking(int n, int k, int startIndex) {
            if (subResult.size() == k) {
                result.add(new ArrayList<>(subResult));// 注意这里不能直接result.add(subResult);
                return;
            }
            // 剪枝条件 -- 到i及其之后的数据数量无法满足还需要的元素数量的情况
            // n - i + 1 >= k - subResult.size()
            // i <= n - k + subResult.size() + 1
            for (int i = startIndex; i <= n - k + subResult.size() + 1; i++) {
                subResult.add(i);
                backtracking(n, k, i + 1);
                subResult.removeLast();
            }
        }
    }
```

> 这里的startIndex可以防止重复选择。
>

## 贪心算法
局部最优推出全局最优

## 动态规划
三要素：

1. <font style="color:rgb(44, 62, 80);">dp数组（dp table）以及下标的含义</font>
2. <font style="color:rgb(44, 62, 80);">dp数组如何初始化</font>
3. <font style="color:rgb(44, 62, 80);">递推公式和遍历顺序</font>

## 比较
回溯是穷举所有可能，适合找所有解或特定解；动态规划通过记忆化避免重复计算，适合找最优解；贪心适合局部最优推出全局最优，是动态规划的特例。

1. 如果是求最优解： BFS 动态规划 贪心
    - 有重叠子问题 → 动态规划
    - 局部最优导致全局最优 → 贪心
    - 最短路径类型 → BFS
2. 如果是求所有解或特定解： 回溯 BFS DFS 
    - 组合/排列/子集问题 → 回溯
    - 图的连通性/可达性 → DFS
    - 最少步数/层级遍历 → BFS
3. 如果是单一可行解： BFS DFS 
    - 深度优先的场景 → DFS
    - 按层推进的场景 → BFS




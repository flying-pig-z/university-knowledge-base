<meta name="referrer" content="no-referrer"/>

## 例题（**LeetCode 28 题**）
### 题目
**找出字符串中第一个匹配项的下标 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。**

**如果 needle 不是 haystack 的一部分，则返回 -1 。 **

**示例 1： ** 输入：haystack = "sadbutsad", needle = "sad" 

输出：0 

解释："sad" 在下标 0 和 6 处匹配。 第一个匹配项的下标是 0 ，所以返回 0。 

**示例 2： **

输入：haystack = "leetcode", needle = "leeto" 

输出：-1 

解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。 

**提示： **

1 <= haystack.length, needle.length <= 104 

haystack 和 needle 仅由小写英文字符组成

### **实现代码**
```plain
public class KMP {
    
    // 计算 needle 的前缀函数
    private static int[] computePrefixFunction(String needle) {
        int m = needle.length();
        int[] prefixFunction = new int[m];
        
        // j 是前缀的长度
        int j = 0;
        
        // 从 needle 的第二个字符开始计算前缀函数
        for (int i = 1; i < m; i++) {
            // 回退 j，直到找到一个合适的前缀
            while (j > 0 && needle.charAt(i) != needle.charAt(j)) {
                j = prefixFunction[j - 1];
            }
            // 如果字符匹配，扩展前缀长度
            if (needle.charAt(i) == needle.charAt(j)) {
                j++;
            }
            prefixFunction[i] = j;  // 存储前缀函数值
        }
        
        return prefixFunction;
    }
    
    // 使用 KMP 算法在 haystack 中查找 needle
    public static int strStr(String haystack, String needle) {
        if (needle.isEmpty()) {
            return 0;  // 如果 needle 是空字符串，返回 0
        }
        
        int n = haystack.length();
        int m = needle.length();
        
        // 如果 needle 长度大于 haystack，肯定没有匹配
        if (m > n) {
            return -1;
        }
        
        // 计算 needle 的前缀函数
        int[] prefixFunction = computePrefixFunction(needle);
        
        int i = 0;  // haystack 的指针
        int j = 0;  // needle 的指针
        
        // 开始匹配
        while (i < n) {
            // 如果当前字符匹配，两个指针都向后移动
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
                
                // 如果 j 达到 needle 的长度，说明匹配成功，返回匹配的起始位置
                if (j == m) {
                    return i - j;
                }
            } else {
                // 如果不匹配，根据前缀函数决定是否回退 needle 指针
                if (j > 0) {
                    j = prefixFunction[j - 1];
                } else {
                    // 如果 j == 0，则 haystack 指针向后移动
                    i++;
                }
            }
        }
        
        // 如果没有找到匹配项，返回 -1
        return -1;
    }
    
    public static void main(String[] args) {
        String haystack1 = "sadbutsad";
        String needle1 = "sad";
        System.out.println(strStr(haystack1, needle1));  // 输出: 0

        String haystack2 = "leetcode";
        String needle2 = "leeto";
        System.out.println(strStr(haystack2, needle2));  // 输出: -1
    }
}
```

上面的复杂度是O（n+m）, haystack 的长度为 n，needle 的长度为 m。

## 分析
暴力解法的话是下面这样：

```plain
public class ViolentSolution {
    
    // 暴力解法实现
    public static int strStr(String haystack, String needle) {
        // 如果 needle 是空字符串，返回 0
        if (needle.isEmpty()) {
            return 0;
        }
        
        int n = haystack.length();
        int m = needle.length();
        
        // 如果 needle 的长度大于 haystack 的长度，不可能找到匹配
        if (m > n) {
            return -1;
        }
        
        // 遍历 haystack
        for (int i = 0; i <= n - m; i++) {
            // 从当前 i 位置开始，逐个字符比较
            int j = 0;
            while (j < m && haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }
            
            // 如果 j 达到 needle 的长度，表示完全匹配
            if (j == m) {
                return i; // 返回开始进行匹配的位置就是最后的结果
            }
        }
        
        // 如果遍历完所有可能的起始位置，都没有匹配，返回 -1
        return -1;
    }
    
    public static void main(String[] args) {
        String haystack1 = "sadbutsad";
        String needle1 = "sad";
        System.out.println(strStr(haystack1, needle1));  // 输出: 0

        String haystack2 = "leetcode";
        String needle2 = "leeto";
        System.out.println(strStr(haystack2, needle2));  // 输出: -1
    }
}
```

**思路**

1. 遍历 haystack：我们从 haystack 字符串的每个位置 i 开始，尝试将 needle 的第一个字符与 haystack[i] 比较。
2. 逐个字符比较：如果 haystack[i] 与 needle[0] 相同，那么继续比较后续的字符，直到 needle 中的所有字符都匹配，或者发现不匹配。
3. 匹配成功：如果所有字符都匹配成功，则返回 i，即 needle 在 haystack 中首次匹配的位置。
4. 匹配失败：如果 needle 不能完全匹配 haystack[i..i+m-1]，则继续向后移动 haystack 的指针，进行下一个位置的比较。
5. 提前结束：如果 needle 的长度大于 haystack 的长度，则直接返回 -1，因为不可能找到匹配项。

**时间复杂度**

最坏情况下，我们需要检查每个位置的所有字符。假设 haystack 的长度为 n，needle 的长度为 m，则最坏情况下的时间复杂度为 O(n * m)。

在传统的暴力匹配算法中，我们通常会在每次字符匹配失败时，将 haystack 的指针往后移一步，然后继续从needle头部重新开始比较。假设在某个位置发生了不匹配，如果我们从needle第一个字符开始重新匹配，就会重复比较一些已经验证过的字符。

我们可不可以避免重复比较已经匹配的部分，来提高字符串匹配的效率呢？这时候就想到时候前缀和，但是这里不是使用前缀和，而是前缀函数。

**前缀是指不包含最后一个字符的所有以第一个字符开头的连续子串。**

**后缀是指不包含第一个字符的所有以最后一个字符结尾的连续子串。**

正确理解什么是前缀什么是后缀很重要!

使用前缀函数，我们做到haystack 指针不需要回退，needle 指针根据前缀函数决定回退到哪个位置呢。

### 计算前缀函数
前缀函数 pi[i] 的值表示 needle 中以 needle[i] 结尾的字符串中，最长的相同前缀和后缀的长度。例如：

+ 对于字符串 ABCAB，前缀函数是 [0, 0, 0, 1, 2]。这意味着：
    - needle[0] 没有前缀和后缀的匹配。
    - needle[1] 也没有前缀和后缀的匹配。
    - needle[2] 也没有。
    - 对于 needle[3]，我们知道它有一个长度为 1 的匹配（即前缀和后缀是 A）。
    - 对于 needle[4]，我们知道它有一个长度为 2 的匹配（即前缀和后缀是 AB）。

这个信息帮助我们在匹配失败时，不需要回到 needle 的起始位置，而是直接跳到一个合适的位置继续匹配，从而避免了对已经匹配的部分重复计算。

### 利用前缀函数匹配字符串
```plain
public static int strStr(String haystack, String needle) {
    if (needle.isEmpty()) {
        return 0;  // 如果 needle 是空字符串，返回 0
    }

    int n = haystack.length();
    int m = needle.length();

    // 如果 needle 长度大于 haystack，肯定没有匹配
    if (m > n) {
        return -1;
    }

    // 计算 needle 的前缀函数
    int[] prefixFunction = computePrefixFunction(needle);

    int i = 0;  // haystack 的指针
    int j = 0;  // needle 的指针

    // 开始匹配
    while (i < n) {
        // 如果当前字符匹配，两个指针都向后移动
        if (haystack.charAt(i) == needle.charAt(j)) {
            i++;
            j++;

            // 如果 j 达到 needle 的长度，说明匹配成功，返回匹配的起始位置
            if (j == m) {
                return i - j;
            }
        } else {
            // 如果不匹配，根据前缀函数决定是否回退 needle 指针
            if (j > 0) {
                j = prefixFunction[j - 1];
            } else {
                // 如果 j == 0，则 haystack 指针向后移动
                i++;
            }
        }
    }

    // 如果没有找到匹配项，返回 -1
    return -1;
}
```

为什么可以这样回滚呢？这个比较难以用语言表达，

**但是模拟一下你就懂了（一定要模拟或者去网上找一下动图！）**

案例：

+ `needle = "ababc"`
+ `haystack = "abacababcab"`

前面计算过前缀和函数，如下：

| **<font style="color:rgb(0, 0, 0);">索引 i</font>** | **<font style="color:rgb(0, 0, 0);">子串 needle[0..i]</font>** | **<font style="color:rgb(0, 0, 0);">前缀函数 prefix[i]</font>** |
| --- | --- | --- |
| <font style="color:rgb(0, 0, 0);">0</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">0</font> |
| <font style="color:rgb(0, 0, 0);">1</font> | <font style="color:rgb(0, 0, 0);">ab</font> | <font style="color:rgb(0, 0, 0);">0</font> |
| <font style="color:rgb(0, 0, 0);">2</font> | <font style="color:rgb(0, 0, 0);">aba</font> | <font style="color:rgb(0, 0, 0);">1</font> |
| <font style="color:rgb(0, 0, 0);">3</font> | <font style="color:rgb(0, 0, 0);">abab</font> | <font style="color:rgb(0, 0, 0);">2</font> |
| <font style="color:rgb(0, 0, 0);">4</font> | <font style="color:rgb(0, 0, 0);">ababc</font> | <font style="color:rgb(0, 0, 0);">0</font> |


| **<font style="color:rgb(0, 0, 0);">步骤</font>** | **<font style="color:rgb(0, 0, 0);">i (haystack)</font>** | **<font style="color:rgb(0, 0, 0);">j (needle)</font>** | **<font style="color:rgb(0, 0, 0);">haystack[i]</font>** | **<font style="color:rgb(0, 0, 0);">needle[j]</font>** | **<font style="color:rgb(0, 0, 0);">匹配状态</font>** | **<font style="color:rgb(0, 0, 0);">备注</font>** |
| --- | --- | --- | --- | --- | --- | --- |
| <font style="color:rgb(0, 0, 0);">1</font> | <font style="color:rgb(0, 0, 0);">0</font> | <font style="color:rgb(0, 0, 0);">0</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">2</font> | <font style="color:rgb(0, 0, 0);">1</font> | <font style="color:rgb(0, 0, 0);">1</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">3</font> | <font style="color:rgb(0, 0, 0);">2</font> | <font style="color:rgb(0, 0, 0);">2</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">4</font> | <font style="color:rgb(0, 0, 0);">3</font> | <font style="color:rgb(0, 0, 0);">3</font> | <font style="color:rgb(0, 0, 0);">c</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">不匹配</font> | <font style="color:rgb(0, 0, 0);">使用前缀函数跳跃，j = prefix[2] = 1</font> |
| <font style="color:rgb(0, 0, 0);">5</font> | <font style="color:rgb(0, 0, 0);">3</font> | <font style="color:rgb(0, 0, 0);">1</font> | <font style="color:rgb(0, 0, 0);">c</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">不匹配</font> | <font style="color:rgb(0, 0, 0);">使用前缀函数跳跃，j = prefix[1] = 0</font> |
| <font style="color:rgb(0, 0, 0);">6</font> | <font style="color:rgb(0, 0, 0);">3</font> | <font style="color:rgb(0, 0, 0);">0</font> | <font style="color:rgb(0, 0, 0);">c</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">不匹配</font> | <font style="color:rgb(0, 0, 0);">使用前缀函数跳跃，j = prefix[0] = 0</font> |
| <font style="color:rgb(0, 0, 0);">7</font> | <font style="color:rgb(0, 0, 0);">4</font> | <font style="color:rgb(0, 0, 0);">0</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">8</font> | <font style="color:rgb(0, 0, 0);">5</font> | <font style="color:rgb(0, 0, 0);">1</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">9</font> | <font style="color:rgb(0, 0, 0);">6</font> | <font style="color:rgb(0, 0, 0);">2</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">10</font> | <font style="color:rgb(0, 0, 0);">7</font> | <font style="color:rgb(0, 0, 0);">3</font> | <font style="color:rgb(0, 0, 0);">c</font> | <font style="color:rgb(0, 0, 0);">c</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">11</font> | <font style="color:rgb(0, 0, 0);">8</font> | <font style="color:rgb(0, 0, 0);">4</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">a</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">i++, j++</font> |
| <font style="color:rgb(0, 0, 0);">12</font> | <font style="color:rgb(0, 0, 0);">9</font> | <font style="color:rgb(0, 0, 0);">5</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">b</font> | <font style="color:rgb(0, 0, 0);">匹配</font> | <font style="color:rgb(0, 0, 0);">匹配完成，从第 9 个字符开始，返回索引 i - m 即 0</font> |


**简单说我们每次i要遍历一个一个往下走，因为我们怕当前字符前面还有相匹配的一段，万一错过了怎么办？**

**那怎么做到头也不回的往下走呢？那你要确定现在的i字符之前有没有一段与匹配字符串的部分前缀匹配的字符串，匹配的是什么、**

**怎么判断呢？前缀函数代表了后面字符在前面有没有前缀相对应，通过这个可以很容易找到匹配到对应的前缀字符串，回滚到这部分前缀字符串之后继续匹配。**


**！！！本文适合有c和c++基础的，通过比较c++和java的不同，快速入门java。！！！**  
这篇文章主要是介绍和c++[不同的](https://so.csdn.net/so/search?q=%E4%B8%8D%E5%90%8C%E7%9A%84&spm=1001.2101.3001.7020)地方，没说的知识点按照c++写就行了。

## 零.整体的结构
Java是[面向对象](https://so.csdn.net/so/search?q=%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1&spm=1001.2101.3001.7020)的程序。首先对于Java来说一个文件就是一个类,而且类名必须和文件名一致，比如Main类，则文件名要叫做Main.java，而Person类，文件名要叫做Person.java。

它和c++首先映入眼帘的不同就是不可以在类外定义函数，它所有的函数（包括主函数都要定义在类里面）。

### 1.主函数
比如在一般只有一个文件的话c++结构是这样的：

```plain
#include<iostream>
using namespace std;
int main(){
	//代码
    return 0;
}
```

但是Java的话main函数也要放在类里面：

```plain
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        //代码
    }
}

```

**注：public static void main(String[] args) {}是主函数（或者叫程序入口）的唯一格式，不能写成其他形式。**类的话命名随意。

### **2.函数/方法**
【1】在类外定义方法

c++中允许在类外定义方法，比如

```plain
#include<iostream>
using namespace std;
void print(){
	cout<<"666";
}
int main(){
	print();
	return 0;
}
```

在Java中应该这么写：

```plain
import java.util.Scanner;
public class Main {
    public static void speak(){
        //下面这句话是Java的控制台输出语句，相当于printf或者cout
        System.out.println("666");
    }
    public static void main(String[] args) {
        speak();
    }
}
```

**注意因为main函数为静态方法，学过c++都知道，静态方法属于类中的所有实例所共有，并且只能调用静态的变量和方法，所以speak函数必须是static才能被main函数调用**，至于是要public还是private看你自己。

【2】在类内定义方法

当然c++也可以在类内定义方法：

```plain
#include<iostream>
using namespace std;
class Person{
	public:
		void speak(){
			cout<<"666";
		}
};
int main(){
	Person person;
	person.speak();
	return 0;
}
```

改写成Java是这样的：

```plain
import java.util.Scanner;
public class Main {
    static class Person{
        public void speak(){
            System.out.println("666");
        }
    };
    public static void main(String[] args) {
        Person person=new Person();
        person.speak();
    }
}
```

因为Java中一个文件只能是一个类，所以Person类只能作为内部类存在于Main中，所以Person前面也要加上static关键字才能被同为静态方法的main函数调用。

### 3.分文件编写
当然Java也可以像c++那样分文件编写（因为下面是定义在同一个包内，所以不用引包）  
我们可以重新创建一个文件Person.java来定义Person类。

```plain
public class Person{
    public void speak(){
        System.out.println("666");
    }
}

```

```plain

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Person person=new Person();
        person.speak();
    }
}
```

### 4.包的概念
【1】包是什么

c++中没有包的概念。那么包是什么呢？

当程序足够大的时候，我们就要学会去管理我们代码。写程序的时候代码管理很重要。在c++中，比如当零散的代码足够多时，我们就要用函数去分类包装这些代码，将一部分代码抽象成这个函数，另一部分代码抽象成另一个函数。当函数足够多时，我们要将方法分类，进一步抽象，一部分函数属于这个类，一部分函数当成那个类的方法，用类包装。

但是当类足够多，我们就要进一步分类，一部分类放在这个命名空间，一部分类放在那个命名空间。

包说白了就是文件夹，作用就类似于命名空间，用来对各个类进行分类管理，一部分包放在这个文件夹，另一部分包放在那个文件夹。

【2】案例：新建一个Util包，将Person类放在Util中

```plain

package util;
public class Person{
    public void speak(){
        System.out.println("666");
    }
}
```

```plain

import util.Person;
public class Main {
    public static void main(String[] args) {
        Person person=new Person();
        person.speak();
    }
}
```

【3】包名命名规则  
上面只是个示例：比较正式的项目要采用以下的命名规则

公司域名反写+包的名字（要体现作用），需要全部英文小写，见名知意   
例：com.flyingpig.entity     com.flyingpig.util【其中com.flyingpig是域名】  
简单说就是建立一个com文件夹，里面再建立一个flyingpig文件夹，然后里面就可以建立entity文件夹来存放实体类，建立util文件夹来存放工具类

在com.flyingpig.entity包下的Student类表示为com.flyingpig.entity.Student ，这个叫做全类名和全限定名。

【3】我们看到Person类上面加了个package，而Main类上面import。  
这是因为类放在包里要package。  
而引用放在别的包里的类需要引包。具体的引包规则如下：  
（1）使用同一个包中的类时，不需要导包  
（2）使用于java.lang包中的类时，不需要导包  
（3）其他情况都需要导包  
（3）如果同时使用两个包中的同名类，需要用同类名.

## 一.注释（和c一样）
单行注释：//  
多行注释：/*   */  
文档注释：/**    **/

## 二.字面量和变量类型
### 1.字面量
字面量--整型，小数，字符串，字符，布尔类型，空类型（null）

### **2.变量**
**变量--四类八种(或者说三类八种)**

**6 种数字类型：  
****4 种整数型：**`**byte**`**、**`**short**`**、**`**int**`**、**`**long**`**  
****2 种浮点型：**`**float**`**、**`**double**`**  
****1 种字符类型：**`**char**`**  
****1 种布尔型：**`**boolean**`

> 这 8 种基本数据类型的默认值以及所占空间的大小如下：
>
> ![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1734012424093-646eb7af-d2d1-421f-a7ee-127314fb6472.png)
>
> 对于 `boolean`，官方文档未明确定义，它依赖于 JVM 厂商的具体实现。逻辑上理解是占用 1 位，但是实际中会考虑计算机高效存储因素。
>

和c++基本一致，不一样的是多了像byte之类类型，少了像long double之类的类型。

**注意：  
****1.Java 里使用 **`**long**`** 类型的数据一定要在数值后面加上 L，否则将作为整型解析。  
**`**2.char a = 'h'**`**char :单引号，**`**String a = "hello"**`** :双引号。**

### 3.包装类型
#### 【1】包装类型介绍
这八种基本类型都有对应的包装类分别为：`Byte`、`Short`、`Integer`、`Long`、`Float`、`Double`、`Character`、`Boolean` 。

区别嘛，简单说基本类型是变量，而包装类型是对象。

具体区别嘛也就是变量与对象的区别：

![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1734012424203-76a7a611-ce05-4005-b0a6-6e15091616cf.png)

#### 【2】包装类型的缓存机制
Java 基本数据类型的包装类型的大部分都用到了缓存机制来提升[性能](https://marketing.csdn.net/p/3127db09a98e0723b83b2914d9256174?pId=2782&utm_source=glcblog&spm=1001.2101.3001.7020)。

`Byte`,`Short`,`Integer`,`Long` 这 4 种包装类默认创建了数值 **[-128，127]** 的相应类型的缓存数据，`Character` 创建了数值在 **[0,127]** 范围的缓存数据，`Boolean` 直接返回 `True` or `False`。

**Integer 缓存源码：**

```plain
public static Integer valueOf(int i) {
    if (i >= IntegerCache.low && i <= IntegerCache.high)
        return IntegerCache.cache[i + (-IntegerCache.low)];
    return new Integer(i);
}



private static class IntegerCache {

    static final int low = -128;
    static final int high;
    
    static {
        // high value may be configured by property
        int h = 127;
    }
}
```

如果超出对应范围仍然会去创建新的对象，缓存的范围区间的大小只是在性能和资源之间的权衡。

两种浮点数类型的包装类 `Float`,`Double` 并没有实现缓存机制。

下面我们来看一个问题：下面的代码的输出结果是 `true` 还是 `false` 呢？

```plain
Integer i1 = 40;

Integer i2 = new Integer(40);

System.out.println(i1==i2);
```

`Integer i1=40` 这一行代码会发生装箱，也就是说这行代码等价于 `Integer i1=Integer.valueOf(40)` 。因此，`i1` 直接使用的是缓存中的对象。而`Integer i2 = new Integer(40)` 会直接创建新的对象。

简单说valueOf方法或者直接赋值（本质上也是调用value of）才会使用缓存，new对象是直接创建对象，不管值是什么。因此，答案是 `false` 。你答对了吗？

记住：**所有整型包装类对象之间值的比较，全部使用 equals 方法比较**。

![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1734012424268-776ad8d0-b307-4681-9bf6-6ec611b54026.png)

#### 【3】自动装箱与拆箱
**装箱**：将基本类型用它们对应的引用类型包装起来；  
**拆箱**：将包装类型转换为基本数据类型；

```plain
Integer i = 10;  //装箱

int n = i;   //拆箱
```

从字节码中，我们发现装箱其实就是调用了 包装类的`valueOf()`方法，拆箱其实就是调用了 `xxxValue()`方法。

因此，

+ `Integer i = 10` 等价于 `Integer i = Integer.valueOf(10)`
+ `int n = i` 等价于 `int n = i.intValue()`;

注意：**如果频繁拆装箱的话，也会严重影响系统的性能。我们应该尽量避免不必要的拆装箱操作。**

```plain
private static long sum() {
    // 应该使用 long 而不是 Long
    Long sum = 0L;

    for (long i = 0; i <= Integer.MAX_VALUE; i++)
        sum += i;
    return sum;
}
```

#### 【4】BigDecimal和BigInteger
c++做题经常有数据溢出的问题，如果要无限大的数经常得自己实现类，而java中已经给了我们很好用的内置类。

##### （1）BigDecimal
浮点数运算精度丢失代码演示：

```plain
float a = 2.0f - 1.9f;

float b = 1.8f - 1.7f;

System.out.println(a);// 0.100000024

System.out.println(b);// 0.099999905

System.out.println(a == b);// false
```

为什么会出现这个问题呢？

这个和计算机保存浮点数的机制有很大关系。我们知道计算机是二进制的，而且计算机在表示一个数字时，宽度是有限的，无限循环的小数存储在计算机时，只能被截断，所以就会导致小数精度发生损失的情况。这也就是解释了为什么浮点数没有办法用二进制精确表示。

就比如说十进制下的 0.2 就没办法精确转换成二进制小数：

```plain
// 0.2 转换为二进制数的过程为，不断乘以 2，直到不存在小数为止，

// 在这个计算过程中，得到的整数部分从上到下排列就是二进制的结果。

0.2 * 2 = 0.4 -> 0
0.4 * 2 = 0.8 -> 0
0.8 * 2 = 1.6 -> 1
0.6 * 2 = 1.2 -> 1
0.2 * 2 = 0.4 -> 0（发生循环）
...
```

`BigDecimal` 可以实现对浮点数的运算，不会造成精度丢失。通常情况下，大部分需要浮点数精确运算结果的[业务场景](https://edu.csdn.net/cloud/pm_summit?utm_source=blogglc&spm=1001.2101.3001.7020)（比如涉及到钱的场景）都是通过 `BigDecimal` 来做的。

```plain
BigDecimal a = new BigDecimal("1.0");

BigDecimal b = new BigDecimal("0.9");

BigDecimal c = new BigDecimal("0.8");

BigDecimal x = a.subtract(b);

BigDecimal y = b.subtract(c);

System.out.println(x); /* 0.1 */

System.out.println(y); /* 0.1 */

System.out.println(Objects.equals(x, y)); /* true */
```

关于 `BigDecimal` 的详细介绍，可以看看javaguide的这篇文章：[BigDecimal 详解open in new window](https://javaguide.cn/java/basis/bigdecimal.html)。

##### （2）BigInteger
基本数值类型都有一个表达范围，如果超过这个范围就会有数值溢出的风险。

在 Java 中，64 位 long 整型是最大的整数类型。

```plain
long l = Long.MAX_VALUE;



System.out.println(l + 1); // -9223372036854775808



System.out.println(l + 1 == Long.MIN_VALUE); // true
```

`BigInteger` 内部使用 `int[]` 数组来存储任意大小的整形数据。

相对于常规整数类型的运算来说，`BigInteger` 运算的效率会相对较低。

### 4.补充
**默认值**：从变量是否有默认值来看，成员变量如果没有被赋初始值，则会自动以类型的默认值而赋值（一种情况例外:被 `final` 修饰的成员变量也必须显式地赋值），而局部变量则不会自动赋值。

而c中不管怎么样都有默认值。

```plain
为什么成员变量有默认值？先不考虑变量类型，如果没有默认值会怎样？
变量存储的是内存地址对应的任意随机值，程序读取该值运行会出现意外。
默认值有两种设置方式：手动和自动，
根据第一点，没有手动赋值一定要自动赋值。
成员变量在运行时可借助反射等方法手动赋值，而局部变量不行。
对于编译器（javac）来说，局部变量没赋值很好判断，可以直接报错。
而成员变量可能是运行时赋值，无法判断，误报“没默认值”又会影响用户体验，所以采用自动赋默认值。
```

## 三.输入输出
输出：System.out.println方法

```plain
//输出字符串字面量
System.out.println("我可以输出任何变量哦");
//输出整型字面量
System.out.println(666);
//输出整型变量
int a=0;
System.out.println(a);
//注意long类型的数据值后面一般需要加个L或l作为后缀。
long n=9999999999L;
System.out.println(n);
//注意float类型的数据值后面一般需要加个F作为后缀。
float f=10.1F;
System.out.println(f);
```

输入：用Scanner类

```plain
//建立一个调用Scanner的有参构造建立一个Scanner对象
Scanner scanner=new Scanner(System.in);
///调用其中的方法进行输入，其中nextInt方法是用来输入整数的
int number=sc.nextInt();
```

## 四.关系运算符
和c++几乎一样，只有些许不同，这里列举几个不同点。  
（1）%也能用于小数运算  
（2）bool类型不能用于算数计算  
（3）java中对的数据类型转换检查严格

下面的代码在c++中是可以的，但在java中就会报错。

```plain
int a=1.1;
```

## 五.分支和循环语句
写法与c++一模一样。

但是Java还提供了增强for和增强Switch，可以简化书写。

### 1.增强for
#### 【1】优点
  
Java 中的增强 for 循环（也称为 for-each 循环）相比于传统的 for 循环  
优点：  
1. 简洁，不需要索引  
2. 安全性：防止越界（没有使用索引）和修改集合中的元素。  
缺点：  
1. 无法获取当前元素的索引：增强 for 循环没有提供内置的索引访问机制，如果需要获取当前元素的索引，仍然需要使用传统 for 循环。  
2. 无法修改集合中的元素：增强 for 循环只能读取集合中的元素，无法修改元素的值或删除元素。

需要注意的是，增强for并不会提高程序的运行效率。在底层实现上，增强 for 循环其实还是通过迭代器或索引来遍历集合或数组的。

#### 【2】增强 for 循环的语法
```plain
for (元素类型 元素变量 : 遍历对象) {
    // 循环体
}
```

其中，元素类型表示遍历对象中元素的类型，元素变量是用于接收每个元素值的变量名，遍历对象可以是数组或实现了 Iterable 接口的集合类（如 List、Set 等）。

下面是几个示例：

1. 遍历数组：

```plain
int[] numbers = {1, 2, 3, 4, 5};
for (int number : numbers) {
    System.out.println(number);
}
```

2. 遍历集合：

```plain
List<String> fruits = Arrays.asList("apple", "banana", "orange");
for (String fruit : fruits) {
    System.out.println(fruit);
}
```

3. 遍历字符串：

```plain
String message = "Hello";

for (char ch : message.toCharArray()) {
    System.out.println(ch);
}
```

在以上示例中，每次迭代时，元素变量（如 number、fruit、ch）都会被赋值为遍历对象中的一个元素值，然后执行循环体内的代码。循环将按顺序遍历遍历对象中的每个元素，直到遍历完成。

### 2.增强switch
原来：

```plain
int dayOfWeek = 3;
String dayName;
switch (dayOfWeek) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;
    case 7:
        dayName = "Sunday";
        break;
    default:
        dayName = "Invalid day";
        break;
}
System.out.println("The day is: " + dayName);
```

简化：

```plain
int dayOfWeek = 3;
String dayName=new String();
switch (dayOfWeek) {
    case 1 -> String dayName ="Monday";
    case 2 -> String dayName ="Tuesday";
    case 3 -> String dayName ="Wednesday";
    case 4 -> String dayName ="Thursday";
    case 5 -> String dayName ="Friday";
    case 6 -> String dayName ="Saturday";
    case 7 -> String dayName ="Sunday";
    default -> String dayName ="Invalid day";
};
System.out.println("The day is: " + dayName);
```

还可以进一步化简，将变量提取出来

```plain
int dayOfWeek = 3;

String dayName = switch (dayOfWeek) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    case 3 -> "Wednesday";
    case 4 -> "Thursday";
    case 5 -> "Friday";
    case 6 -> "Saturday";
    case 7 -> "Sunday";
    default -> "Invalid day";
};

System.out.println("The day is: " + dayName);
```

## 六.引用数据类型
**基本数据类型 【**上面讲的四类八种**】**

数据值是存储在自己的空间中。  
特点：赋值给其他变量，也是赋的是真实的值。  
![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1734012424210-c71acd7c-abb0-4352-ad8b-3971b071d1b8.png)

**引用数据类型**--就是java中表示对象的数据类型。

数据值是存储在其他空间中，自己空间中存储的是地址值。类似于c++的指针。同样的储存变量，同样的可以改变地址。  
特点：赋值给其他变量，赋的地址值。

![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1734012424273-12e5c070-3434-40e8-b907-b7176ac23e81.png)  
【1】因为java和c++不同的是，java创建对象都是在堆区new出来的，所以都使用引用数据类型来操作对象。

例如：  
在c++中可以

```plain
Person person;
```

但是创建的话java中必须用new来创建对象：

```plain
Person person=new Person();
```

这里的Person与c++的Person不一样，它代表引用，就像下面c++的Person*。

```plain
Person* person=new Person();
```

【2】调用方法的时候java自动解引用，下面的第一个是java，第二个是c++:

```plain
person.speak();
```

```plain
*person.speak();
```

【3】赋值的时候java和c++一样也是直接赋值地址：

```plain
person=person1;
```

【4】Java中的引用相比于c++更加方便安全，因为它不用手动释放空间。

**总结来说java的引用功能上类似于安全化的c++指针，写法上的话相当于c++的引用。**

**注：功能上不同于c++的引用，因为c++的引用第一次赋值后不可以修改指向的变量，而Java可以。****Java中的链表就是通过引用数据类型实现的，因为其实Java中引用的功能和C++指针差不多，只不过有自动回收更安全。**

## 七.数组
在java中，数组是一种对象。  
创建数组

```plain
public static void main(String[] args) {
    
    //int数组的类型名叫做int[],所以一般是这样写的
    int[] array1=new int[3];

    //但是如c++之类的语言一般习惯用int array2[]这种格式，所以也可以这么写
    int array2[]=new int[3];

    //当然了，赋值的话还可以用数组专门用于赋值的初始化列表
    int[] array3=new int[]{11,22,33};

    //也可以简化写成
    int[] array4={11,22};
}
```

使用的话和c几乎一样，但还是有不同。  
（1）因为是变量，所以java里面的数组有属性size可以来获取数组的长度，如  
array3.length。这个比较经常在循环中用到。  
（2）还有数组越界，在java中不会纵容数组越界，一越界会抛出异常。

## 九.方法
### 1.与c++写法比较
和c，c++差不多，就像第零条所讲的，最大的不同就是所有方法，包括main方法都得在类里面定义。  
还有值得一提的是java方法里面最终的结果要确定（除了void），例如c++中可以这样：

```plain
#include<iostream>
using namespace std;
bool judge(int num){
	if(num>1)
		return 0;
} 
int main(){
	bool result=judge(1);
	cout<<result;
}
```

大于1返回0，可以不指定小于等于1，当num小于或等于1时，它会返回默认值。

但是java这样的话会报错缺少return语句

```plain
static boolean judge(int num){
    if(num>1)
        return false;
}
```

而需要这样写：

```plain
static boolean judge(int num){
      if(num>1)
          return false;
      else 
          return true;
  }
```

### 2.可变长参数
从 Java5 开始，Java 支持定义可变长参数，所谓可变长参数就是允许在调用方法时传入不定长度的参数。就比如下面的这个 `printVariable` 方法就可以接受 0 个或者多个参数。

```plain
public static void method1(String... args) {
   //......
}
```

另外，可变参数只能作为函数的最后一个参数，但其前面可以有也可以没有任何其他参数。

```plain
public static void method2(String arg1, String... args) {
   //......
}
```

**遇到方法重载的情况怎么办呢？会优先匹配固定参数还是可变参数的方法呢？**

答案是会优先匹配固定参数的方法，因为固定参数的方法匹配度更高。

另外，Java 的可变参数编译后实际会被转换成一个数组，我们看编译后生成的 `class`文件就可以看出来了。

## 其他
### final关键字--类似于c++的const
语法：public final void 函数名

作用：简单说就是不可改变。  
作用于变量，变量只能被赋值一次。  
作用于方法，方法不能被重写。  
作用于类，不能被继承。

静态变量会被 `final` 关键字修饰成为常量。


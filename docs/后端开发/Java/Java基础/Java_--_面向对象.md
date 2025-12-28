### 十. 封装
#### 1. 访问权限不用加
在 c++ 中是访问权限： 属性 / 行为：

```plain
class Person{
    public:
        void speak(){
            cout<<"666";
        }
};
```

在 Java 中是访问权限 属性 / 行为：

```plain
class Person{
    public void speak(){
        cout<<"666";
    }
};
```

#### 2. 和 c++ 一样类中对象可以没有初始化
为什么要刻意强调这一点呢？因为与 c++ [不同的](https://so.csdn.net/so/search?q=%E4%B8%8D%E5%90%8C%E7%9A%84&spm=1001.2101.3001.7020)是 java 方法中建立变量没有初始化会报错。但是类中对象没有初始化会像 c++ 一样分配初始值。  
整型的初始值是 0。浮点型是 0.0。布尔型是 false。引用类型是 null。

#### 3. 对象的创建
前面讲过 java 是通过 new 来创建对象的。

```plain
//无参构造
Student student1=new Student();
//有参构造
Student student2=new Student("张三",19);
```

补充：  
Java 中没有析构函数。  
set 和 get 方法可以通过 IDEA 的快捷键 alt+insert 进行快速生成。当然后期会使用 lombok 来简化书写。

#### 4.this 关键字
c++ 中是这么写的 this->  
java 中是这么写的 this.

#### 5. 静态成员
c++ 是这么调用的 Person::m_A  
Java 是这么调用的 Person.m_A

#### 6. 类的分类
【1】Java 中专门用来**描述一类事物**的类就叫做 **Javabean 类**，简单说就是里面没有 main 方法。  
**【2】里面有 main 方法的类叫做测试类**，因为有 main 方法，所以可以运行，主要用来测试本类和其他类的方法书写是否正确。  
**【3】专门提供方法让别人使用的就是工具类。最大的特点就是变量和方法都是静态的。**

**注：我们一般在类中添加 main 方法来测试该类的书写是否正确。**

例如下面这个代码

```plain
public class JwtUtil {
    //有效期为
    public static final Long JWT_TTL =15*24* 60 * 60 *1000L;// 60 * 60 *1000  一个小时
    //设置秘钥明文
    public static final String JWT_KEY = "Zmx5aW5ncGln";//flyingpig
 
    public static String getUUID(){
        String token = UUID.randomUUID().toString().replaceAll("-", "");
        return token;
    }
 
    /**
     * 生成jtw
     * @param subject token中要存放的数据（json格式）
     * @return
     */
    public static String createJWT(String subject) {
        JwtBuilder builder = getJwtBuilder(subject, null, getUUID());// 设置过期时间
        return builder.compact();
    }
 
    /**
     * 生成jtw
     * @param subject token中要存放的数据（json格式）
     * @param ttlMillis token超时时间
     * @return
     */
    public static String createJWT(String subject, Long ttlMillis) {
        JwtBuilder builder = getJwtBuilder(subject, ttlMillis, getUUID());// 设置过期时间
        return builder.compact();
    }
 
    private static JwtBuilder getJwtBuilder(String subject, Long ttlMillis, String uuid) {
        SignatureAlgorithm signatureAlgorithm = SignatureAlgorithm.HS256;
        SecretKey secretKey = generalKey();
        long nowMillis = System.currentTimeMillis();
        Date now = new Date(nowMillis);
        if(ttlMillis==null){
            ttlMillis=JwtUtil.JWT_TTL;
        }
        long expMillis = nowMillis + ttlMillis;
        Date expDate = new Date(expMillis);
        return Jwts.builder()
                .setId(uuid)              //唯一的ID
                .setSubject(subject)   // 主题  可以是JSON数据
                .setIssuer("flyingpig")     // 签发者
                .setIssuedAt(now)      // 签发时间
                .signWith(signatureAlgorithm, secretKey) //使用HS256对称加密算法签名, 第二个参数为秘钥
                .setExpiration(expDate);
    }
 
    /**
     * 创建token
     * @param id
     * @param subject
     * @param ttlMillis
     * @return
     */
    public static String createJWT(String id, String subject, Long ttlMillis) {
        JwtBuilder builder = getJwtBuilder(subject, ttlMillis, id);// 设置过期时间
        return builder.compact();
    }
 
    public static void main(String[] args) throws Exception {
      String jwtKey = "flyingpig";
        String encodedKey = Base64.getEncoder().encodeToString(jwtKey.getBytes());
        System.out.println(encodedKey);
    }
 
    /**
     * 生成加密后的秘钥 secretKey
     * @return
     */
    public static SecretKey generalKey() {
        byte[] encodedKey = Base64.getDecoder().decode(JwtUtil.JWT_KEY);
        SecretKey key = new SecretKeySpec(encodedKey, 0, encodedKey.length, "AES");
        return key;
    }
    //解析JWT令牌
    public static Claims parseJwt(String jwt) {
        SecretKey secretKey = generalKey();
        return Jwts.parser()
                .setSigningKey(secretKey)
                .parseClaimsJws(jwt)
                .getBody();
    }
}
```

**然后我们就可以直接通过类名. 方法的格式直接对里面的方法为其他类提供服务。**

### **十一. 继承**
【1】语法：

```plain
public class Student extends Person{}

```

【2】Java 中所有的继承都是公有继承，即公有的仍然是公有，私有的还是私有。

【3】子类和父类同名成员

访问子类同名成员 --son.m_A 或者 this.m_A  
访问父类 --super.m_A

c++ 中是类名:: 变量名，而 Java 中用 son 和 this 代表子类，super 代表父类。

【4】Java 中无多继承

【5】方法重写

```plain
    @Override
    public Integer getIdByTeacherName(String teacherName) {
        Integer teacherId=teacherMapper.getIdByName(teacherName);
        return teacherId;
    }
```

与 c++ 一个很大的区别是重写方法前面要加上一个 @Override 注解。什么是注解呢？Override 注解又有什么用呢？

注释是给程序员看的，而注释是给虚拟机和电脑看的。  
@Override 是重写注解，是放在重写后的方法上，如果重写的方法语法错误，就会有红色波浪线。

【6】java 使用 super() 调用父类的构造方法

### 十二. 多态
#### 1. 什么是多态？
多态，顾名思义就是多种形态。  
首先要明确父类或者子类的对象都可以赋值给父类引用。  
而当用父类的引用调用一个方法，会根据当前父类的引用或指针指向什么类型去调用对应的实现，然后执行不同的过程，就类似变换多种形态。  
举个例子，动物类都有叫这个方法，如果将狗类对象赋值给动物类引用，则执行的叫是狗的汪汪叫，如果赋值的是猫类对象，则是猫叫，赋值的是老鼠类对象，则是老鼠叫。  
为什么只说方法，不说变量，因为多态只会对方法起作用。 通过多态，我们可以提高代码的复用性。

#### 2. 多态的实现
多态是通过抽象的父类 + 子类继承实现的（在 c++ 中的关键字是 virtual，在 Java 中是 abstract）

【1】抽象的父类

```plain
//抽象类
public abstract class Animal {
    public void printName(){
        System.out.println("Animal");
    }
    //抽象方法
    public abstract void speak();
}
```

格式为 public abstract class 类名 {}；的类称为抽象类。  
格式为 public abstract 返回值类型 方法名（参数列表）; 的方法成为抽象方法。

注：（1）如果一个类中存在抽象方法，那么该类就必须声明为抽象类。例如上面的 Animal 类，使用 abstract 关键字声明抽象类。抽象类不一定有抽象方法，但有抽象方法一定是抽象类。  
（2）抽象类中定义的抽象方法无实现。

【2】子类继承

子类继承后一定要重写父类抽象类中的所有抽象方法，要不然子类也得定义为抽象类。

重写抽象方法：

```plain
public class Cat extends Animal{
    public void speak() {
        System.out.println("喵喵喵");
    }
}
```

```plain
public class Dog extends Animal{
    public void speak() {
        System.out.println("汪汪汪");
    }
}
```

```plain
public class Person extends Animal{
    public void speak() {
        System.out.println("666");
    }
}
```

除非继续定义为抽象类：

```plain
public abstract class Person extends Animal{
}
```

【3】多态的使用 -- 就是使用子类对象赋值给父类引用，那么调用父类引用的方法就会使用其对应子类的实现。

```plain
public class Main {
    public static void main(String[] args){
        Animal animal=new Dog();
        animal.speak();
        animal=new Cat();
        animal.speak();
        animal=new Person();
        animal.speak();
    }
}
```

![](https://i-blog.csdnimg.cn/blog_migrate/aa70cadd093e9edbc137f03d4b4df1c2.png)

### 十三. 接口
接口是什么，就是一种特殊的抽象类，类中所有的方法都是抽象方法。  
关键字是 interface 和 implements。

#### 1. 接口的实现
【1】定义接口: 就是将 abstract class 换成 interface

```plain
public interface Animal {
    void speak();
}
```

【2】继承接口：就是将 extend 换成 implements

```plain
public class Cat implements Animal{
    public void speak() {
        System.out.println("喵喵喵");
    }
}
```

```plain
public class Dog implements Animal{
    public void speak() {
        System.out.println("汪汪汪");
    }
}
```

```plain
public class Person implements Animal{
    public void speak() {
        System.out.println("666");
    }
}
```

【3】使用和多态一样

```plain
​public class Main {
    public static void main(String[] args){
        Animal animal=new Dog();
        animal.speak();
        animal=new Cat();
        animal.speak();
        animal=new Person();
        animal.speak();
    }
}
```

#### 2. 接口的特点
【1】接口支持多继承，一个类可以实现多个接口。  
【2】接口不能实例化，不能 new 对象。  
【3】接口没有构造方法  
【4】接口成员变量的默认修饰符是 public static final  
接口成员方法的默认修饰符是 public abstract  
所以这些修饰符可以省略不写，还有出这些之外的修饰符也不能写。

#### 3. 接口的意义
那么接口有什么特殊意义呢？为什么要把只有抽象函数的抽象类特意的提出来，叫做接口，并刚给它特殊的关键字和定义方法？

接口的意义主要是**定义规范和规则**。接口的特点就是所有继承它的类都要去实现其中的所有抽象方法。  
比如当你是架构师，你不用编写所有的代码，只需要编写接口，那么让其他程序员继承这个接口，他就需要去实现其中的所有方法。  
又比如同一套 api 在不同的环境下有不同的实现，比如 java 操作数据库的 jdbc 的 api，数据库类型有很多，mysql,Oracle 等。  
所以 java 公司它只是规定接口，规定要实现哪些方法和功能，至于具体的实现交给各个数据库公司提供。这就是制定规范。

### 十四. Object 和 String 类
### 1.Object 类
#### 【1】Object 介绍
Object 类是一个特殊的类，是所有类的父类。它主要提供了以下 11 个方法：

```plain
/**
 * native 方法，用于返回当前运行时对象的 Class 对象，使用了 final 关键字修饰，故不允许子类重写。
 */
public final native Class<?> getClass()
/**
 * native 方法，用于返回对象的哈希码，主要使用在哈希表中，比如 JDK 中的HashMap。
 */
public native int hashCode()
/**
 * 用于比较 2 个对象的内存地址是否相等，String 类对该方法进行了重写以用于比较字符串的值是否相等。
 */
public boolean equals(Object obj)
/**
 * native 方法，用于创建并返回当前对象的一份拷贝。
 */
protected native Object clone() throws CloneNotSupportedException
/**
 * 返回类的名字实例的哈希码的 16 进制的字符串。建议 Object 所有的子类都重写这个方法。
 */
public String toString()
/**
 * native 方法，并且不能重写。唤醒一个在此对象监视器上等待的线程(监视器相当于就是锁的概念)。如果有多个线程在等待只会任意唤醒一个。
 */
public final native void notify()
/**
 * native 方法，并且不能重写。跟 notify 一样，唯一的区别就是会唤醒在此对象监视器上等待的所有线程，而不是一个线程。
 */
public final native void notifyAll()
/**
 * native方法，并且不能重写。暂停线程的执行。注意：sleep 方法没有释放锁，而 wait 方法释放了锁 ，timeout 是等待时间。
 */
public final native void wait(long timeout) throws InterruptedException
/**
 * 多了 nanos 参数，这个参数表示额外时间（以纳秒为单位，范围是 0-999999）。 所以超时的时间还需要加上 nanos 纳秒。。
 */
public final void wait(long timeout, int nanos) throws InterruptedException
/**
 * 跟之前的2个wait方法一样，只不过该方法一直等待，没有超时时间这个概念
 */
public final void wait() throws InterruptedException
/**
 * 实例被垃圾回收器回收的时候触发的操作
 */
protected void finalize() throws Throwable { }
```

#### 【2】equals 方法
== 对于基本类型比较的是值，如果是对象比较的是对象的内存地址。

equals 方法没有重写则等效于 equals 方法，有重写经常用于比较两个对象的属性是否相等。  
比如比较两个 String 和包装类型的值是否相等经常使用 equals 方法。

#### 【3】hashCode 方法
hashCode() 的作用是获取哈希码。在 Java 与哈希表相关的容器 HashMap 和 HashSet 底层实现就会调用这个方法。

> 附：为什么重写 equals() 时必须重写 hashCode() 方法？
>
> 因为两个相等的对象的 `hashCode` 值必须是相等。也就是说如果 `equals` 方法判断两个对象是相等的，那这两个对象的 `hashCode` 值也要相等。
>
> 如果重写 `equals()` 时没有重写 `hashCode()` 方法的话就可能会导致 `equals` 方法判断是相等的两个对象，`hashCode` 值却不相等
>

### 2.String、StringBuffer、StringBuilder
#### 【1】StringBuilder 与 StringBuffer 都继承自 AbstractStringBuilder 类。
#### 【2】比较
String 是不可变的，而 StringBuffer 线程有加同步锁，是线程安全的，但是相对性能低一点点。  
而 StringBuilder 是线程不安全的，而性能高一点点。

#### 【3】String 为什么是不可变的?
String 类的定义

```plain
public final class String implements java.io.Serializable, Comparable<String>, CharSequence {
    private final char value[];
  //...
}
```

通过 String 的定义可以看到 String 里的字符数组被 final 和 private 修饰：  

+ 保存字符串的数组是私有的，并且 String 类没有提供 / 暴露修改这个字符串的方法。  
*String 类被 final 修饰导致其不能被继承，进而避免了子类破坏 String 不可变。

> **Java 9 为何要将 String 的底层实现由 char[] 改成了 byte[] ?**  
新版的 String 其实支持两个编码方案：Latin-1 和 UTF-16。如果字符串中包含的汉字没有超过 Latin-1 可表示范围内的字符，那就会使用 Latin-1 作为编码方案。Latin-1 编码方案下，byte 占一个字节 (8 位)，char 占用 2 个字节（16），**byte 相较 char 节省一半的内存空间。**  
**如果字符串中包含的汉字超过 Latin-1 可表示范围内的字符，**`byte`** 和 **`char`** 所占用的空间是一样的。**
>

#### 【4】字符串拼接
字符串的拼接可以使用 + 和 +=，“+”和 “+=” 是专门为 String 类重载过的运算符，也是 Java 中仅有的两个重载过的运算符。  
java8 及以前的字符串拼接 + 底层使用的是 StringBuilder 的 append() 方法实现的，拼接完成之后调用 toString() 得到一个 String 对象 。但是会有重复创建 StringBuilder 对象的缺点，所以 Java8 之前会自己创建 StringBuilder 进行拼接效率比较高。

**不过，使用 “+” 进行字符串拼接会产生大量的临时对象的问题在 JDK9 中得到了解决。**在 JDK9 当中，字符串相加 “+” 改为了用动态方法 makeConcatWithConstants() 来实现，而不是大量的 StringBuilder 了。

#### 【5】字符串常量值的简要说明
**字符串常量池** 是 JVM 为了提升性能和减少内存消耗针对字符串（String 类）专门开辟的一块区域，主要目的是为了避免字符串的重复创建。

```plain
// 在堆中创建字符串对象”ab“
// 将字符串对象”ab“的引用保存在字符串常量池中
String aa = "ab";
// 直接返回字符串常量池中字符串对象”ab“的引用
String bb = "ab";
System.out.println(aa==bb);// true
```

如果使用字符串常量, 如果检测到字符串常量池有，会取出，要不就存入。

> 附：
>
> String s1 = new String("abc"); 这句话创建了几个字符串对象？池存在则创建一个，否则创建两个。
>
> String.intern() 是一个 native（本地）方法，其作用是将指定的字符串对象的引用保存在字符串常量池中。
>

### 十五. 数据结构类
熟悉 List（链表），Queue（队列），Stack（栈）等类，不仅以后刷算法题需要用到，List 在开发中也经常用到。

初始化都是这种格式：

```plain
List<Integer> integerList=new List<>();
Queue<Integer> integerQueue=new Queue<>();
Stack<Integer> integerStack=new Stack<>();
```

例：List 常见 api:add,remove 等

Queue 和 Stack 常见 api：  
push()【插入元素】  
pop()【移除元素，队列先进先出，栈后进先出】  
peek()【栈顶的元素和队首的元素，简单说就是如果执行移除操作要移除的元素是什么】  
empty()【检查是否为空】


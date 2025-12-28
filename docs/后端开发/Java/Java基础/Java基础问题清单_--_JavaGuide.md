## 一.上
+ Javase vs javaee vs javame
+ JDK JRE JVM分别是什么
+ JRE
+ JDK9之后的模块系统 和 jlink工具是干什么的，有什么好处
+ JDK11不提供JRE
+ Java 程序从源代码到运行的完整流程？字节码文件的后缀名是什么？
+ JIT是什么？
+ 为什么说Java编译与解释共存？
+ HotSpot 采用了惰性评估用来干什么？代码执行次数越多，速度会越快吗？
+ AOT是什么 有什么优点和缺点
+ CGLIB的大致原理，为什么不能用AOT
+ Java和C++的区别
+ Java有哪三种注释？
+ Java中八种数据类型及其位数/字节数/取值范围
+ long类型数值后面加上什么？float类型数值后面加上什么？
+ 八种基本类型的包装类
+ Java中类是放在栈上还是堆上的？基本变量呢？
+ 哪些包装类缓存了数据？缓存了什么数据？
+ 什么方法/情况会使用缓存数据？new一个对象会吗？
+ 用什么方法对包装类之间进行比较？
+ 什么是自动拆装箱
+ 拆装箱实际调用什么方法？
+ 为什么要避免频繁拆装箱
+ 为什么浮点数运算的时候会有进度丢失？
+ 如何解决浮点数运算的精度丢失问题
+ 超过long长度的数据要用什么类表示？
+ 什么是静态变量
+ 字符常量和字符串常量的差别。
+ 静态方法为什么不能调用非静态的成员？
+ 重载和重写分别是什么？
+ 什么是可变长参数？
+ 遇到方法的时候会优先匹配固定参数还是可变长参数？
+ 可变长参数的原理

## 二.中
+ 面向对象和面向过程的差别。
+ 创建一个对象用什么运算符?对象实体与对象引用有何不同?
+ 如果一个类没有声明构造方法，该程序能正确执行吗?
+ 构造方法有哪些特点？是否可被 override?
+ 对象的相等和引用相等的区别 
+ 面向对象三大特征
+ 接口和抽象类有什么共同点？有什么区别？
+ 深拷贝和浅拷贝有什么区别？分别怎么实现？
+ Object类里面有什么常用方法

getClass -- 字节码

hashCode equals toString -- 集合 比较 打印 

notify notifyAll wait -- 多线程线程状态转换 

finalize -- jvm

+ == 和 equals() 的区别 
    - ==对于基本数据类型比较的是啥，引用数据类型比较的是啥？
    - equals是用来干什么的？存在于什么类中？没有重写是怎么样的？重写之后达到什么效果？String中的equals被重写过吗？
+ equals的默认实现是什么？为什么通常都要重写equals方法？
+ hashCode()的作用
+ 哈希表是怎么插入数据的？（综合使用hashcode和equals）
+ 为什么重写equals方法时必须重写hashCode方法
+ 重写equals()时没有重写hashCode()方法，使用HashMap可能会出现什么问题
+ String 为什么是不可变的?
+ String StringBuffer、StringBuilder是可变的吗？是线程安全性的吗？性能分别怎么样？使用场景是什么？
+ Java 9 为何要将 String 的底层实现由 char[] 改成了 byte[] ?
+ “+”和“+=”有重载吗？JDK8底层是使用什么呢？JDK9是采用什么策略呢？
+ String#equals() 和 Object#equals() 有何区别？
+ 字符串常量池的作用了解吗？直接=赋值字符串常量会发生什么？
+ String s1 = new String("abc");这句话创建了几个字符串对象？
+ String类的intern方法有什么用？如果字符串已经在常量池会怎么样，如果不在会怎么样？
+ String类型的变量和常量使用+号时候会发生什么？
+ 什么是常量折叠？
+ 什么常量会进行折叠？引用的值可以进行折叠优化吗？

## 三.下
+ Java异常体系 -- Throwable,Exception,Checked exception,Unchecked exception,Error
+ Exception 和 Error 有什么区别？
+ Error比如有哪些
+ Checked Exception 和 Unchecked Exception 有什么区别？
+ Throwable类常用方法getMessage toString getLocalizedMessage printStackTrace分别干什么？什么差别？
+ try catch final异常捕获中try catch final分别是干什么的
+ finally 中的代码一定会执行吗？
+ 什么时候用try-with-resources 代替try-catch-finally？
+ 什么是泛型 反射
+ 注解是干什么的？它的解析方法有哪两种？
+ 什么是spi机制，和api有什么差别？spi怎么实现？spi的优缺点？
+ 什么是序列化和反序列化？有什么应用场景？序列化协议对应于 TCP/IP 4 层模型的哪一层？有些变量不想序列化怎么办？常见的序列化协议有哪些？为什么不推荐使用Java自带的jdk序列化？
+ 什么是语法糖？有哪些常见的语法糖？


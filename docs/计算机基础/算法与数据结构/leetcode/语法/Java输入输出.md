## 1.Scanner类
```plain
import java.util.Scanner;

public class ConsoleInputExample {
    public static void main(String[] args) {
        // 创建一个 Scanner 对象，用于接收控制台输入
        Scanner scanner = new Scanner(System.in);

        // 提示用户输入
        System.out.print("请输入您的姓名: ");

        // 使用 Scanner 对象获取用户输入的字符串
        String name = scanner.nextLine();

        // 打印用户输入的内容
        System.out.println("您输入的姓名是: " + name);

        // 关闭 Scanner 对象
        scanner.close();
    }
}
```

常用API：

```plain
hasNext系列：
boolean hasNext()：如果此扫描器的输入中还有输入，则返回 true 。
boolean hasNextInt()：如果此扫描器的输入中还有输入且可以转换为 int 类型，则返回 true 。

next系列：
String next(): 读取下个字符串，到空格为止
String nextLine()：读取这一行
int nextInt()：读取下一个数转化为int类型
```

## 2.怎么读取单个字符
【1】System.in.read()

```plain
import java.io.IOException;

public class ConsoleInputExample {
    public static void main(String[] args) {
        try {
            System.out.print("请输入一个字符串: ");

            // 逐个字符地读取用户输入
            int ch;
            while ((ch = System.in.read()) != '\n') {
                // 打印每个字符
                System.out.println("读取到的字符为: " + (char) ch);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

【2】使用Scanner的nextline()获取整行，然后进一步处理

使用Scanner的nextline()获取整行然后对该字符串进行处理提取出你想要的字符

```plain
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入一串字符：");
        String input = scanner.nextLine();
        
        // 逐个字符处理输入
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            // 在这里对每个读取到的字符进行处理
            System.out.println("读取到字符：" + ch);
        }
        
        scanner.close();
    }
}
```

## 3.输出
### 【1】System.out.println()和System.out.print()
前一个会自动加一个换行符，而后面不会加。不管什么参数都会转化为字符串输出。

### 【2】System.out.printf()
与c或c++的printf函数一样


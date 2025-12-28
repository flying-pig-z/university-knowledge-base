## 一. Spring Cloud 与 Spring Cloud Alibaba 与 Springboot 各版本的依赖关系
我们可以去 springcloud alibaba 的 [github](https://so.csdn.net/so/search?q=github&spm=1001.2101.3001.7020) 仓库中的说明中查找到三个依赖版本的对应关系：

[版本说明 · alibaba/spring-cloud-alibaba Wiki · GitHub](https://github.com/alibaba/spring-cloud-alibaba/wiki/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E)

## 二. 通过 BOM 对 Spring Cloud 与 Spring Cloud Alibaba 各组件的依赖版本进行控制
**【1】什么是 BOM 呢？**

**BOM（Bill of Materials）是由 Maven 提供的功能, 它通过定义一整套相互兼容的 jar 包版本集合：**[Maven BOM！拿来吧你 - 掘金](https://juejin.cn/post/6987553343983845407)

**【2】SpirngCloud 官方文档的内容：**

![](https://i-blog.csdnimg.cn/blog_migrate/a2a9653b253d4f9aca22074c6b0f4646.png)

**【3】SpringCloudAlibaba 官方文档的内容：**

![](https://i-blog.csdnimg.cn/blog_migrate/7d3a1b04f8ffe6eeb1f70c981c82218a.png)

**【4】简单说意思就是说我们在父项目的 dependencyManagement 引入了上述的依赖后在子项目中书写其各组件的依赖就不用去关心版本的问题。**

**父项目中：**

```plain
    <!--统一管理依赖版本-->
    <dependencyManagement>
        <dependencies>
            <!-- springCloud -->
            <dependency>
                <groupId>org.springframework.cloud</groupId>

                <artifactId>spring-cloud-dependencies</artifactId>

                <version>Hoxton.SR9</version>

                <type>pom</type>

                <scope>import</scope>

            </dependency>

            <!--springCloudAlibaba -->
            <dependency>
                <groupId>com.alibaba.cloud</groupId>

                <artifactId>spring-cloud-alibaba-dependencies</artifactId>

                <version>2.2.6.RELEASE</version>

                <type>pom</type>

                <scope>import</scope>

            </dependency>

    </dependencyManagement>

```

> pom：这里指定了依赖项的类型为 "pom"，表示引入的是一个 POM 文件，通常用于管理其他依赖项的版本号。
>
> import：这里指定了依赖项的作用域为 "import"，表示这个依赖项主要用于进行版本管理，不会实际参与编译和打包。
>

**这样父子项目中与 Spring Cloud 与 Spring Cloud Alibaba 相关的组件依赖就可以省去版本的书写：**

例如原先：

```plain
<!--        openfeign远程连接-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>

            <artifactId>spring-cloud-starter-openfeign</artifactId>

            <version>2.2.6.RELEASE</version>

        </dependency>

```

现在：

```plain
<!--        openfeign远程连接-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>

            <artifactId>spring-cloud-starter-openfeign</artifactId>

        </dependency>

```

**这样就可以统一管理和控制 Spring Cloud 框架中各个模块的版本号。这样做有助于避免版本冲突，简化项目配置，并提高开发效率，不用再去官网查询版本了。****  
****需要注意的是子项目不要忘了继承父项目，不然没有这种效果。**

**另外如果想了解，我们也可以点开** **spring-cloud-dependencies 和 spring-cloud-alibaba-dependencies 去查看各组件的版本。**


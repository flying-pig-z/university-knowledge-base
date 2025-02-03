<meta name="referrer" content="no-referrer"/>

### 初步实现Bean的定义，注册，获取三个基本步骤
搭建一个简单的Spring Bean容器 -- 实现Bean的定义，注册，获取三个基本步骤。

![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1735359136343-e0173a53-dca7-4573-bf89-a5dbc9849371.png)

+ <font style="color:rgb(44, 62, 80);">定义：BeanDefinition，可能这是你在查阅 Spring 源码时经常看到的一个类，例如它会包括 singleton、prototype、BeanClassName 等。</font>
+ <font style="color:rgb(44, 62, 80);">注册：这个过程就相当于我们把数据存放到 HashMap 中，只不过现在 HashMap 存放的是定义了的 Bean 的对象信息。</font>
+ <font style="color:rgb(44, 62, 80);">获取：最后就是获取对象，Bean 的名字就是key，Spring 容器初始化好 Bean 以后，就可以直接获取了。</font>

### Bean的实例化 -- 采用单例Bean实现
完善一种的定义，注册，获取三个基本步骤。

把 Bean 的创建交给容器，而不是我们在调用时候传递一个实例化好的 Bean 对象，另外还需要考虑单例对象，在对象的二次获取时是可以从内存中获取对象的。

为了支持单例模式，这次我们除了存放Bean的对象信息的HashMap，还要多一个存放已经创建的对象的HashMap。

![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1735359407905-4a8b9712-539f-4a0e-9d15-dcbdbc474185.png)

### 基于Cglib实现含构造函数的类实例化策略
前面有个坑，就是如果Bean中有构造函数就无法实例化成功。

<font style="color:rgb(44, 62, 80);">我们实例化对象的代码里并没有考虑对象类是否含构造函数，也就是说如果我们去实例化一个含有构造函数的对象那么就要抛异常了。</font>

<font style="color:rgb(44, 62, 80);">所以我们要解决带有构造函数的Bean的实例化。</font>

<font style="color:rgb(44, 62, 80);">填平这个坑的技术设计主要考虑两部分，一个是串流程从哪合理的把构造函数的入参信息传递到实例化操作里，另外一个是怎么去实例化含有构造函数的对象。</font>

+ <font style="color:rgb(44, 62, 80);">参考 Spring Bean 容器源码的实现方式，在 BeanFactory 中添加</font><font style="color:rgb(44, 62, 80);"> </font>`<font style="color:rgb(71, 101, 130);">Object getBean(String name, Object... args)</font>`<font style="color:rgb(44, 62, 80);"> </font><font style="color:rgb(44, 62, 80);">接口，这样就可以在获取 Bean 时把构造函数的入参信息传递进去了。</font>
+ <font style="color:rgb(44, 62, 80);">另外一个核心的内容是使用什么方式来创建含有构造函数的 Bean 对象呢？这里有两种方式可以选择，一个是基于 Java 本身自带的方法 </font>`<font style="color:rgb(71, 101, 130);">DeclaredConstructor</font>`<font style="color:rgb(44, 62, 80);">，另外一个是使用 Cglib 来动态创建 Bean 对象。</font>_<font style="color:rgb(44, 62, 80);">Cglib 是基于字节码框架 ASM 实现，所以你也可以直接通过 ASM 操作指令码来创建对象</font>_



![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1735359469405-70655104-9a2b-4a72-8513-126b6b30243b.png)

### 注入Bean的属性和依赖对象
如果有类中包含属性那么在实例化的时候就需要把属性信息填充上，这样才是一个完整的对象创建。

对于属性的填充不只是 int、Long、String，还包括还没有实例化的对象属性，都需要在 Bean 创建时进行填充操作。

这里暂时不会考虑Bean的循环依赖。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1735875453445-7a181287-c517-4070-9b1e-2d0fb9ad0c7a.png)

### 实现资源加载器解析XML文件注入对象
![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1735360473241-b8c29a42-f98c-4757-a1ad-285fccd9048d.png)

### <font style="color:rgb(44, 62, 80);">实现上下文操作类和 BeanFactoryPostProcessor 和 BeanPostProcessor接口</font>
<font style="color:rgb(44, 62, 80);">为了能满足于在 Bean 对象从注册到实例化的过程中执行用户的自定义操作，就需要在 Bean 的定义和初始化过程中插入接口类，这个接口再有外部去实现自己需要的服务。那么在结合对 Spring 框架上下文的处理能力，就可以满足我们的目标需求了。整体设计结构如下图：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/42768076/1735362135461-f279b93d-fb5f-4c2b-be0b-ac2381e761f3.png)

+ BeanFactoryPostProcessor，是由 Spring 框架组建提供的容器扩展机制，允许在 Bean 对象注册后但未实例化之前，对 Bean 的定义信息 BeanDefinition 执行修改操作。 
+ BeanPostProcessor，也是 Spring 提供的扩展机制，不过 BeanPostProcessor 是在 Bean 对象实例化前后修改 Bean 对象，也可以替换 Bean 对象。这部分与后面要实现的 AOP 有着密切的关系。 
+ 同时如果只是添加这两个接口，不做任何包装，那么对于使用者来说还是非常麻烦的。我们希望于开发 Spring 的上下文操作类，把相应的 XML 加载 、注册、实例化以及新增的修改和扩展都融合进去，让 Spring 可以自动扫描到我们的新增服务，便于用户使用。

### 实现Bean对象的初始化和销毁方法
![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1735876387951-562d2f35-1609-4da6-a407-1d4650ebd14c.png)

+ <font style="color:rgb(44, 62, 80);">在 spring.xml 配置中添加</font><font style="color:rgb(44, 62, 80);"> </font>`<font style="color:rgb(71, 101, 130);">init-method、destroy-method</font>`<font style="color:rgb(44, 62, 80);"> </font><font style="color:rgb(44, 62, 80);">两个注解，在配置文件加载的过程中，把注解配置一并定义到 BeanDefinition 的属性当中。这样在 initializeBean 初始化操作的工程中，就可以通过反射的方式来调用配置在 Bean 定义属性当中的方法信息了。另外如果是接口实现的方式，那么直接可以通过 Bean 对象调用对应接口定义的方法即可，</font>`<font style="color:rgb(71, 101, 130);">((InitializingBean) bean).afterPropertiesSet()</font>`<font style="color:rgb(44, 62, 80);">，两种方式达到的效果是一样的。</font>
+ <font style="color:rgb(44, 62, 80);">除了在初始化做的操作外，</font>`<font style="color:rgb(71, 101, 130);">destroy-method</font>`<font style="color:rgb(44, 62, 80);"> 和 </font>`<font style="color:rgb(71, 101, 130);">DisposableBean</font>`<font style="color:rgb(44, 62, 80);"> 接口的定义，都会在 Bean 对象初始化完成阶段，执行注册销毁方法的信息</font>
+ <font style="color:rgb(44, 62, 80);">DefaultSingletonBeanRegistry 类中的 disposableBeans 属性里，这是为了后续统一进行操作。</font>_<font style="color:rgb(44, 62, 80);">这里还有一段适配器的使用，因为反射调用和接口直接调用，是两种方式。所以需要使用适配器进行包装，下文代码讲解中参考 DisposableBeanAdapter 的具体实现</font>_<font style="color:rgb(44, 62, 80);"> -关于销毁方法需要在虚拟机执行关闭之前进行操作，所以这里需要用到一个注册钩子的操作，如：</font>`<font style="color:rgb(71, 101, 130);">Runtime.getRuntime().addShutdownHook(new Thread(() -> System.out.println("close！")));</font>`<font style="color:rgb(44, 62, 80);"> </font>_<font style="color:rgb(44, 62, 80);">这段代码你可以执行测试</font>_<font style="color:rgb(44, 62, 80);">，另外你可以使用手动调用 ApplicationContext.close 方法关闭容器。</font>

### 实现Aware接口
`Aware` 接口能让 Bean 能拿到 Spring 容器资源。

Spring 中提供的 `Aware` 接口主要有：

1. `BeanNameAware`：注入当前 bean 对应 beanName；
2. `BeanClassLoaderAware`：注入加载当前 bean 的 ClassLoader；
3. `BeanFactoryAware`：注入当前 `BeanFactory` 容器的引用。

> + <font style="color:rgb(44, 62, 80);">定义接口 Aware，在 Spring 框架中它是一种感知标记性接口，具体的子类定义和实现能感知容器中的相关对象。</font>_<font style="color:rgb(44, 62, 80);">也就是通过这个桥梁，向具体的实现类中提供容器服务</font>_
> + <font style="color:rgb(44, 62, 80);">继承 Aware 的接口包括：BeanFactoryAware、BeanClassLoaderAware、BeanNameAware和ApplicationContextAware，当然在 Spring 源码中还有一些其他关于注解的，不过目前我们还是用不到。</font>
>



### 实现Bean对象作用域[增加原型模式]+实现FactoryBean
> `FactoryBean` 允许你在 Spring 容器中创建复杂的对象。这个复杂对象可能需要一些额外的初始化，或者是基于特定条件动态创建的。通过实现 `FactoryBean`，Spring 容器可以自动处理这些复杂对象的创建。  
>

关于提供一个能让使用者定义复杂的 Bean 对象，功能点非常不错，意义也非常大，因为这样做了之后 Spring 的生态种子孵化箱就此提供了，谁家的框架都可以在此标准上完成自己服务的接入。 

但这样的功能逻辑设计上并不复杂，因为整个 Spring 框架在开发的过程中就已经提供了各项扩展能力的接茬，你只需要在合适的位置提供一个接茬的处理接口调用和相应的功能逻辑实现即可，

像这里的目标实现就是对外提供一个可以二次从 FactoryBean 的 getObject 方法中获取对象的功能即可，这样所有实现此接口的对象类，就可以扩充自己的对象功能了。MyBatis 就是实现了一个 MapperFactoryBean 类，在 getObject 方法中提供 SqlSession 对执行 CRUD 方法的操作。

整体设计结构如下图：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1735886974871-d7f28ae9-c2c0-407b-abf4-b81652ad7d61.png)

+ <font style="color:rgb(44, 62, 80);">整个的实现过程包括了两部分，一个解决单例还是原型对象，另外一个处理 FactoryBean 类型对象创建过程中关于获取具体调用对象的</font><font style="color:rgb(44, 62, 80);"> </font>`<font style="color:rgb(71, 101, 130);">getObject</font>`<font style="color:rgb(44, 62, 80);"> </font><font style="color:rgb(44, 62, 80);">操作。</font>
+ `<font style="color:rgb(71, 101, 130);">SCOPE_SINGLETON</font>`<font style="color:rgb(44, 62, 80);">、</font>`<font style="color:rgb(71, 101, 130);">SCOPE_PROTOTYPE</font>`<font style="color:rgb(44, 62, 80);">，对象类型的创建获取方式，主要区分在于</font><font style="color:rgb(44, 62, 80);"> </font>`<font style="color:rgb(71, 101, 130);">AbstractAutowireCapableBeanFactory#createBean</font>`<font style="color:rgb(44, 62, 80);"> </font><font style="color:rgb(44, 62, 80);">创建完成对象后是否放入到内存中，如果不放入则每次获取都会重新创建。</font>
+ <font style="color:rgb(44, 62, 80);">createBean 执行对象创建、属性填充、依赖加载、前置后置处理、初始化等操作后，就要开始做执行判断整个对象是否是一个 FactoryBean 对象，如果是这样的对象，就需要再继续执行获取 FactoryBean 具体对象中的</font><font style="color:rgb(44, 62, 80);"> </font>`<font style="color:rgb(71, 101, 130);">getObject</font>`<font style="color:rgb(44, 62, 80);"> </font><font style="color:rgb(44, 62, 80);">对象了。整个 getBean 过程中都会新增一个单例类型的判断</font>`<font style="color:rgb(71, 101, 130);">factory.isSingleton()</font>`<font style="color:rgb(44, 62, 80);">，用于决定是否使用内存存放对象信息。</font>

## <font style="color:rgb(44, 62, 80);">  
</font>
<font style="color:rgb(44, 62, 80);">  
</font>

## <font style="color:rgb(44, 62, 80);">  
</font>
## <font style="color:rgb(44, 62, 80);">  
</font>
## <font style="color:rgb(44, 62, 80);">  
</font>

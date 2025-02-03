<meta name="referrer" content="no-referrer"/>

JavaGuide：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1735873799160-648f6336-c165-424b-becb-ab4ad7db612b.png)

小傅哥：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1735873705912-5cebab70-c0b9-41bd-9d90-2ad731b13d27.png)

小傅哥更加完整，但是缺少销毁过程中的注册Destruction相关回调接口。

**下面是我的总结：**

### 实例化（Instantiation）
Spring 容器根据配置 （XML 配置、注解配置或 Java 配置类）  创建 Bean 的实例。这是 Bean 生命周期的开始，Spring 会通过反射机制创建 Bean 实例。

> 加载 -> 注册 -> 使用BeanFactoryPostProcessor修改Bean定义 -> 实例化
>

### 属性赋值
Spring 将配置的属性值和依赖注入到 Bean 实例中，注入依赖的其他 Bean、属性值等。

### 执行 Aware 接口方法 
Spring 检测 Bean 是否实现了 Aware 接口，如果实现了则执行相应方法：

[1]BeanNameAware.setBeanName() - 设置 Bean 的名称

[2]BeanFactoryAware.setBeanFactory() - 注入 BeanFactory 容器实例

[3]ApplicationContextAware.setApplicationContext() - 注入 ApplicationContext 容器实例

### 初始化前
执行 BeanPostProcessor.postProcessBeforeInitialization() 方法，对 Bean 进行前置处理，如修改属性值等。

### 初始化（Initialization）
按以下顺序执行初始化方法：

+ @PostConstruct 注解标注的方法
+ InitializingBean.afterPropertiesSet() 方法
+ XML 配置的 init-method 方法

### 初始化后
执行 BeanPostProcessor.postProcessAfterInitialization() 方法，对 Bean 进行后置处理。

### 使用
Bean 可以被应用程序使用，存活于应用上下文中，处理业务逻辑。

### 销毁前
+ @PreDestroy 注解标注的方法被调用
+ DisposableBean.destroy() 方法被调用
+ XML 配置的 destroy-method 方法被调用


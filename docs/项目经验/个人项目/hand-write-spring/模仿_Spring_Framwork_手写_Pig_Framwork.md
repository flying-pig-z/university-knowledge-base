<meta name="referrer" content="no-referrer"/>

## <font style="color:rgb(31, 35, 40);">一.项目介绍</font>
<font style="color:rgb(31, 35, 40);">项目分为五个模块： ioc模块 aop模块 jdbc模块 webmvc模块 boot模块</font>

demo模块用于webmvc模块 jdbc模块 boot模块的集成测试，这里后三个模块依赖于Spring的ioc和aop能力，并没有与项目中的ioc模块和aop模块集成。

## <font style="color:rgb(31, 35, 40);">二.功能清单</font>
### <font style="color:rgb(31, 35, 40);">1.ioc模块</font>
+ <font style="color:rgb(31, 35, 40);">注册Bean：@Componet @Bean</font>
+ <font style="color:rgb(31, 35, 40);">注入属性：@Value</font>
+ <font style="color:rgb(31, 35, 40);">注入Bean对象：构造函数注入 Setter注入 Field(字段)注入[这里提供@Autowired]</font>
+ <font style="color:rgb(31, 35, 40);">Bean提供单例模式和prototype模式</font>
+ <font style="color:rgb(31, 35, 40);">BeanFactoryPostProcessor接口修改Bean的定义</font>
+ <font style="color:rgb(31, 35, 40);">实现上下文操作类</font>
+ <font style="color:rgb(31, 35, 40);">实现BeanPostProcessor接口</font>
+ <font style="color:rgb(31, 35, 40);">实现Bean对象的初始化和销毁方法：@PreDestroy 注解和@PostConstruct 注解</font>
+ <font style="color:rgb(31, 35, 40);">Aware接口提供Bean获取Spring资源的能力</font>
+ <font style="color:rgb(31, 35, 40);">三级缓存解决循环依赖</font>

### <font style="color:rgb(31, 35, 40);">2.aop模块</font>
<font style="color:rgb(31, 35, 40);">使用jdk动态代理实现简单的aop功能，提供@Advice定义切面类的注解，以及@Before @Around @After通知类型。后续可以通过初始化后置处理绑定到Bean的生命周期中。</font>

### <font style="color:rgb(31, 35, 40);">3.webmvc模块</font>
+ <font style="color:rgb(31, 35, 40);">提供多种Mapping注解定义Get Post Put Delete等请求方法</font>
+ <font style="color:rgb(31, 35, 40);">支持路径参数，query参数，body参数等多种参数类型</font>
+ <font style="color:rgb(31, 35, 40);">提供@ResponseBody将结果序列化返回</font>
+ <font style="color:rgb(31, 35, 40);">使用体验感觉和原来的mvc模块差不多</font>

### <font style="color:rgb(31, 35, 40);">4.jdbc模块</font>
+ <font style="color:rgb(31, 35, 40);">数据库链接配置，并提供starter配置</font>
+ <font style="color:rgb(31, 35, 40);">JdbcTemplate实现对JDBC原有查询和更新操作的封装</font>
+ <font style="color:rgb(31, 35, 40);">事务注解</font>

### <font style="color:rgb(31, 35, 40);">5.boot模块</font>
+ <font style="color:rgb(31, 35, 40);">内置Tomcat和Jetty两种服务器，并可通过配置指定相关的服务器类型和服务启动端口</font>
+ <font style="color:rgb(31, 35, 40);">自动装配，扫描SpringBootAppliation标注主类所在包的Bean对象以及第三方依赖注册的Bean对象。</font>




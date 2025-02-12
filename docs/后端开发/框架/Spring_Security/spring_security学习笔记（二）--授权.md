<meta name="referrer" content="no-referrer"/>

## 零.前情提要
这篇文章主要借鉴B站三更大大关于spring security的教程，这篇文章的大部分内容也来自于那个教程，写这个的主要目的是记录加强印象，总结，并且在文章中我也有穿插自己的想法。

前面的文章【spring security学习笔记（一）–认证】：

https://blog.csdn[.net](https://so.csdn.net/so/search?q=.net&spm=1001.2101.3001.7020)/bjjx123456/article/details/132414814?spm=1001.2014.3001.5501

我们知道spring security的功能主要有两部分：  
一个是认证，就是检验访问系统的用户是不是本系统的用户，能不能访问只有系统用户才能访问的接口。  
另外一个是授权，是指用户是什么身份，能访问系统哪些接口。

总结起来不同用户可以使用不同功能/接口，这就是权限系统要去实现的效果。

举个例子：  
我们设计一个[考勤系统](https://so.csdn.net/so/search?q=%E8%80%83%E5%8B%A4%E7%B3%BB%E7%BB%9F&spm=1001.2101.3001.7020)，由督导调用接口来负责对班级成员的点名。  
如果普通学生知道那个接口的地址，而我们后端如果没有对调用接口用户的身份进行识别，判断调用接口的用户是学生还是督导，该有没有权利使用该接口，那么这个接口就会被利用来修改整个班级的课程考勤情况。

## 一.权限基本流程(简单看一下就好)
在SpringSecurity中，会使用默认的FilterSecurityInterceptor来进行权限校验。在FilterSecurityInterceptor中会从SecurityContextHolder获取其中的Authentication，然后获取其中的权限信息。当前用户是否拥有访问当前资源所需的权限。

所以我们在项目中只需要把当前登录用户的权限信息也存入Authentication,再将Authentication存入SecurityContextHolder。

然后设置我们的资源所需要的权限即可。

## 二.授权实现
### 1.限制访问资源所需权限
SpringSecurity为我们提供了基于注解的[权限控制](https://so.csdn.net/so/search?q=%E6%9D%83%E9%99%90%E6%8E%A7%E5%88%B6&spm=1001.2101.3001.7020)方案，我们可以使用注解去指定访问对应的资源所需的权限。

我们现在原来配置类的上方添加注解：@EnableGlobalMethodSecurity(prePostEnabled = true)

```plain
@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {
	//之前的代码
}
```

然后就可以使用对应的注解：@PreAuthorize

```plain
@RestController
public class HelloController {

    @RequestMapping("/hello")
    @PreAuthorize("hasAuthority('test')")
    public String hello(){
        return "hello";
    }
}
```

注：因为hasAuthority外是双引号，所以里面就只能是单引号。  
对这个注解的理解：实际上是读取注解里面的属性值，读取注解的内容作为表达式/代码进行执行，所以实际上是方法的调用。

### 2.封装权限信息
我们前面在写UserDetailsServiceImpl的时候说过，在查询出用户后还要获取对应的权限信息，封装到UserDetails中返回。  
我们先直接把权限信息写死封装到UserDetails中进行测试。  
我们之前定义了UserDetails的实现类LoginUser，想要让其能封装权限信息就要对其进行修改。

修改内容：增加permissions及authorities的list变量，并重写之前直接返回null的getAuthorities()方法，然后还加了有参构造方法，对user和permissions变量进行构造。

```plain
@Data
@NoArgsConstructor
@AllArgsConstructor
public class LoginUser implements UserDetails{
    private User user;
    //存储权限信息
    private List<String> permissions;
    
    //存储SpringSecurity所需要的权限信息的集合
    //为了避免下面获取权限的方法调用都需要进行封装，我们将这个变量作为成员变量
    //redis默认在存储的时候不会将SimpleGrantedAuthority序列化，加上这个注解使得成员变量不会存储到redis
    @JSONField(serialize = false)
    private List<SimpleGrantedAuthority> authorities;
    
    //有参构造
    public LoginUser(User user,List<String> permissions) {
        this.user = user;
        this.permissions = permissions;
    }
    
    //获取用户权限
    @Override
    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        //把permissions中String类型的权限信息封装成SimpleGrantedAuthority权限类对象
        if(authorities!=null){
            return authorities;
        }
        //把permissions中字符串类型的权限信息转换成GrantedAuthority对象存入authorities中
        // 这里采用stream流编写
        authorities = permissions.stream().
                map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());
        return authorities;
    }
    //判断用户名和密码是否没过期
    @Override
    public boolean isAccountNonExpired() {
        return true;
    }
    //返回用户名
    @Override
    public String getUsername(){
        return user.getNo();
    }
    //返回密码
    @Override
    public String getPassword(){
        return user.getPassword();
    }
    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}
```

LoginUser修改完后我们就可以在UserDetailsServiceImpl中去把权限信息封装到LoginUser中了。我们写死权限进行测试，后面我们再从数据库中查询权限信息。

### 3.从数据库查询权限信息
#### 3.1 RBAC权限模型
RBAC权限模型（Role-Based Access Control）即：基于角色的权限控制。这是目前最常被开发者使用也是相对易用、通用权限模型。  
![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1739339840542-0e47e59b-8827-46ab-be5e-45e817c13e50.png)

简化就是：

![](https://cdn.nlark.com/yuque/0/2025/jpeg/42768076/1739339841077-c0a57fb1-5cd0-4c33-a4c7-8b9a5ba44fe6.jpeg)

> **另外的权限模型–ACL(Access Control List)**  
除了RBAC,还有ACL(Access Control List)，简单说就是用户和权限直接挂钩。  
特点是很简单，不需要那么多表。只需要用户表，权限表，和用户和权限的关联表。  
而RBAC，强调role-based，基于角色，用户要先和角色绑定，再和权限绑定。相对来说较复杂一点。  
ACL适合于用户和权限关系不复杂的系统，而RBAC适合用于用户和权限关系相对复杂的系统。也是利用了分层的思想，相当于在用户和权限之间加了一层角色，便于管理。
>

#### 3.2 根据RBAC权限模型建库
根据RBAC模型建库：

```plain
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sg_security` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `sg_security`;

/*Table structure for table `sys_menu` */

DROP TABLE IF EXISTS `sys_menu`;

CREATE TABLE `sys_menu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `menu_name` varchar(64) NOT NULL DEFAULT 'NULL' COMMENT '菜单名',
  `path` varchar(200) DEFAULT NULL COMMENT '路由地址',
  `component` varchar(255) DEFAULT NULL COMMENT '组件路径',
  `visible` char(1) DEFAULT '0' COMMENT '菜单状态（0显示 1隐藏）',
  `status` char(1) DEFAULT '0' COMMENT '菜单状态（0正常 1停用）',
  `perms` varchar(100) DEFAULT NULL COMMENT '权限标识',
  `icon` varchar(100) DEFAULT '#' COMMENT '菜单图标',
  `create_by` bigint(20) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_by` bigint(20) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `del_flag` int(11) DEFAULT '0' COMMENT '是否删除（0未删除 1已删除）',
  `remark` varchar(500) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='菜单表';

/*Table structure for table `sys_role` */

DROP TABLE IF EXISTS `sys_role`;

CREATE TABLE `sys_role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `role_key` varchar(100) DEFAULT NULL COMMENT '角色权限字符串',
  `status` char(1) DEFAULT '0' COMMENT '角色状态（0正常 1停用）',
  `del_flag` int(1) DEFAULT '0' COMMENT 'del_flag',
  `create_by` bigint(200) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_by` bigint(200) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(500) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='角色表';

/*Table structure for table `sys_role_menu` */

DROP TABLE IF EXISTS `sys_role_menu`;

CREATE TABLE `sys_role_menu` (
  `role_id` bigint(200) NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `menu_id` bigint(200) NOT NULL DEFAULT '0' COMMENT '菜单id',
  PRIMARY KEY (`role_id`,`menu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `sys_user` */

DROP TABLE IF EXISTS `sys_user`;

CREATE TABLE `sys_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `user_name` varchar(64) NOT NULL DEFAULT 'NULL' COMMENT '用户名',
  `nick_name` varchar(64) NOT NULL DEFAULT 'NULL' COMMENT '昵称',
  `password` varchar(64) NOT NULL DEFAULT 'NULL' COMMENT '密码',
  `status` char(1) DEFAULT '0' COMMENT '账号状态（0正常 1停用）',
  `email` varchar(64) DEFAULT NULL COMMENT '邮箱',
  `phonenumber` varchar(32) DEFAULT NULL COMMENT '手机号',
  `sex` char(1) DEFAULT NULL COMMENT '用户性别（0男，1女，2未知）',
  `avatar` varchar(128) DEFAULT NULL COMMENT '头像',
  `user_type` char(1) NOT NULL DEFAULT '1' COMMENT '用户类型（0管理员，1普通用户）',
  `create_by` bigint(20) DEFAULT NULL COMMENT '创建人的用户id',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` bigint(20) DEFAULT NULL COMMENT '更新人',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `del_flag` int(11) DEFAULT '0' COMMENT '删除标志（0代表未删除，1代表已删除）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

/*Table structure for table `sys_user_role` */

DROP TABLE IF EXISTS `sys_user_role`;

CREATE TABLE `sys_user_role` (
  `user_id` bigint(200) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `role_id` bigint(200) NOT NULL DEFAULT '0' COMMENT '角色id',
  PRIMARY KEY (`user_id`,`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

但是里面有很多字段都可以进行简化：

sys_user中主要就是用户id与用户的信息  
sys_role中主要就是角色id和角色信息，如name,role_key  
简化后可以如下：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1739339840225-9678310c-e158-460f-aa52-11c7aa0a8057.png)

sys_menu中就是存储的各种操作的id和操作信息，其中perms是必要的

简化后可以如下：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1739339840280-e7d59498-08a8-4bca-9328-16b447a9eba4.png)

另外两张表是关联表，sys_user_role和sys_role_menu，每张表有两个字段，分别存储两张表的外键。

#### 3.3 代码实现(按照简化后的字段来编写)
##### [1]menu实体类
```plain
/**
 * 权限表(Menu)实体类
 *
 * @author flyingpig
 */
@TableName(value="sys_menu")
@Data
@AllArgsConstructor
@NoArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class Menu implements Serializable {
    private static final long serialVersionUID = -54979041104113736L;

    @TableId
    private Long id;
    /**
     * 菜单名
     */
    private String menuName;
    /**
     * 权限标识
     */
    private String perms;
}
```

##### [2]编写dao层，编写查询用户对应menu表中权限的方法(perms字段)
```plain
public interface MenuMapper extends BaseMapper<Menu> {
    List<String> selectPermsByUserId(Long id);
}
```

对应的mapper文件

```plain
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<mapper namespace="com.flyingpig.mapper.MenuMapper">
    <select id="selectPermsByUserId" resultType="java.lang.String">
        SELECT
            DISTINCT m.`perms`
        FROM
            sys_user_role ur
            LEFT JOIN `sys_role` r ON ur.`role_id` = r.`id`
            LEFT JOIN `sys_role_menu` rm ON ur.`role_id` = rm.`role_id`
            LEFT JOIN `sys_menu` m ON m.`id` = rm.`menu_id`
        WHERE
            user_id = #{userid}
    </select>
</mapper>
```

##### [3]将原先在UserDetailsServiceImpl中写死的权限改为在数据库中查询
```plain
@Service
public class UserDetailsServiceImpl implements UserDetailsService {

    @Autowired
    private UserMapper userMapper;

    @Autowired
    private MenuMapper menuMapper;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        LambdaQueryWrapper<User> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(User::getUserName,username);
        User user = userMapper.selectOne(wrapper);
        if(Objects.isNull(user)){
            throw new RuntimeException("用户名或密码错误");
        }
        List<String> permissionKeyList =  menuMapper.selectPermsByUserId(user.getId());
//        //测试写法
//        List<String> list = new ArrayList<>(Arrays.asList("test"));
        return new LoginUser(user,permissionKeyList);
    }
}
```

##### [4]最后使用@PreAuthorize注解即可对接口做精细化权限控制。
例：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1739339840510-ddc53d0a-c641-441b-b075-89a54f91b181.png)

只有这个user在其对应的role对应的menu表中的perms字段（权限字段）中有sys:student:operation才可以访问。

### 4. 自定义失败处理
我们知道springboot中有全局异常处理器，当发生异常后会如果没在controller层，service层或者dao层进行处理会向上抛出给全局异常处理器，从而统一返回结果。

SpringSecurity也有异常处理机制，我们还希望在认证失败或者是授权失败的情况下也能和我们的接口一样返回相同结构的json，这样可以让前端能对响应进行统一的处理。要实现这个功能我们需要知道SpringSecurity的异常处理机制。

在SpringSecurity中，如果我们在认证或者授权的过程中出现了异常会被ExceptionTranslationFilter捕获到。在ExceptionTranslationFilter中会去判断是认证失败还是授权失败出现的异常。

如果是认证过程中出现的异常会被封装成AuthenticationException然后调用**AuthenticationEntryPoint**对象的方法去进行异常处理。

如果是授权过程中出现的异常会被封装成AccessDeniedException然后调用**AccessDeniedHandler**对象的方法去进行异常处理。

所以如果我们需要自定义异常处理，我们只需要自定义AuthenticationEntryPoint和AccessDeniedHandler然后配置给SpringSecurity即可。

①自定义实现类

```plain
@Component
public class AccessDeniedHandlerImpl implements AccessDeniedHandler {
    @Override
    public void handle(HttpServletRequest request, HttpServletResponse response, AccessDeniedException accessDeniedException) throws IOException, ServletException {
        ResponseResult result = new ResponseResult(HttpStatus.FORBIDDEN.value(), "权限不足");
        String json = JSON.toJSONString(result);
        WebUtils.renderString(response,json);

    }
}
```

```plain
@Component
public class AuthenticationEntryPointImpl implements AuthenticationEntryPoint {
    @Override
    public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException {
        ResponseResult result = new ResponseResult(HttpStatus.UNAUTHORIZED.value(), "认证失败请重新登录");
        String json = JSON.toJSONString(result);
        WebUtils.renderString(response,json);
    }
}
```

②配置给SpringSecurity(SecurityConfig)

```plain
@Autowired
    private AuthenticationEntryPoint authenticationEntryPoint;

    @Autowired
    private AccessDeniedHandler accessDeniedHandler;
```

然后我们可以使用HttpSecurity对象的方法去配置

```plain
http.exceptionHandling().authenticationEntryPoint(authenticationEntryPoint).
                accessDeniedHandler(accessDeniedHandler);
```

但是就是有一个问题，就是如果你定义了AccessDeniedHandlerImpl和springboot的全局异常处理器，AccessDeniedHandlerImpl的异常处理会被后者覆盖，所以为了统一返回结构，我就在springboot中的全局异常处理器中来处理权限不足的异常：

```plain
//全局异常处理器
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(Exception.class)
    public Result ex(Exception ex){
        ex.printStackTrace();
        if(ex instanceof AccessDeniedException){
            return Result.error("身份权限不符合");
        }
        return Result.error("对不起，操作失败，请联系管理员");
    }
}
```

## 三.其他
### 1.其它权限校验方法
我们前面都是使用@PreAuthorize注解，然后在在其中使用的是hasAuthority方法进行校验。SpringSecurity还为我们提供了其它方法例如：hasAnyAuthority，hasRole，hasAnyRole等。

【1】这里我们先不急着去介绍这些方法，我们先去理解hasAuthority的原理，然后再去学习其他方法你就更容易理解，而不是死记硬背区别。并且我们也可以选择定义校验方法，实现我们自己的校验逻辑。

hasAuthority方法实际是执行到了SecurityExpressionRoot的hasAuthority，大家只要断点调试既可知道它内部的校验原理。

它内部其实是调用authentication的getAuthorities方法获取用户的权限列表。然后判断我们存入的方法参数数据在权限列表中。

【2】hasAnyAuthority方法可以传入多个权限，只有用户有其中任意一个权限都可以访问对应资源。

```plain
@PreAuthorize("hasAnyAuthority('admin','test','system:dept:list')")
public String hello(){
	return "hello";
}
```

【3】

### 2.自定义权限校验方法
### 3.CSRF
CSRF是指跨站请求伪造（Cross-site request forgery），是web常见的攻击之一。

https://blog.csdn.net/freeking101/article/details/86537087

SpringSecurity去防止CSRF攻击的方式就是通过csrf_token。后端会生成一个csrf_token，前端发起请求的时候需要携带这个csrf_token,后端会有过滤器进行校验，如果没有携带或者是伪造的就不允许访问。

我们可以发现CSRF攻击依靠的是cookie中所携带的认证信息。但是在前后端分离的项目中我们的认证信息其实是token，而token并不是存储中cookie中，并且需要前端代码去把token设置到请求头中才可以，所以CSRF攻击也就不用担心了。

### 4.其他处理器
#### [1]认证成功处理器
实际上在UsernamePasswordAuthenticationFilter进行登录认证的时候，如果登录成功了是会调用AuthenticationSuccessHandler的方法进行认证成功后的处理的。AuthenticationSuccessHandler就是登录成功处理器。

我们也可以自己去自定义成功处理器进行成功后的相应处理。

```plain
@Component
public class SGSuccessHandler implements AuthenticationSuccessHandler {

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        System.out.println("认证成功了");
    }
}
```

```plain
@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private AuthenticationSuccessHandler successHandler;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.formLogin().successHandler(successHandler);

        http.authorizeRequests().anyRequest().authenticated();
    }
}
```

#### [2]认证失败处理器
实际上在UsernamePasswordAuthenticationFilter进行登录认证的时候，如果认证失败了是会调用AuthenticationFailureHandler的方法进行认证失败后的处理的。AuthenticationFailureHandler就是登录失败处理器。

我们也可以自己去自定义失败处理器进行失败后的相应处理。

```plain
@Component
public class SGFailureHandler implements AuthenticationFailureHandler {
    @Override
    public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
        System.out.println("认证失败了");
    }
}
```

```plain
@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private AuthenticationSuccessHandler successHandler;

    @Autowired
    private AuthenticationFailureHandler failureHandler;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.formLogin()
//                配置认证成功处理器
                .successHandler(successHandler)
//                配置认证失败处理器
                .failureHandler(failureHandler);

        http.authorizeRequests().anyRequest().authenticated();
    }
}
```

#### [3]登出成功处理器
```plain
@Component
public class SGLogoutSuccessHandler implements LogoutSuccessHandler {
    @Override
    public void onLogoutSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        System.out.println("注销成功");
    }
}
```

```plain
@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private AuthenticationSuccessHandler successHandler;

    @Autowired
    private AuthenticationFailureHandler failureHandler;

    @Autowired
    private LogoutSuccessHandler logoutSuccessHandler;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.formLogin()
//                配置认证成功处理器
                .successHandler(successHandler)
//                配置认证失败处理器
                .failureHandler(failureHandler);

        http.logout()
                //配置注销成功处理器
                .logoutSuccessHandler(logoutSuccessHandler);

        http.authorizeRequests().anyRequest().authenticated();
    }
}
```

  


> 来自: [spring security学习笔记（二）--授权_springsecurity hasauthority-CSDN博客](https://blog.csdn.net/bjjx123456/article/details/133468101)
>


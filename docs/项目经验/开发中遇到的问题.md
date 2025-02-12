<meta name="referrer" content="no-referrer"/>

## Java之Docker中部署Websocket
在Docker中部署websocket，设置网络为host，与宿主机共享网络。但前端仍然无法连接

原因是因为Spring Websocket默认映射到127.0.0.1导致出错，所以只能被本地请求。而SpringMVC的HTTP接口不会这样是因为默认被映射到了0.0.0.0，所以可以外界访问。

我们需要通过修改[配置文件](https://so.csdn.net/so/search?q=%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6&spm=1001.2101.3001.7020)将其改为0.0.0.0

```plain
server:
    ip: 0.0.0.0
    port: 8888
```

> 127.0.0.1是本地回环地址，默认情况下只有本地可以访问。  
而0.0.0.0会监听所有地址的请求，包括本地和外界的
>
>   
补充：**255.255.255.255**
>
> 这是广播地址，用于将数据包发送到本地网络中的所有主机。当数据包被发送到广播地址时，网络中的所有主机都会接收到该数据包。然而，大多数情况下，广播地址是用于发送UDP广播消息，而不是用于绑定服务器或服务。
>

## nacos和gateway和sentinel部署实践踩的坑
### nacos
我的微服务项目部署之后，发现不同服务之间无法实现通信，但是我在本地多个服务运行明明运行的很好。

后来我进去 nacos 页面查看各服务的信息，发现各服务对应的 ip 竟然不是我[服务器](https://so.csdn.net/so/search?q=%E6%9C%8D%E5%8A%A1%E5%99%A8&spm=1001.2101.3001.7020)的 ip，而是本地 ip / 或者说是内网 ip。而 nacos 服务发现的基本逻辑就是根据服务名，然后去 nacos 拉取对应的 ip，然后根据 ip 请求接口。如果是内网 ip，如果不像本地测试一样在同一个内网，则无法通信是正常的。

那么怎么解决呢？直接在配置中添加服务注册的 ip 和端口就可以了。

```plain
  cloud:
    nacos:
      server-addr: 
      discovery:
        cluster-name: FJ # 集群名称
        # 注册到nacos的ip与端口
        ip: ip地址
        port: 8081
```

### gateway
gateway 中的路由配置要分开写：

```plain
      routes: # 网关路由配置
        - id: music-service-music
          uri: lb://music-service # 路由的目标地址 lb就是负载均衡，后面跟服务名称
          predicates:
            - Path=/musics/**
        - id: music-service-comment
          uri: lb://music-service # 路由的目标地址 lb就是负载均衡，后面跟服务名称
          predicates:
            - Path=/comments/**
```

而不能合起来写：

```plain
      routes: # 网关路由配置
        - id: music-service-music
          uri: lb://music-service # 路由的目标地址 lb就是负载均衡，后面跟服务名称
          predicates:
            - Path=/musics/**
            - Path=/comments/**
```

因为合起来写它会匹配两次，不管什么链接都不可能通过的。

### sentinel
如果不是一个内网，服务注册到 sentinel 也要写好公网 ip

## 加入PreAuthorize注解鉴权之后NullPointerException报错
记录一次很坑的bug，加入[PreAuthorize注解](https://so.csdn.net/so/search?q=PreAuthorize%E6%B3%A8%E8%A7%A3&spm=1001.2101.3001.7020)鉴权之后NullPointerException报错，按理来说没有权限应该403报错，但是这个是500报错，原因是因为controller层的service注入失败，然而我去掉注解后service注入成功，并且接口仍然可以正常运行，就很迷。

我最后再stackoverflow中发现原来是我的接口的权限修饰符是private，改成public就好了，真的坑！

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1738689977194-a70fc7ed-15df-4abb-8e32-b144361ffd2f.png)![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1738689977180-5dadf45a-4d38-4dc4-9ec5-14b40d32c469.png)

## 跨域问题
### 同源策略
大部分项目都是前后端分离部署的。

![](https://i-blog.csdnimg.cn/blog_migrate/a567d6123caa1aadcdc15eb46634bc03.png)

如果对[服务端](https://so.csdn.net/so/search?q=%E6%9C%8D%E5%8A%A1%E7%AB%AF&spm=1001.2101.3001.7020)没有进行特殊处理，我们在进行前后端联调的时候游览器会发生报错：

![](https://i-blog.csdnimg.cn/blog_migrate/8d1d4b1d8a060998c735d1b6cf0de9e8.png)

这是因为请求被同源策略被阻止，**浏览器**出于安全的考虑，使用 XMLHttpRequest 对象发起 HTTP 请求（异步请求）时必须遵守同源策略，除非服务端允许非同源的请求，否则请求会被游览器拦截，发送失败。

那什么是同源策略呢？

**同源策略（Same-Origin Policy），是一个 web 安全的基础原则。**

#### 同源
什么是同源呢？指的是**协议（如 HTTP 或 HTTPS）、域名和端口号完全相同才算同源。**

#### 跨域
从一个地址请求另一个地址，如果协议、主机、端口三者全部一致则不属于跨域**（CORS--cross origin resource share 跨域资源共享****），否则有一个不一致就是跨域请求，即不同源就是跨域。**

![](https://i-blog.csdnimg.cn/blog_migrate/a116f033cf6fbb7385e26ea4a86ca01d.png)

#### 同源策略
**同源策略简单说就是要求在游览器中网页发送请求的时候，请求的协议，主机，端口要以发送请求的页面（或者脚步）的主机，协议，端口一致。**

**而非同源（跨域）的请求如果没对服务端做特殊处理，默认情况下游览器的请求是无法访问成功的。这就是游览器的同源策略。**

**在游览器中进行前后端联调的时候，本地的端口号与游览器中网页的协议一致，主机一致，但是端口号不一致，所以就会请求接口服务失败。这就是违反了同源策略，产生了跨域问题。所以游览器请求本地接口会失败。**

注：为什么 Postman 没有跨域问题呢？因为 Postman 不是游览器，没有同源策略。

### 跨域请求的原理
**在普通的跨域请求中（非简单请求），浏览器会先发送一个 OPTIONS 请求，该请求称为预检请求（preflight request），用来检查是否允许跨域访问。服务器收到预检请求后，根据请求中的头部信息进行判断，并返回相应的响应头，表示是否允许跨域访问。如果服务器返回的响应头中包含了允许跨域的信息（返回 Access-Control-Allow-Origin 头信息****），浏览器才会发送实际的跨域请求。**

**如果服务器没有正确设置响应头，或者返回的响应头中不包含允许跨域的信息，浏览器会拦截跨域请求，导致请求失败。**

另外，需要注意的是浏览器的同源策略限制只存在于浏览器环境中。只有游览器才有跨域请求，如果在服务器端进行跨域请求，是不受同源策略限制的。

**同源策略的作用是防止恶意网站通过在其页面中注入恶意脚本并获取其他来源的数据，防止跨站点脚本攻击（Cross-Site Scripting，XSS）、跨站点请求伪造（Cross-Site Request Forgery，CSRF）等安全问题的发生。**

### 解决跨域问题的方法
那我们怎么让跨域请求成功发送呢？

#### JSONP-- 了解一下
通过 script 标签的 src 属性进行跨域请求，如果服务端要响应内容则首先读取请求参数 callback 的值，callback 是一个回调函数的名称，服务端读取 callback 的值后将响应内容通过调用 callback 函数的方式告诉请求方。如下图：

![](https://i-blog.csdnimg.cn/blog_migrate/93bc3fccc1202f91376d1c68c3cf1aa2.png)

#### 添加响应头 -- 常用
**服务端在响应头添加 Access-Control-Allow-Origin：*，这样浏览器才会发送实际的跨域请求。**

原理：

![](https://i-blog.csdnimg.cn/blog_migrate/d32f89c7ed1f40f305c0111dd1aedc0a.png)

![](https://i-blog.csdnimg.cn/blog_migrate/05b4a368e8461a031e76899f27e4ae82.png)

实现：

【1】添加 @CrossOrigin 注解

既可以用在 controller 层方法上，表示让这个 controller 层的接口允许跨域，也可以用在 controller 层的该类中所有接口允许跨域

【2】在 springboot 中添加跨域配置类

（实现的原理就是在响应头添加 Access-Control-Allow-Origin）

```plain
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry){
        //设置允许跨域的路径
        registry.addMapping("*")
                //是否允许cookie
                .allowCredentials(true)
                //设置允许的请求方式
                .allowedMethods("GET","POST","DELETE","PUT")
                //设置允许的header属性
                .allowedHeaders("*")
                //跨域允许时间
                .maxAge(3600);
    }
}
```

#### 通过 nginx 代理跨域
![](https://i-blog.csdnimg.cn/blog_migrate/7a605506a86305c8ac53ad107227bceb.png)

![](https://i-blog.csdnimg.cn/blog_migrate/2eebf3e8c6b817bdeb7988a39084b9e3.png)

**简单说以前是直接访问服务器，现在是先访问 nginx 再由 nginx 访问服务器。nginx 相当于代理，因为 nginx 不是游览器，所以没有跨域的问题，通过这样子就解决了跨域的问题。**


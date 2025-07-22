<meta name="referrer" content="no-referrer"/>

## REST
Get -- 查询

POST -- 增加

PUT -- 修改

DELETE -- 删除

## HEAD
只返回HTTP头部而没有内容

**1. 检查资源是否存在**

快速验证URL是否有效，检查文件或页面是否存在而不下载内容

> 网络爬虫和下载工具检查文件大小后再决定是否下载
>

**2. 获取资源元信息**

文件大小，文件类型，最后修改时间，缓存控制信息

**3. 检查资源是否已更新**

通过比较Last-Modified或ETag判断资源是否有变化，实现智能缓存机制

> CDN和缓存系统验证缓存是否过期，检查原始资源状态
>

## <font style="color:rgb(9,13,17);">OPTION</font>
浏览器在**跨域**且**非简单请求**时才会发送OPTIONS预检。

> **什么是简单请求？**
>
> 1. HTTP方法限制
>
> + GET
> + POST
> + HEAD
>
> 2. 请求头限制
>
> + Accept
> + Accept-Language
> + Content-Language
> + Content-Type（但有值的限制）
> + Range（简单范围）
>
> 3. Content-Type限制 
>
> + text/plain
> + application/x-www-form-urlencoded
> + multipart/form-data
>

**作用：**

**1. 预检请求 -- CORS相关请求头**

在CORS（跨域资源共享）场景中，浏览器会自动发送OPTIONS请求作为预检，检查服务器是否允许实际的跨域请求，验证请求域名、请求方法、请求头等是否被服务器允许。

**2. 查询服务器支持的HTTP方法 -- Allow请求头**

获取目标资源支持哪些HTTP方法（GET、POST、PUT、DELETE等），服务器通过`Allow`响应头返回支持的方法列表。

**3. 获取服务器能力信息**

了解服务器对特定资源的处理能力，检查服务器支持的功能特性。

## TRACE请求
HTTP中的TRACE方法主要用于**诊断和调试**目的，**进行回环测试**：当客户端发送TRACE请求时，服务器会将收到的完整请求（包括请求行、请求头等）原样返回给客户端，就像一面"镜子"一样。

因为安全，隐私和实际需求不多，大多数现代Web服务器和代理服务器都默认禁用了TRACE方法，或者返回405 Method Not Allowed响应。

## CONNECT请求
HTTP中的CONNECT方法主要用于**建立隧道连接**，开始加密通信，特别是通过代理服务器建立到目标服务器的TCP连接。

注：WebSocket **不是基于CONNECT请求**建立的，而是基于HTTP的**Upgrade机制**，使用标准的HTTP GET请求进行协议升级。 


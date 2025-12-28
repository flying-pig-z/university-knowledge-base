**目录**

[一.开放端口](https://blog.csdn.net/bjjx123456/article/details/132131628#t0)

[【1】在linux打开防火墙或开放3306端口（其实一般情况下服务器里的防火墙并没有开启）编辑](https://blog.csdn.net/bjjx123456/article/details/132131628#t1)

[【2】在控制台的云安全组里开放端口](https://blog.csdn.net/bjjx123456/article/details/132131628#t2)

[二.修改datagrip连接时高级的useSSL属性](https://blog.csdn.net/bjjx123456/article/details/132131628#t3)

---

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737863473252-71e62361-6f92-4963-8120-d71bf8e6092d.png)

先填好主机（就是IP地址）和端口（默认都是3306，除非你没事去/etc/my.cnf这个配置文件中修改）还有用户名和密码。  
然后你会发现点击测试连接，不通过；点击确定，报错：Connection timed out: connect。  
还是有坑的。下面就来说说怎么解决这个问题的操作，亲测有效，缺一不可。

### 一.开放端口
很重要的一个点，就是开发端口不仅要把服务器的[防火墙](https://so.csdn.net/so/search?q=%E9%98%B2%E7%81%AB%E5%A2%99&spm=1001.2101.3001.7020)打开或者在防火墙关闭但开放3306端口，还需要在阿里云的控制台的云安全组里开放端口。

#### 【1】在linux打开防火墙或开放3306端口（其实一般情况下服务器里的防火墙并没有开启）  
![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737863474187-b2e15572-f6bb-4ba5-a05f-bf2e5c680548.png)
#### 【2】在控制台的云安全组里开放端口（这里演示阿里云）
下面是基于2023年8月的阿里云页面进入云安全组里开放端口的方式。

点击控制台->进入云服务器ECS->点击云服务器ECS页面侧边栏中的安全组->点击里面的安全组ID链接->安全组id页面的安全组规则里点击手动添加需要开放的端口

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737863474085-4d2d9f52-2241-46b3-980e-2ab9dd355b91.png)

### 二.修改datagrip连接时高级的useSSL属性
![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1737863473257-e822e5dc-103b-47f2-b083-ecdf55973efd.png)

**把useSSL属性由TRUE改为FALSE**  


> 来自: [用datagrip远程连接mysql超时怎么解决【连接mysql会遇到的坑】_datagrip连接mysql数据库超时-CSDN博客](https://blog.csdn.net/bjjx123456/article/details/132131628)
>


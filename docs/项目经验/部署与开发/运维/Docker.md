<meta name="referrer" content="no-referrer"/>

## 一.Docker 是干什么的
在没亲自使用过之前，再多的术语也仅仅是抽象，只有写的人或者使用过的人能看懂。  
所以，作为新手来说，先知道 Docker 是用于部署项目就够了，下面展示如何用 [Docker 部署](https://so.csdn.net/so/search?q=Docker%E9%83%A8%E7%BD%B2&spm=1001.2101.3001.7020)项目及 Docker 常用命令。

## 二、安装 Docker
```plain
# 1、yum 包更新到最新 
yum update
# 2、安装需要的软件包， yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的 
yum install -y yum-utils device-mapper-persistent-data lvm2
# 3、 设置yum源
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# 4、 安装docker，出现输入的界面都按 y 
yum install -y docker-ce
# 5、 查看docker版本，验证是否验证成功
docker -v
#6 然后我们就可以启动docker了
systemctl start docker
```

**关联知识点：Docker 进程相关的命令**

```plain
#1.启动docker服务
systemctl start docker
#2.停止docker服务
systemctl stop docker
#3.重启docker服务
systemctl restart docker
#4.查看docker服务状态
systemctl status docker
#5.设置开机启动docker服务
systemctl enable docker
```

## 三. 用 Docker 部署应用
简单说就是先搜索镜像，然后再拉取（下载）镜像，最后再根据镜像创建容器。

#### 1、部署 MySQL
##### 【1】搜索 mysql 镜像
```plain
docker search mysql


```

##### 【2】拉取 mysql 镜像 (这里拉取最新版)
```plain
docker pull mysql:latest


```

##### 【3】创建容器
```plain
docker run --name mysql-server  -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306  -d mysql:latest


```

–name: 容器的名字  
-e 设置 mysql 密码, 要记住你设置的密码  
-p 3306:3306 将 docker 中的 3306 端口映射到宿主机的 3306 端口，外界要访问的就是 3306 端口  
-d 根据什么镜像来创建的

##### 【4】开始使用 mysql
```plain
docker exec -it mysql-server bash

```

```plain
mysql -uroot -p

```

或者将两个命令合起来使用

```plain
docker exec -it mysql-server mysql -uroot -p

```

注：

（1）使用`docker exec`命令，可以在容器中启动一个新的进程，并且可以与该进程进行交互。（2）在 Docker 中，-it 是两个选项的组合：`-i`和`-t`。  
综合使用`-it`选项，可以在容器中运行交互式进程，并且通过终端与之进行交互，比如在终端中键入命令或者接收命令的输出。在上述命令中，`docker exec -it mysql-server mysql -uroot -p`打开了一个交互式的 MySQL 会话，可以使用 MySQL 的命令行工具与数据库进行交互。

##### 【5】用 datagrip 连接 mysql
除了常规的要设置腾讯云防火墙和 linux 的防火墙，连接时候还要将高级的选项除了 useSSL 要为 false,allowPublicKeyRetrieval 也要改为 true。

#### 2、部署 redis
##### 【1】搜索 redis 镜像
```plain
docker search redis


```

##### 【2】拉取 redis 镜像
```plain
docker pull redis:5.0

```

##### 【3】用该 redis 镜像创建容器运行
```plain
#从docker的6379端口映射到宿主机的6379端口，命名为c_redis
docker run -id --name=c_redis -p 6379:6379 redis:5.0
```

## 四. 镜像和容器
### 1. 概念
可以看到有两个非常重要的概念：镜像和容器。

**【1】Docker 镜像可以看作是一个应用程序运行所需的所有文件和依赖项的打包版本，你可以把它当成安装包。**类比于照片，Docker 镜像就像是一张静态的照片，记录了应用程序的全部内容和状态。可以通过构建  Dockerfile 文件来创建镜像，也可以向 Docker Hub 等镜像仓库下载别人构建好的镜像。我们上面就是拉取别人的镜像。



**【2】Docker 容器则是根据镜像创建的运行实例，其主要作用是隔离不同的应用程序或应用程序的不同版本，以便它们不会相互干扰，你可以把它当成是用安装包安装的程序。**类比于卡通里的小木屋，Docker 容器就像是一个动态的小木屋，可以在其中运行应用程序并与外部系统交互。

为什么要隔离呢？比如有两个写好了两个 springboot 程序，一个运行在 java8 的环境，一个运行在 java17 的环境，那样的话如果没有 docker 或者虚拟机，那么两个程序肯定要有一个不能运行。  
其他软件之间也可能会发生这种问题，不同的 app 所需的依赖会冲突，导致部分程序不能运行，这不是我们想看到的。

而 Docker 容器都有自己的文件系统和网络接口，（可以看成是类似于虚拟机）和其他容器以及宿主机完全隔离。

![](https://i-blog.csdnimg.cn/blog_migrate/a8e79f7e850248ad82cd16db96cbe5ee.png)

**从 logo 我们可以看到，如果 docker 是那只鲸鱼，那么容器就是上面的集装箱。**

### 2. 相关命令
接下来介绍镜像和容器相关的命令：

与镜像相关：

```plain
#查看本地所有的镜像
docker images
##查看所用镜像的id
docker images -q
#搜索镜像：从网络中查找需要的镜像
docker search 镜像名称
#拉取镜像：从Docker仓库下载镜像到本地，镜像名称格式为 名称：版本号
#如果版本号不指定则是最新的版本，如果不知道镜像版本，可以去docker hub 搜索对应镜像查看。
docker pull 镜像名称
#删除镜像：删除本地镜像
docker rmi 镜像id #删除指定本地镜像
docker rmi 'docker images -q' #删除所有本地镜像
```

与容器相关：

```plain
#查看容器
docker ps   #查看正在运行的容器
docker ps -a        #查看所有容器
#创建容器
docker run 参数
#进入容器，退出容器不会关闭
docker exec 参数
#停止容器
docker stop 容器名称/id
#启动容器
docker start 容器名称/id
#删除容器：如果容器是运行状态则删除失败，需要停止容器才能删除
docker rm 容器名称/id
#查看容器信息，如网络信息等
docker inspect 容器名称
```

> **docker run 的参数说明：**  
-i: 保持容器运行。通常与 - t 同时使用。加入 it 这两个参数后，容器创建后自动进入容器后，退出容器后，容器自动关闭。  
-t: 为容器重新分配一个伪输入终端，通常与 - i 同时使用。  
-d: 以守护（后台）模式运行容器。创建一个容器在后台运行，需要使用 docker exec 进入容器。退出后，容器不会关闭。  
-name: 为创建容器命名。
>

## 五. Dockerfile-- 构建属于自己的镜像
#### 【1】Dockerfile 概念
Dockerfile 是一个文本文件，用来构建镜像。包含了一条条指令，通过这些指令规定了基础镜像，镜像的环境与数据，并且规定了通过镜像生成容器运行的命令 等信息，最终构建出一个新的镜像。

可以统一开发测试运维的环境，为整个团队提供一个完全一致的开发环境，实现应用的无缝移植。

#### 【2】案例：用 dockerfile 部署 springboot 容器
（1）idea 中用 maven 的 package 命令打包，如果之前打包过可能要用 clear 命令一下。

（2）用 ssh 工具，例如 finalshell 上传到服务器（我是 root 目录下创建个 docker-files 文件夹来存储）

（3）在这个文件夹下创建 springboot_dockerfile 文件，编写 dockerfile-- 不用记，重点知道关键字是什么意思

```plain
FROM openjdk:17-jdk
MAINTAINER flyingpig <1839976096@qq.com>
ADD uuAttendance-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 9090
CMD nohup java -jar app.jar > uuAttendance.log
```

然后就编辑完毕，退出先 cd 到刚刚创建的 root/docker-files

```plain
cd /root/docker-files


```

使用编写好的 dockerfile 构建镜像：

```plain
docker build -f ./springboot_dockerfile -t app .

```

（4）然后就能运行镜像了（但是会遇到问题，看下面）

```plain
 docker run --name uuAttendance app:latest

```

#### 【3】dockerfile 中语句的解释
![](https://i-blog.csdnimg.cn/blog_migrate/13363556d5dfab08be05fe9901d0c96f.png)

各个步骤的解释【自己根据实际情况进行修改】：

```plain
#指定父镜像，指定dockerfile基于那个image构建
FROM openjdk:17-jdk
#定义作者信息，用来标明这个dockerfile谁写的 
MAINTAINER flyingpig <1839976096@qq.com>
 
#将jar包添加到镜像中（生成镜像）
#其中uuAttendance-0.0.1-SNAPSHOT.jar是原来jar包的名称，app.jar是添加到容器后的jar包名称
ADD uuAttendance-0.0.1-SNAPSHOT.jar app.jar
#定义容器启动执行的命令
CMD nohup java -jar /app.jar > /uuAttendance.log
 
 
 
 
通过dockerfile构建镜像：docker bulid -f dockerfile的文件路径 -t 镜像名称:版本
不写版本表示最新版
docker build -f ./springboot_dockerfile -t app .
```

**我们还可以添加 workdir 来指定工作目录，方便后面的挂载, 比如下面指定的是 / app 为工作目录，后面的时候挂载只需要将 / app 挂载到宿主机目录即可【挂载的知识详细看后面的数据卷**】：

```plain
FROM openjdk:17-jdk
MAINTAINER flyingpig <1839976096@qq.com>
#指定容器内部的工作目录 如果没有创建则自动创建，
#通过目录指定在哪个目录下工作，比如下面的jar包就添加到了app目录
WORKDIR /app
ADD websocket-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8888
CMD java -jar /app/app.jar > /app/uuAttendance.log
```

可以看到，上面的文件规定了我们把什么东西扔进镜像（jar 包和 jdk），和通过镜像生成容器所运行的代码 (运行 jar 包)。

#### 【4】发布自己的镜像到 docker hub 上（代办）
#### 【5】遇到的问题
然后你运行你的 springboot 项目，如果说你的项目没调用到数据库，那么一点问题都没有。如果说你有用到 mysql 数据库，并且 mysql 的地址使用 localhost, 那么的话程序就无法正常运行，打开日志，发现报错：

```plain
Caused by: com.mysql.cj.exceptions.CJCommunicationsException: Communications link failure


```

接下去我们讲讲 docker 的网络问题。这是不是顺其自然的学习下面这个知识点了，O(∩_∩)O 哈哈~。

## 六. Docker 网络 --Docker 如何处理容器的网络访问
【1】为什么会出现上面的问题呢？

其实默认情况下容器和容器可以进行网络通信，但是每次创建容器都是 Docker 给容器分配的 IP 地址, 而不是 localhost。  
比如上面的我们在连接数据库的时候都是使用 localhost 的地址：jdbc:mysql://localhost:3306/<数据库名>，但是容器使用的是 docker 分配给属于它自己的 ip，所以连接不上。要改为 jdbc:mysql://<Dokcer 给容器分配的 ip>:3306/< 数据库名 > 才能连接的上。  
但是每次创建容器分配的 ip 都是不一样的，导致我们如果更换容器就需要去重新修改代码中的 ip 地址，很麻烦。

这些情况我们都可以创建自定义网络来解决这些问题。把需要互相连通的容器加入到同一个网络，**这样容器和容器之间就可以通过容器名代替 ip 地址进行互相访问**。

【2】然后讲讲怎么用偷懒的方法解决上述的问题：

最简单的解决方法就是在每次 docker run 的时候添加 --net=host，直接用 host 作为网络。这样容器与主机共享网络命名空间，这意味着容器内的应用程序使用主机的网络配置，包括 IP 地址和端口。  
如果这样写的话端口映射就可以删了，没用。

例如：

```plain
docker run --name mysql-server --net=host -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest


```

```plain
docker run -id --net=host --name=c_redis redis:5.0

```

```plain
 docker run --name uuAttendance --net=host app:latest

```

’这样就可以实现不同容器之间使用 host 网络，从而可以直接使用 localhost 访问。

【3】但是这样并不推荐，更好的方法是建立一个网络

1. 运行以下命令来创建一个自定义网络：

```plain
#创建一个网络命名为my_network
docker network create my_network
```

2. 创建网络后，你可以在启动容器时将其连接到该网络。例如：

```plain
docker run -id --net=my_network --name=c_redis -p 6379:6379 redis:5.0

```

在这个网络中的容器就可以相互连接啦。

![](https://i-blog.csdnimg.cn/blog_migrate/305252d60d5fb32ad3637a360cdd93eb.png)

## 七. Docker 容器的数据卷
### 1. 什么是数据卷以及数据卷的作用
#### **【1】什么是数据卷**
**数据卷的功能：数据卷（volume）是容器内目录与宿主机目录之间映射的桥梁。****  
****它可以****使得容器目录和宿主机（我们的 linux）目录相互绑定。****  
****绑定之后，这两个目录的数据和文件是同步的，只要有一个目录的文件和数据修改另一个目录会立即同步。**

> 首先我们要先知道**什么是容器内目录。**
>
> **其实容器就相当于是虚拟机，每个容器都有自己独立的一套目录。**我们可以通过下面命令查看容器内目录：
>
> **宿主机目录就是我们 Linux 主机上的目录。**
>
> **而数据卷目录就是使得容器内目录与宿主机目录相互绑定来实现数据同步。**
>

```plain
docker exec -it <container-name> /bin/bash
ls /
```

![](https://i-blog.csdnimg.cn/blog_migrate/cd12dcd7581736a9e0c736e5bd16b8b2.png)

![](https://i-blog.csdnimg.cn/blog_migrate/2a375605b4c459dec3d44c525cb15f8e.png)

#### 【2】数据卷的好处
**（1）数据持久化**  
因为 Docker 容器被删除后，在容器中的数据就不在了，但宿主机目录依然存在。所以使用数据卷可以实现容器数据持久化，防止数据丢失。  
比如如果 mysql 容器如果被删了，宿主机目录还存在，那么就可以找回原来 mysql 中的数据。  
**（2）便于对容器的文件进行操作**  
以前我们要操作 docker 某个软件 / 容器的文件，就得进入 docker 容器自己的终端，就像上面那样，但是有了数据卷之后，由于数据同步的功能，我们操作容器的文件就直接在宿主机的目录进行操作就行了。  
比如 nginx 我们经常需要更换 html 中的静态资源来展示不同的页面，还需要去 log 目录查看日志。有了是数据卷之后，我们将其挂载到宿主机中的目录就直接操作宿主机目录即可。  
**（3）容器之间数据交换**  
一个数据卷可以被多个容器和目录同时挂载。也就是说一个宿主机目录中同时拥有多个容器中目录的所有文件和数据，由于数据同步的功能，就可以实现不同容器中的数据共享。

### 2. 怎么配置数据卷 -- 以 nginx 为例
#### 【1】如何设置数据卷？
数据卷大致可以分为具名挂载和匿名挂载。

![](https://i-blog.csdnimg.cn/blog_migrate/cebc863e80920b1e92f1335f5d673d8a.png)![](https://i-blog.csdnimg.cn/blog_migrate/58e95973e6c2fd32cebce5db70574ec6.png)

```plain
#创建启动容器时，使用-v参数设置数据卷
docker run 容器名称或id -v 宿主机目录(文件):容器内目录(文件)
 
 
# 一般的话挂载分为3种
-v 容器内目录(文件)               # 匿名挂载
-v /宿主机目录(文件):容器内目录(文件)    # 指定路径匿名挂载
-v 卷名:容器内目录(文件)        # 具名挂载
```

**（1）具名挂载的时候会创建根据你提供的名字创建一个数据卷，然后将你指定的容器内目录与 / var/lib/docker/volumes/<数据卷名>/_data 绑定。****  
****而匿名挂载则是直接将指定的宿主机目录与容器内目录绑定，但是数据卷却没有名字。**

**注意事项：1. 目录必须是绝对路径，这样才区分卷名和宿主机目录****  
****2. 如果目录不存在，会自动创建，不管是宿主机目录还是容器内目录。****  
****3. 一个数据卷可以被多个容器内目录挂载，一个容器也可以挂载多个数据卷。****  
****但是要注意，一个容器目录只能挂载一个数据卷，不然会报错！！！**

**看到这里你应该不是很清楚，那我们就拿 nginx 举个例子，记得看完下面的例子过后再回来看看！！！**

#### 【2】nginx 场景举例
我们知道 Nginx 中有几个关键的目录：html 目录是放置一些静态资源，conf 目录是放置配置文件，而 log 目录是放置日志文件。

如果我们要让 Nginx 代理我们的静态资源，需要将资源放到 html 目录；如果我们要修改 Nginx 的配置，最好是找到 conf 下的 nginx.conf 文件。

但是容器运行的 Nginx 所有的文件都在容器内部，这样的话我们每次都要进入 nginx 中进行文件的增删改查操作，那如果我们可以在 linux 终端直接操作而不是进入容器自己的终端进行文件操作就好了。所以我们要利用数据卷将 nginx 中的目录与宿主机目录关联，方便我们操作。如图：

![](https://i-blog.csdnimg.cn/blog_migrate/cd12dcd7581736a9e0c736e5bd16b8b2.png)

#### 【3】nginx 部署具体过程
> 1. 搜索 nginx 镜像
>
> docker search nginx  
2. 拉取 nginx 镜像  
docker pull nginx  
3. 创建容器，设置端口映射、目录映射
>
> 上面实现了宿主机目录和容器目录的绑定，但是是匿名数据卷的话没有名字，我们可以使用具名挂载给数据卷设定名字：
>
> 上面我们创建了 conf 数据卷，将容器内目录 / etc/nginx / 与宿主机目录 var/lib/docker/volumes/conf/_data 绑定；  
创建了 logs 目录，将容器内目录 / var/log/nginx 与宿主机目录 var/lib/docker/volumes/logs/_data 绑定；  
创建了 html 目录，将容器内目录 / usr/share/nginx/html 与宿主机目录 var/lib/docker/volumes/html/_data 绑定。
>
> 
>
> **注：docker 没办法做到既指定数据卷的名字，又指定容器对应的目录。**
>

```plain
# 在/root目录下创建nginx目录用于存储nginx数据信息
mkdir ~/nginx
cd ~/nginx
mkdir conf
cd conf
# 在~/nginx/conf/下创建nginx.conf文件,粘贴下面内容
vim nginx.conf
 
 
user  nginx;
worker_processes  1;
​
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;
​
​
events {
    worker_connections  1024;
}
​
​
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
​
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
​
    access_log  /var/log/nginx/access.log  main;
​
    sendfile        on;
    #tcp_nopush     on;
​
    keepalive_timeout  65;
​
    #gzip  on;
​
    include /etc/nginx/conf.d/*.conf;
}
​
```

```plain
​4.运行容器


```

```plain
docker run -id --name=c_nginx -p 80:80 -v /root/nginx/conf/nginx.conf:/etc/nginx/nginx.conf -v /root/nginx/logs:/var/log/nginx -v /root/nginx/html:/usr/share/nginx/html nginx

```

```plain
参数说明：
-p 80:80：将容器的 80端口映射到宿主机的 80 端口
-v /root/nginx/conf/nginx.conf:/etc/nginx/nginx.conf：将主机当前目录下的 /root/nginx/conf/nginx.conf 挂载到容器的 :/etc/nginx/nginx.conf配置文件。
-v /root/nginx/logs:/var/log/nginx：将主机/root/nginx/logs 目录挂载到容器的/var/log/nginx日志目录。
-v /root/nginx/html:/usr/share/nginx/html ：将主机当前目录下的/root/nginx/html目录挂载到容器的/usr/share/nginx/html静态资源目录。



```

```plain
docker run -id --name=c_nginx -p 80:80 -v conf:/etc/nginx -v logs:/var/log/nginx -v html:/usr/share/nginx/html nginx

```

### 3. 数据卷相关命令
| docker volume create | 创建数据卷 |
| --- | --- |
| docker volume ls | 查看所有数据卷 |
| docker volume rm | 删除指定数据卷 |
| docker volume inspect | 查看某个数据卷的详情 |
| docker volume prune | 清除数据卷 |


docker volume create-- 容器与数据卷的挂载要在创建容器时配置，对于创建好的容器，是不能设置数据卷的。**创建容器的过程中，数据卷会自动创建**。

docker volume ls-- 当创建容器挂载完数据卷后，我们可以通过 docker volume ls 命令查看 docker 中存在的数据卷，但是只有具名数据卷，而没有匿名数据卷，也比较好理解，匿名数据卷知识一种绑定，严格意义上来讲应该也不算数据卷。

docker volume rm-- 当我们删除容器后，匿名卷消失了，但是匿名卷和具名卷的目录都不会消失。我们可以通过 rm 的命令来删除具名卷，具名卷删除后具名卷对应的目录也消失了。

docker volume inspect-- 通过 inspect 查看一下某个数据卷的相关信息。

> 补充：我们可以通过 docker inspect <容器名> 查看一下某容器的所有数据卷信息（包括匿名数据卷和具名数据卷）
>
> 例如：
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/c7dc6be95ebd8fe33797a7587aab6d28.png)
>
> 通过查看信息中的 Mounts 部分我们可以知道该容器挂载相关的信息，里面的 name 是数据卷的名字，source 是指这个卷对应的宿主机的目录，destination 则是挂载到容器内的目录。
>
> 我们可以看到里面有一个名字很长的数据卷，但是我们创建的时候没挂载，这是怎么回事呢？这是因为 mysql 创建的时候自动帮我们挂载了数据卷。
>

```plain
# 查看MySQL容器详细信息
docker inspect mysql-server
# 关注其中.Config.Volumes部分和.Mounts部分
```

## 八. Docker Compose
我们部署一个 java 项目，经常包含多个容器 mysql,redis,mq,java 项目, es 等一个个。如果还像之前那样手动的逐一部署，就太麻烦了。

而 Docker Compose 就可以帮助我们实现**多个 Docker 容器的快速部署**。它允许用户通过一个单独的 docker-compose.yml 配置文件来定义一组相关联的应用容器，进而实现快速部署一组关联的容器。

### 1. 编写 compose
docker-compose.yml 文件的基本语法可以参考官方文档：

[Compose file version 3 reference | Docker Docs](https://docs.docker.com/compose/compose-file/compose-file-v3/)

docker-compose 文件中可以定义多个相互关联的应用容器，每一个应用容器被称为一个服务（service）。由于 service 就是在定义某个应用的运行时参数，因此与 docker run 参数非常相似。

对比如下：

| **docker run 参数** | **docker compose 指令** | **说明** |
| --- | --- | --- |
| --name | container_name | 容器名称 |
| -p | ports | 端口映射 |
| -e | environment | 环境变量 |
| -v | volumes | 数据卷配置 |
| --network | networks | 网络 |


举例来说：

```plain
#用docker run部署MySQL的命令如下：
 
docker run -d \
  --name mysql \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=123 \
  -v ./mysql/data:/var/lib/mysql \
  -v ./mysql/conf:/etc/mysql/conf.d \
  -v ./mysql/init:/docker-entrypoint-initdb.d \
  --network flyingpig
  mysql
 
#如果用docker-compose.yml文件来定义，就是这样：
 
version: "3.8"
 
services:
  mysql:
    image: mysql
    container_name: mysql
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: 123
    volumes:
      - "./mysql/conf:/etc/mysql/conf.d"
      - "./mysql/data:/var/lib/mysql"
    networks:
      - new
networks:
  new:
    name: flyingpig
```

**下面是我写的一个有 mysql,redis 和 springboot 下面的 docker-compose****  
****【网络的话是直接与主机共享网络】**

```plain
version: '3'
services:
  mysql-server:
    image: mysql:latest
    container_name: mysql-server
    network_mode: host
    environment:
      - MYSQL_ROOT_PASSWORD=123456
    restart: unless-stopped
 
  redis-server:
    image: redis:5.0
    container_name: redis-server
    network_mode: host
    restart: unless-stopped
 
  springboot-server:
    build:
      context: .
      dockerfile: ./springboot_dockerfile
    image: app:latest
    container_name: springboot-server
    network_mode: host
    volumes:
      - /root/springboot_data:/app
    restart: unless-stopped
```

### 2. 运行 compose
基本语法如下：`docker compose [OPTIONS] [COMMAND]`

| **类型** | **参数或指令** | **说明** |
| --- | --- | --- |
| Options | -f | 指定 compose 文件的路径和名称 |
| | -p | 指定 project 名称。project 就是当前 compose 文件中设置的多个 service 的集合，是逻辑概念 |
| Commands | up | 创建并启动所有 service 容器 |
| | down | 停止并移除所有容器、网络 |
| | ps | 列出所有启动的容器 |
| | logs | 查看指定容器的日志 |
| | stop | 停止容器 |
| | start | 启动容器 |
| | restart | 重启容器 |
| | top | 查看运行的进程 |
| | exec | 在指定的运行中容器中执行命令 |


## 九. Docker 与虚拟机比较
与虚拟机一样，Docker 的每个容器都是一个独立的沙箱，每个 Docker 容器之间的环境相互不影响。比如这个容器可以运行 Java8 的 web 项目, 那个容器可以运行 Java17 的 web 项目之间不会产生冲突，而如果没有 Docker，那么这两个环境只能运行一个。

而且相比与重量级运行不同操作系统，模拟硬件的虚拟机，容器更加轻便，更加接近于原生。

![](https://i-blog.csdnimg.cn/blog_migrate/245056d149e2bc1e5343561e55289d52.png)

![](https://i-blog.csdnimg.cn/blog_migrate/354c04443900096cfe4ad2932d5c35f5.png)

## 十. Docker 总结
所以我们再次回到文章开头的那个话题，Docker 是干什么的？

![](https://i-blog.csdnimg.cn/blog_migrate/a8e79f7e850248ad82cd16db96cbe5ee.png)

总结而言：Docker 主要为我们提供了两个好处：  
（1）一个是简化部署。Docker 提供了镜像和容器的功能，我们可以将我们写好的软件及其环境打包成镜像，然后我们只要通过这个镜像创建对应的容器实例就可以很方便的进行软件的部署。同时，docker 还提供了 docker compose，我们只需要通过一个文件，就可以一键部署很多软件。  
（2）另一个就是提供了环境隔离。与虚拟机一样，Docker 的每个容器都是一个独立的沙箱，每个 Docker 容器之间的环境相互不影响。比如这个容器可以运行 Java8 的 web 项目, 那个容器可以运行 Java17 的 web 项目之间不会产生冲突，而如果没有 Docker，那么这两个环境只能运行一个。  
而且相比与虚拟机，容器更加轻便，更加接近于原生。

现在你再来看这只鲸鱼是不是觉得这只鲸鱼很可爱？

![](https://i-blog.csdnimg.cn/blog_migrate/a8e79f7e850248ad82cd16db96cbe5ee.png)

**本文完。**


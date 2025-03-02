<meta name="referrer" content="no-referrer"/>

## 一. 概述
### 1. 基础概念
数据库、[数据库管理系统](https://so.csdn.net/so/search?q=%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F&spm=1001.2101.3001.7020)、SQL

![](https://i-blog.csdnimg.cn/blog_migrate/1f0f92b60fa8766c09ce5de75f225bd1.png)

### 2. 主流数据库
Oracle：大型的收费数据库，Oracle 公司产品。

MySQL：开源免费的中小型数据库，后来 Sun 公司收购了 MySQL，而 oracle 又收购了 Sun 公司。目前 Oracle 推出了收费版本的 MySQL，也提供了免费的社区版本。

SQL Server：Microsoft 公司推出的收费的中型数据库，C#、.net 等语言常用。

PostgreSQL：开源免费的中小型数据库。

[Sqllite](https://so.csdn.net/so/search?q=Sqllite&spm=1001.2101.3001.7020)：轻量级数据库，一般用于本地。

另外还有一些国产数据库，比如人大金仓，KingBase，OceanDB 这些。

### 3. 主流图形化界面
Navicat DataGrip Sqlyog

个人最喜欢用的是 Navicat，当然因为方便也常用 IDEA 中自带的数据库管理（和 DataGrip 功能相似）。

## 二. 数据模型
1). 关系型数据库（RDBMS）

概念：建立在关系模型基础上，由多张相互连接的二维表组成的数据库。 而所谓二维表，指的是由行和列组成的表，就类似于 Excel 表格数据，有表头、有列、有行， 还可以通过一列关联另外一个表格中的某一列数据。我们之前提到的 MySQL、Oracle、DB2、 SQLServer 这些都是属于关系型数据库，里面都是基于二维表存储数据的。

简单说，基于二维表存储数据的数据库就成为关系型数据库，不是基于二维表存储数据的数据库，就是非关系型数据库。

2). 数据模型 MySQL 是关系型数据库，是基于二维表进行数据存储的，具体的结构图下:

![](https://i-blog.csdnimg.cn/blog_migrate/39b56192b62ff7bb32d1b212d01a15d5.png)

我们可以通过 MySQL 客户端连接数据库管理系统 DBMS，然后通过 DBMS 操作数据库。  
可以使用 SQL 语句，通过数据库管理系统操作数据库，以及操作数据库中的表结构及数据。  
一个数据库服务器中可以创建多个数据库，一个数据库中也可以包含多张表，而一张表中又可以包含多行记录。

## 三. SQL
全称 Structured Query Language，结构化查询语言。操作关系型数据库的编程语言，定义了 一套操作关系型数据库统一标准。

**通用语法**：【1】SQL 语句可以单行或多行书写，以分号结尾  
【2】不区分大小写，关键字建议使用大写  
【3】注释：  
单行注释：-- 注释内容 或 # 注释内容  
多行注释：/* 注释内容 */

SQL 语句，根据其功能，主要分为四类：DDL、DML、DQL、DCL。

![](https://i-blog.csdnimg.cn/blog_migrate/cf3a04fb7cd18cb19d11a2c5368e94b0.png)

### 1.DDL
Data Definition Language，数据定义语言，用来定义数据库对象 (数据库，表，字段) 。

#### 【1】对数据库 (模式) 的增删查
```plain
# 增
create database [ if not exists ] 数据库名 [ default charset 字符集 ] [ collate 排序规则 ] ; # 创建数据库
create schema 模式名 # 创建数据库的另一种写法
create schema 模式名 authorization 用户名
# 在创建模式时,可以使用authorization指定授权的用户可以访问和管理该模式下的对象,
# 同时如果有用户名没有模式名,则模式名默认为用户名
 
# 注:定义数据库/模式,用户必须拥有DBA权限,或者获得了DBA授予的CREATE SCHEMA的权限
 
# 删
drop database [ if exists ] 数据库名 <CASCADE|RESTRICT> ; # 删除数据库
# CASCADE 级联删除，删除模式的同时把该模式中所有的数据库对象全部删除
# RESTRICT 限制删除，如果该模式中定义了下属的数据库对象（如表、视图等）， 则拒绝该删除语句的执行。只有当该模式中没有任何下属的对象是才能执行。
 
# 查
show databases ;#查询所有数据库
use 数据库名 ;#use 数据库名 ;
select database() ;#查询当前数据库
```

> 【1】定义数据库 / 模式实际上定义了一个命名空间，在这个空间中可以定义该模式包含的数据库对象，例如基本表、视图、索引等。
>
> 【2】在 CREATE SCHEMA 中可以接受 CREATE TABLE（创建表） ， CREATE VIEW（创建视图）和 GRANT 字句。 CREATE SCHEMA <模式名> AUTHORIZATION < 用户名 >[< 表定义字句 >|< 视图定义字句 >|< 授权定义字句 >]
>

#### 【2】对表的增删改查
```plain
#查
show tables;#查询当前数据库所有表
desc 表名 ;#查看指定表结构
show create table 表名 ;#查询指定表的建表语句
 
#增[创建表]
CREATE TABLE 表名(
字段1 字段1类型 [列完整性约束条件] [ COMMENT 字段1注释 ],
字段2 字段2类型 [列完整性约束条件] [ COMMENT 字段2注释 ],
字段3 字段3类型 [列完整性约束条件] [ COMMENT 字段3注释 ],
......
字段n 字段n类型 [列完整性约束条件] [COMMENT 字段n注释 ]
 
[表完整性约束条件] 
) [ COMMENT 表注释 ] ;
#注意: [...] 内为可选参数，最后一个字段后面没有逗号
 
#改
ALTER TABLE 表名 RENAME TO 新表名;##修改表名
 
#删
DROP TABLE [ IF EXISTS ] 表名;#删除表;注意: 在删除表的时候，表中的全部数据也都会被删除。
TRUNCATE TABLE 表名;#删除指定表, 并重新创建表
```

#### 【3】对字段的增删改查
```plain
##对字段名的增
ALTER TABLE 表名 ADD 字段名 类型 (长度) [ COMMENT 注释 ] [ 约束 ];#添加字段
 
#改
ALTER TABLE 表名 MODIFY 字段名 新数据类型 (长度);#修改数据类型，MODIFY也可以是ALTER COLUMN
ALTER TABLE 表名 CHANGE 旧字段名 新字段名 类型 (长度) [ COMMENT 注释 ] [ 约束 ];#修改字段名和字段类型
 
#删
ALTER TABLE 表名 DROP 字段名;#删除字段
```

> **数据类型：数值类型，字符串类型，日期时间类型**
>
> 1. 数值类型
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/9dc5c899ecd7b2042d49dbcd41578706.png)
>
> 2. 字符串类型
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/e4bad57eb71a8e96d668e65e2401e56a.png)
>
> 3. 日期时间类型
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/8e77eeb5aced5e7cfa4513f1ee47c78f.png)
>

### 2.DML-- 对表中数据的增删改
DML 英文全称是 Data Manipulation Language(数据操作语言)，用来对数据库中表的数据记录进行增、删、改操作。  
添加数据（INSERT） 修改数据（UPDATE） 删除数据（DELETE）

```plain
#增
INSERT INTO 表名 (字段名1, 字段名2, ...) VALUES (值1, 值2, ...);#给指定字段添加数据
INSERT INTO 表名 VALUES (值1, 值2, ...);#给全部字段添加数据
INSERT INTO 表名 (字段名1, 字段名2, ...) VALUES (值1, 值2, ...), (值1, 值2, ...), (值1, 值2, ...) ;#批量添加数据
INSERT INTO 表名 VALUES (值1, 值2, ...), (值1, 值2, ...), (值1, 值2, ...) ;#批量添加数据
 
/*
注：字符串和日期型数据应该包含在引号中。插入的数据类型和大小要符合字段规定。
*/
 
#删
DELETE FROM 表名 [ WHERE 条件 ] ;
 
#改
UPDATE 表名 SET 字段名1 = 值1 , 字段名2 = 值2 , .... [ WHERE 条件 ] ;
```

> 记忆：SELECT 和 DELETE 使用 from 语句，而 UPDATE 和 INSERT 不是
>

### 3.DQL-- 对表中数据的查询
DQL 英文全称是 Data Query Language(数据查询语言)，数据查询语言，用来查询数据库中表的记 录。

查询关键字: SELECT

#### 1. 基本语法
```plain
SELECT
    字段列表
FROM
    表名列表
WHERE
    条件列表
GROUP BY
    分组字段列表
HAVING
    分组后条件列表
ORDER BY
    排序字段列表
LIMIT
    分页参数
```

#### 2. 语法
```plain
#基本查询
SELECT 字段1, 字段2, 字段3 ... FROM 表名 ; # 查询多个字段
SELECT * FROM 表名 ; # 查询所有专业,开发中尽量少用，因为无法做到覆盖索引，影响效率
SELECT 字段1 [ AS 别名1 ] , 字段2 [ AS 别名2 ] ... FROM 表名; # 字段设置别名
SELECT 字段1 [ 别名1 ] , 字段2 [ 别名2 ] ... FROM 表名; # 字段设置别名
SELECT DISTINCT 字段列表 FROM 表名; # 去除重复记录
 
#条件查询
SELECT 字段列表 FROM 表名 WHERE 条件列表 ;
 
#聚合函数查询
SELECT 聚合函数(字段列表) FROM 表名 ;
/*
注意 : NULL值是不参与所有聚合函数运算的。
*/
 
#分组查询[分为不同组进行查询]
SELECT 字段列表 FROM 表名 [ WHERE 条件 ] GROUP BY 分组字段名 [ HAVING 分组后过滤条件 ];
/*
1.where与having区别
执行时机不同：where是分组之前进行过滤，不满足where条件，不参与分组；而having是分组
之后对结果进行过滤。
判断条件不同：where不能对聚合函数进行判断，而having可以。
2.注意事项:
• 分组之后，查询的字段一般为聚合函数和分组字段，查询其他字段会出错。（重点！！！）
• 执行顺序: where > 聚合函数 > having 。
• 支持多字段分组, 具体语法为 : group by columnA, columnB
*/
 
#排序查询
SELECT 字段列表 FROM 表名 ORDER BY 字段1 排序方式1 , 字段2 排序方式2 ;
/*
排序方式
ASC : 升序(默认值)
DESC: 降序
注意事项：
• 如果是升序, 可以不指定排序方式ASC ;
• 如果是多字段排序，当第一个字段值相同时，才会根据第二个字段进行排序 ;
*/
 
#分页查询
SELECT 字段列表 FROM 表名 LIMIT 起始索引, 查询记录数 ;
SELECT 字段列表 FROM 表名 LIMIT 起始索引 OFFSET 偏移量 ;
/*
注意事项:
• 起始索引从0开始，起始索引 = （查询页码 - 1）* 每页显示记录数
• 分页查询是数据库的方言，不同的数据库有不同的实现，MySQL中是LIMIT
• 如果查询的是第一页数据，起始索引可以省略，直接简写为 limit 10
• limit 10 OFFSET 5,表示跳过前5个从第6个开始查询后面10个
*/
 
```

> **运算符大全：**
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/b82384022448ff894072f2e7d61ba72d.png)
>

#### 3. 执行顺序
![](https://i-blog.csdnimg.cn/blog_migrate/0d236e1310a50e4a23a303f650095697.png)

### 4.DCL-- 对用户和用户访问权限的增删改查
#### 【1】对用户的增删改查
```plain
#创建用户
CREATE USER '用户名'@'主机名' IDENTIFIED BY '密码';
 
#删除用户
DROP USER '用户名'@'主机名' ;
 
#修改用户密码
ALTER USER '用户名'@'主机名' IDENTIFIED WITH mysql_native_password BY '新密码' ;
 
#查询用户
select * from mysql.user;
 
/*
注意事项:
• 在MySQL中需要通过用户名@主机名的方式，来唯一标识一个用户。
• 主机名可以使用 % 通配。
• 这类SQL开发人员操作的比较少，主要是DBA（ Database Administrator 数据库管理员）使用。
*/
```

#### 【2】对用户权限的增删查
MySQL 中定义了很多种权限，但是常用的就以下几种：

![](https://i-blog.csdnimg.cn/blog_migrate/3e24781e5fb684ac7c343374d97cc806.png)

```plain
#查询权限
SHOW GRANTS FOR '用户名'@'主机名' ;
#授予权限
GRANT 权限列表 ON 数据库名.表名 TO '用户名'@'主机名';
#撤销权限
REVOKE 权限列表 ON 数据库名.表名 FROM '用户名'@'主机名';
/*
注意事项：
• 多个权限之间，使用逗号分隔
• 授权时， 数据库名和表名可以使用 * 进行通配，代表所有。
*/
```

## 四. Case 语句和函数
### 1.Case 语句
我们在一些复杂查询的时候经常需要进行条件判断，这时候就需要 Case 语句。

CASE 语句用于根据条件返回不同的值，适用于 SELECT、UPDATE、DELETE 等 SQL 语句中。语法如下：

```plain
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE default_result
END
```

case  
when then  
when then  
else  
end

##### 示例
使用相同的 employees 表，我们可以使用 CASE 语句来创建一个查询，返回员工的薪资等级：

```plain
SELECT 
    name,
    salary,
    CASE 
        WHEN salary > 6000 THEN '高薪员工'
        WHEN salary BETWEEN 4000 AND 6000 THEN '中薪员工'
        ELSE '低薪员工'
    END AS level
FROM employees;
/* 
then 后面不能是表达式，要是值
*/
```

### 2. 函数
MySQL 中的函数主要分为以下四类： 字符串函数、数值函数、日期函数【处理字符串，数值，日期】  
流程函数【一些判断功能】。

我们可以自定义函数，具体语法这里省略。

> SQL 中的函数不同于存储过程。
>
> 最明显的区别是函数可以在 SQL 中使用，而存储过程不可以。  
函数通常返回单个值。  
函数只能用于查询而不是修改操作。
>
> 总而言之，函数是复杂查询功能的封装，在语句中调用；而存储过程是一整个操作流程的封装。
>

## 五. 约束 -- 规定表中字段的规则
### 1. 概述
概念：约束是作用于表中字段上的规则，用于限制存储在表中的数据。  
目的：保证数据库中数据的正确、有效性和完整性。

分类:

![](https://i-blog.csdnimg.cn/blog_migrate/476cf671de7e18e54432eca9750a2bdc.png)

### 2. 外键约束
其中主要讲讲外键约束。

外键：用来让两张表的数据之间建立连接，形成关系。可以想象成指针，由一张表指向另一张表。

![](https://i-blog.csdnimg.cn/blog_migrate/c1a83e81b219c54fa226d6ec9f6d136f.png)

但是目前上述两张表，只是在逻辑上存在这样一层关系；在数据库层面，并未建立外键关联。所以需要外键约束来在数据库层面建立外键。  
并且我们还可以增加外键规则来保证数据的一致性和完整性的。

外键的增加和删除语句：

```plain
#增加外键
CREATE TABLE 表名(
字段名 数据类型,
...
[CONSTRAINT] [外键名称] FOREIGN KEY (外键字段名) REFERENCES 主表 (主表列名)
);
 
ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY (外键字段名)
REFERENCES 主表 (主表列名) ;
例：alter table emp add constraint fk_emp_dept_id foreign key (dept_id) references
dept(id);
 
#删除外键
ALTER TABLE 表名 DROP FOREIGN KEY 外键名称;
例：alter table emp drop foreign key fk_emp_dept_id;
```

规定删除和更新的数据一致性：

![](https://i-blog.csdnimg.cn/blog_migrate/8abc9b90c41968f54f1cf0e622b12873.png)

具体语法：

```plain
ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY (外键字段) REFERENCES
主表名 (主表字段名) ON UPDATE CASCADE ON DELETE CASCADE;
例：
alter table emp add constraint fk_emp_dept_id foreign key (dept_id) references dept(id) on update cascade on delete cascade ;
```

## 六. 多表联查
### 1. 关系型数据库的三种关系
因为是关系型数据库，表和表之间通过外键连接存在关系，可以分为 3 种。

【1】一对多  
案例: 部门 与 员工的关系  
关系: 一个部门对应多个员工，一个员工对应一个部门  
实现: 在多的一方建立外键，指向一的一方的主键  
【2】多对多  
案例: 学生 与 课程的关系  
关系: 一个学生可以选修多门课程，一门课程也可以供多个学生选择  
实现: 建立第三张中间表，中间表至少包含两个外键，分别关联两方主键  
【3】一对一  
案例: 用户 与 用户详情的关系  
关系: 一对一关系，多用于单表拆分，将一张表的基础字段放在一张表中，其他详情字段放在另 一张表中，以提升操作效率  
实现: 在任意一方加入外键，关联另外一方的主键，并且设置外键为唯一的 (UNIQUE)

### 2. 多表查询概述
多表查询就是指从多张表中查询关联行的数据。

**连接查询****分类**  
内连接：**查询 A、B 交集部分数据 (AB)**  
外连接：  
左外连接：**查询左表的所有数据和右表交集部分的数据 (A+AB)**  
右外连接：**查询右表的所有数据和左表交集部分的数据 (****(B+AB)**  
自连接：**当前表与自身的连接条件查询**【**自连接必须使用表别名**】

![](https://i-blog.csdnimg.cn/blog_migrate/39cc4397d8b3178bfc638a4386947a41.png)

### 3. 内连接
内连接的语法分为两种写法: 隐式内连接、显式内连接。先来学习一下具体的语法结构。

**隐式的写法直接用表. 属性，而显示的写法是 inner join 另一张表 on 条件。一般都用前一种。**

```plain
SELECT 字段列表 FROM 表1 , 表2 WHERE 条件 ... ;#隐式内连接
例：select emp.name , dept.name from emp , dept where emp.dept_id = dept.id ;
-- 为每一张表起别名,简化SQL编写
select e.name,d.name from emp e , dept d where e.dept_id = d.id;
 
SELECT 字段列表 FROM 表1 [ INNER ] JOIN 表2 ON 连接条件 ... ;#显式内连接
例：select e.name, d.name from emp e inner join dept d on e.dept_id = d.id;
-- 为每一张表起别名,简化SQL编写
select e.name, d.name from emp e join dept d on e.dept_id = d.id;
```

### 4. 外连接
 外连接分为两种，分别是：左外连接 和 右外连接。具体的语法结构为：

```plain
SELECT 字段列表 FROM 表1 LEFT [ OUTER ] JOIN 表2 ON 条件 ... ;#左外连接
例：select e.*, d.name from emp e left outer join dept d on e.dept_id = d.id;
 
SELECT 字段列表 FROM 表1 RIGHT [ OUTER ] JOIN 表2 ON 条件 ... ;#右外连接
例：select d.*, e.* from emp e right outer join dept d on e.dept_id = d.id;
```

**left/right outer join 另一张表 on 条件**

**注意事项： 左外连接和右外连接是可以相互替换的，只需要调整在连接查询时 SQL 中，表结构的先后顺序就可以了。而我们在日常开发使用时，更偏向于左外连接。**

### 5. 自连接
自连接查询，顾名思义，就是自己连接自己，也就是把一张表连接查询多次。我们先来学习一下自连接 的查询语法：

```plain
SELECT 字段列表 FROM 表A 别名A JOIN 表A 别名B ON 条件 ... ;
例：select a.name , b.name from emp a , emp b where a.managerid = b.id;
```

**注意事项: 在自连接查询中，必须要为表起别名，要不然我们不清楚所指定的条件、返回的字段，到底 是哪一张表的字段。** 

**其他查询要根据有没有重复名称的字段来判断是否要起别名。**

### 6. 联合查询
对于 union 查询，就是把多次查询的结果合并起来，形成一个新的查询结果集。

```plain
SELECT 字段列表 FROM 表A ...
UNION [ ALL ]
SELECT 字段列表 FROM 表B ....;
例：
select * from emp where salary < 5000
union all
select * from emp where age > 50;
```

 对于联合查询的多张表的列数必须保持一致，字段类型也需要保持一致。 union all 会将全部的数据直接合并在一起，union 会对合并之后的数据去重。                          

## 七. 子查询
SQL 语句中嵌套 SELECT 语句，称为嵌套查询，又称子查询。

案例：

```plain
# 比较运算符+子查询
SELECT * FROM t1 WHERE column1 = ( SELECT column1 FROM t2 );
 
select * from emp where entrydate > (select entrydate from emp where name = '方东白');
 
select * from emp where dept_id in (select id from dept where name = '销售部' or name = '市场部');
 
# ANY(SOME)/ALL+子查询   ANY--任意一个值   ALL--所有值
select Sname, Sage from Student where Sage < ANY 
    (select Sage from Student where Sdept= ' CS ')
 
```

根据子查询结果不同，分为：  
A. 标量子查询（子查询结果为单个值）  
B. 列子查询 (子查询结果为一列)  
C. 行子查询 (子查询结果为一行)  
D. 表子查询 (子查询结果为多行多列)  
根据子查询位置，分为： A. WHERE 之后 B. FROM 之后 C. SELECT 之后

除了 SELECT 语句，子查询外部的语句还可以是 INSERT / UPDATE / DELETE。

比如涉及多张表条件的 Update 就需要子查询。

> **子查询和多表查询可以相互转化。****  
****子查询相对来说逻辑比较简单，但是写起来不够简洁。**
>
> 同样的，面对表中的属性冲突子查询中也要对表起别名。  
父查询中的表会对子查询起作用，而子查询中的表不会在父查询中起作用。  
如果父查询中 teacher 表，而子查询也有 teacher 表，会优先使用子查询的 teacher 表，比如 teacher.id 会优先使用子查询中的 teacher 表。但是为了避免歧义还是都标注上别名好。
>


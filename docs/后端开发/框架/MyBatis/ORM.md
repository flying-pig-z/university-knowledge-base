<meta name="referrer" content="no-referrer"/>

### ORM框架
ORM(Object Relational Mapping，对象关系映射)是一种将数据库中的表记录映射为对象的技术，它让开发者可以用面向对象的方式来操作数据库，而不需要直接写SQL语句。

### 半自动ORM和全自动ORM
半自动ORM：需要手动编写SQL或类SQL语句。

特点：支持更细粒度的SQL控制，性能调优更灵活。

代表框架：

+ MyBatis
+ JdbcTemplate

全自动ORM：自动生成SQL语句，无需编写SQL，直接使用面向对象的方式。

特点：开发效率更高，对复杂查询支持相对较弱。

代表框架：

+ Hibernate
+ JPA

### MyBatis-Plus
MyBatis-Plus是一个基于MyBatis的增强工具，它可以看做是半自动ORM和全自动ORM的混合，既可以使用面向对象的方式操作SQL，又可以手动编写SQL语句。




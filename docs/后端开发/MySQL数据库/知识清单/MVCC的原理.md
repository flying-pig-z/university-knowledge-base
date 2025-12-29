<meta name="referrer" content="no-referrer"/>

## MVCC简介
MVCC (Multi-Version Concurrency Control) 多版本并发控制是数据库管理系统中常用的并发控制机制。MVCC的设计目标是在不加锁的情况下实现事务的隔离性，提供一致性的数据读取。在InnoDB中，MVCC的实现主要是为了支持RC（Read Committed）和RR（Repeatable Read）这两种隔离级别。

## MVCC的实现要素介绍
MVCC是借助隐藏字段，ReadView，Undo Log进行实现的，这里来详细介绍一下。

> **这里先有个概念，然后有了概念之后去看三，边看三边回来看这里**
>

### 隐藏字段
InnoDB在每行记录中都保存了三个隐藏字段：

1. `DB_TRX_ID` (6字节)：表示最后一次修改该行记录的事务ID

> 事务ID是在事务第一次修改数据时被分配。这个事务ID是严格递增的。  
每个数据行都有一个事务ID，用于记录最后一次修改该行数据的事务ID。
>

2. `DB_ROLL_PTR` (7字节)：回滚指针，指向该行记录的上一个版本（undo log）
3. `DB_ROW_ID` (6字节)：行ID，当表没有主键时，InnoDB会自动生成

### ReadView
**ReadView是事务进行读操作时用到的一致性视图**，包含以下重要信息：

1. `creator_trx_id`：创建该ReadView的事务ID
2. `trx_ids`：活跃的事务ID列表
3. `low_limit_id`：高水位，大于这个ID的数据版本均不可见
4. `up_limit_id`：低水位，小于这个ID的数据版本均可见

### 可见性判断算法
InnoDB判断一个数据版本是否可见的算法如下：

1. 如果记录的db_trx_id等于creator_trx_id（创建者事务ID），该版本可见
2. 如果记录的db_trx_id小于up_limit_id，该版本可见
3. 如果记录的db_trx_id大于等于low_limit_id，该版本不可见
4. 如果记录的db_trx_id在up_limit_id和low_limit_id之间： 
    - 如果db_trx_id在trx_ids列表中，说明该记录由还未提交的事务生成，不可见
    - 如果db_trx_id不在trx_ids列表中，说明该记录由已经提交的事务生成，可见

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1738891200614-e881037e-75b8-487f-b544-af40902a17ae.png)

### Undo Log
Undo Log是MVCC实现的关键组件。

实际上MVCC所谓的多版本不是真的存储了多个版本的数据，只是借助undolog记录数据被修改前的值，根据这些值进行反向操作，就可以回退到之前的版本。

所以看起来是多个版本，实际上就只有一个最新版本。

每行记录都有一个版本链，版本链通过DB_ROLL_PTR连接，最新的版本在数据库中，历史版本在Undo Log中。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1738897257394-084c5a05-4700-49ad-8b08-aa4cf796e486.png)

## MVCC操作流程详解
### 读操作流程
#### 快照读
（1）获取当前事务ID

（2）根据隐藏字段DB_TRX_ID，获取记录的最新事务ID

（3）创建一个ReadView（RC级别每次读都生成，RR级别第一次读生成），根据ReadView的可见性算法判断是否可见，如果不可见，沿着版本链找到可见的版本，返回可见版本的数据。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1738894416921-bae832d6-4aee-483f-8824-7fdf987edcdc.png)

#### 当前读
> SELECT ... FOR UPDATE
>
> SELECT ... LOCK IN SHARE MODE
>
> INSERT、UPDATE、DELETE
>

这些操作会读取最新的记录版本，也就是数据库本来的数据，并加锁

### 写操作流程
1. INSERT操作：

为新记录分配事务ID，记录的DB_TRX_ID设置为当前事务ID，DB_ROLL_PTR设置为NULL（新插入的记录没有历史版本），记录写入数据表。

2. UPDATE操作 

将原记录复制到undo log中，更新DB_ROLL_PTR指向这条undo log记录，修改记录的值，更新记录的DB_TRX_ID为当前事务ID。

3. DELETE操作 

将记录复制到undo log中，标记记录为删除状态，更新记录的DB_TRX_ID为当前事务ID。

**简单说就是更新操作会更新记录的事务ID为当前事务ID，然后更新操作还要更新undo log指针从而新的版本，原始版本仍然存在。**

### 事务提交和回滚
1. 事务提交

当一个事务提交时，它所做的修改将成为数据库的最新版本，并且对其他事务可见，更新事务提交版本号undo log标记为可被回收。

2. 事务回滚

当一个事务回滚时，它所做的修改将被撤销，对其他事务不可见。

原理：通过DB_ROLL_PTR找到undo log中的历史版本，将历史版本的数据恢复到数据表中，清理本事务产生的undo log，释放事务持有的锁。

### 版本回收机制
为了防止数据库中的版本无限增长，MVCC 会定期进行版本的回收，也就是会定期删除过期的undo log。

清理条件： 

+ 该版本的事务已经提交
+ 没有任何活跃的事务会访问这个版本
+ 版本链中有更新的可用版本

## RC 和 RR 隔离级别下 MVCC 的差异
在 RC 读已提交隔离级别下的 每次select 查询前都生成一个Read View (m_ids 列表)

在 RR 可重复读隔离级别下只在事务开始后 第一次select 数据前生成一个Read View（m_ids 列表）

> 这里更新ReadView实际上是更新其中的m_ids列表
>

总所周知，RC模式是防止rollback带来的脏读造成的数据不一样，使用MVVC版本号，每次读取的数据都是已经提交过的，没有提交过的版本不会被写入，所以就不会有脏读。

而RR模式是防止更新数据造成的不可重复读，全局只使用一个ReadView使得每一个时刻读到的数据都是一样的，这样就不会造成不可重复读。



> 写入都一样，每次都创建新的版本写入成功都覆盖
>
> 主要是读的方面的差别，简单说读已提交的读取都是基于最新已经提交的版本进行的
>
> 而可重复读的读取是基于事务中第一次的版本
>

## RR 可重复读隔离级别是怎么阻止幻读的
InnoDB存储引擎在 RR 级别下通过 MVCC和 Next-key Lock 来解决幻读问题：

【1】对于普通的SQL，MVCC就可以防止幻读

因为RR隔离级别只会在事务开启后的第一次查询生成Read View，所以事务进行过程中其他事务所做的插入对事务并不可见，这样就防止了幻读。

【2】而对于当前读（select...for update/lock in share mode、insert、update、delete）

当前读读取的都是最新数据，所以MVCC就补气作用，这时候InnoDB用临键锁，也就是Next-key Lock来防止幻读。

当执行当前读时，临键锁锁定读取数据他们之间的间隙，防止其它事务在查询范围内插入数据。


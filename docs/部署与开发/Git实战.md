<meta name="referrer" content="no-referrer"/>

假设有两个分支，master分支和feature分支。

> 也可能有release分支，具体要看公司的发布流程是feature-->master，还是feature-->release-->master，还是其他
>

1.刚开始的时候，要拉取远程仓库master的最新代码

2.要开发一个新的功能：创建一个本地仓库的特性开发分支，如命名为feature_add_4，并且推送到远程仓库

3.开始写代码，在特性分支开发代码，写完之后推送到远程对应的特性分支

4.推送过程可能遇到提交冲突（远程仓库有你本地没有的更改），这时候要先merge再push，或者先pull再push。

> 写代码之前最好先pull拉取一下，但是即时是这样，也会有新的提交，这种情况难以避免。
>
> 这两种方法本质都是一样的，当远程仓库有你本地没有的更改，pull操作本质也是执行merge操作。
>

如果过程中有代码冲突（线上新的提交与现在提交要修改同一块代码），就需要手动解决冲突，然后再push。

5.测试代码，然后再合并feature分支到release或master。

6.如果release或master中已经有了新的提交，要同步新的提交到特性分支。

就把新的提交拉取到本地仓库master分支，再合并master到feature分支。

（如果有代码冲突，以上线为主，也可以依据实际情况解决）

> master 分支：a --> b --> c  
feature 分支：a --> b --> d
>
> 合并后的feature：
>
> a --> b --> c (master)
>
>       \     \
>
>        \     \
>
>         d --> m (feature)
>
> 如果将feature分支合并提交到master分支：
>
> a --> b --> c --> n (master)
>
>       \     \   /
>
>        \     \ /
>
>         d --> m (feature)
>

7.其他：分支命名规范和提交命名规范


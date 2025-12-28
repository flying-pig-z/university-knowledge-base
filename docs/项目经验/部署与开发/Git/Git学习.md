# 一.Git简介
## 1.什么是Git?
Git 是一种分布式版本控制系统，用于跟踪代码或文件的更改历史，管理项目的不同版本。

## 2.为什么要使用Git
(1)版本控制

写代码写着写着忽然发现写错了，怎么办呢？

这时候Git的好处就来了，它帮你把以往的历史代码保留起来。一旦你今天把程序给玩坏了，它能倒回去。

(2)分支管理

假如我们的代码想要加两个新功能，相互不影响，分别交给A和B进行进行开发，但是这样的话版本该怎么控制呢？总不能A开发完了再交给B开发吧，这时候就需要我们的分支出场了。

我们可以把原来的代码一分为二，分别用git开一个分支，叫做feature(新功能)/a和feature/b，这样的话，每个人就可以只开发自己的那部分了，互不干扰，做到并行开发，在开发完成后，再通过git的合并操作，非常智能的将两个分支合并。

(3)团队协作

开发代码后进行提交，经过审核就可以进行合并。实现大家有条不紊的进行团队合作开发代码。

## 3.Git下载与安装
### [1]Windows
直接去官网下载：https://git-scm.com/download/win

下载完直接按安装引导一直Next就下载完成了

安装完成后在任意目录点击鼠标右键，如果能看到如右菜单则表示安装完成：

Git GUI Here:打开Git图形界面

Git Bash Here：打开Git命令行

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346488528-e118f6df-4eee-4936-9a8c-48e391425dde.png)

### [2]Linux
Linux直接使用包管理器安装就行了，这里以Ubantu为例：

```plain
sudo apt update
sudo apt install git
```

## 4.Git代码托管服务
### [1]常用的Git代码托管服务
国外：Github Gitlab

国内：Gitee Gitcode

### [2]案例：使用GitHub创建仓库
登录后，按照以下步骤创建一个新的仓库：

1.进入New Repository页面：

1. 在 GitHub 的主页上，点击左上角的New按钮。

2.填写仓库信息：在新建仓库的页面上，你需要填写以下信息：

+ **Repository name**：为你的仓库命名，这个名字在当前账户或组织下必须是唯一的。
+ **Description** (optional)：可以填写仓库的描述，说明这个仓库的用途。
+ **Visibility**：选择仓库的可见性。
    - **Public**：任何人都可以查看此仓库。
    - **Private**：只有你和你指定的协作者可以查看此仓库。
+ **Initialize this repository with a README**：勾选此选项，GitHub 会自动为你生成一个 README 文件，这个文件通常用来描述仓库的基本信息。
+ **Add .gitignore**：选择一个适合的模板，GitHub 会生成一个 `.gitignore` 文件，自动忽略某些不需要跟踪的文件。
+ **Choose a license**：选择一个开源许可协议，这个许可协议将决定别人如何使用你仓库中的代码。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346488603-442b4058-e8bf-43af-8846-0c796c0ecf6f.png)

4.创建仓库： 填写完上述信息后，点击页面底部的 **“Create repository”** 按钮，然后仓库就被创建成功了。

5.点击Code按钮就可以查看你Git的链接信息

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346488632-c626ec17-d1d0-498f-9abc-d08735120437.png)

# 二.Git配置
在使用前我们一般需要执行以下命令进行配置

```plain
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
# 这里的--global使得配置全局生效
```

配置你的用户名和email，你在每次commit到本地仓库或者push到远程仓库的时候的时候都会附带这些信息。

以便找到推送代码的对应的人和邮箱。

# 三.向远程仓库提交代码(非clone版)
暂时无法在飞书文档外展示此内容

## [1]创建一个文件夹，初始化其为本地仓库
创建文件夹，打开cmd，用下面命令初始化Git仓库

```plain
# 将repo初始化为一个本地版本库
git init
```

## [2]将要上传的文件添加到暂存区
```plain
git add filename.txt          # 添加单个文件
git add .                     # 添加当前目录下的所有文件
```

## [3]将暂存区的文件提交到本地仓库
通过git commit命令将已添加的文件和更改保存到本地仓库中。你需要为每次提交提供一个提交信息（commit message），以描述本次更改的内容。

```plain
git commit -m "Initial commit"   # 提交更改并附上说明
```

## [4]连接远程仓库
要向远程仓库提交代码，就需要指定远程仓库。

如果你想要将本地仓库与远程Git仓库（如GitHub、GitLab、Bitbucket等）关联起来，可以使用git remote add命令。

```plain
git remote add origin https://github.com/yourusername/your-repo.git # 这里的origin是远程仓库名
```

**一般这时候需要用各个平台的代码进行登录。**

**远程仓库可以有多个。**

取消绑定的远程仓库：

如果你已经将本地仓库绑定了远程仓库，那么怎么修改呢？

```plain
git remote add origin https://github.com/flying-pig-z/first_rep.git
# 如果使用了上面的命令，会报错--fatal: remote origin already exists.
git remote set-url origin https://github.com/flying-pig-z/first_rep.git
# 换个命令从新设置url
```

## [5]推送到远程仓库
连接远程仓库后，可以使用git push命令将本地提交推送到远程仓库。

如果是第一次推送的话执行下面这个命令：

```plain
git push -u origin master
```

这个命令表示要将本地master分支中的代码推送到 origin 仓库的 master 分支。

注意：推送到master分支，本地也要是master分支。

[1]-u（或 --set-upstream）：这个选项用于设置本地分支和远程分支的跟踪关系。执行这个命令后，本地目前的分支会与远程仓库 origin 上的 master 分支建立关联。

由于已经产生了关联，之后我们就可以使用 git push 或 git pull，而不需要每次都指定远程仓库和分支名，Git会自动知道要推送或拉取的对象。

```plain
# 使用了-u，我们可以不用指定远程仓库和分支名
git push
# 如果没有使用 -u，我们每次都要执行下面的命令
git push origin master
```

[2]origin：这是远程仓库的名字，就是我们前面用git remote add添加的。可以通过 git remote -v 来查看所有远程仓库的名称和对应的URL。

[3]master：这是要推送的分支的名字。master 是Git中一个常见的默认分支名(可能是main，也可能是master)。

# 四.向远程仓库提交代码(clone版)
大致步骤和上面差不多，但是克隆后的代码已经进行了初始化，并关联了仓库链接所在的远程仓库，所以关联远程仓库的步骤可以省略。

## [1]克隆远程仓库
使用 git clone 命令来克隆远程仓库。这会复制整个远程仓库的内容到你的本地机器上，并且会自动设置 origin 作为默认的远程仓库名称。

```plain
git clone <repository_url>
# 例如：git clone https://github.com/username/repository.git
```

克隆完成后，进入这个新创建的仓库目录：

```plain
cd repository
```

## [2]add commit push三部曲
和上面的流程一样：

```plain
git add . # 将更改添加到暂存区
git commit -m "Your commit message" # 提交你的更改
git push -u origin new-branch-name # 推送更改到远程仓库
```

# 五.Git status查看所在分支与文件状态
使用git status可以查看当前所在的分支以及文件的状态。

文件的状态可以分为以下四种：

**未跟踪（untrack）**：表示文件为新增加的，从来没有使用git add命令添加到暂存区。

**已修改（modified）**：之前使用过git add添加到暂存区，已经被跟踪。但是又修改了文件，并且还没再次使用git add保存到本地仓库中。

**已暂存（staged）**：表示文件的最新状态已经被保存到暂存区中。

**已提交（committed）**：表示文件已提交到本地仓库中。

# 六.Git log查看提交日志
## [1]基本用法
使用Git log可以用于输出每次提交的日志详情

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346488674-5617546c-f401-4f09-bcd5-6de337544a74.png)

## [2]加上-p参数查看提交内容差异
查看提交的内容差异 git log提供了-p参数，用于查看每次提交之间的内容差异，如下： git log -p 即可显示每次提交之间的变化：

```plain
commit 92f972422350ef603beb2740a78f57d0f98c1738 (HEAD -> master, origin/mast
Author: educoder <user@sample.com>
Date:   Sat Jan 6 15:57:52 2018 +0800
    第一次提交
diff --git a/7-1.sh b/7-1.sh
new file mode 100644
index 0000000..fa7cc9c
--- /dev/null
+++ b/7-1.sh
@@ -0,0 +1 @@
+###
\ No newline at end of file
diff --git a/7-2.sh b/7-2.sh
new file mode 100644
index 0000000..fa7cc9c
--- /dev/null
+++ b/7-2.sh
@@ -0,0 +1 @@
+###
\ No newline at end of file
diff --git a/7-3.sh b/7-3.sh
new file mode 100644
index 0000000..fa7cc9c
--- /dev/null
+++ b/7-3.sh
@@ -0,0 +1 @@
+###
\ No newline at end of file
diff --git a/7-4.sh b/7-4.sh
new file mode 100644
index 0000000..fa7cc9c
--- /dev/null
+++ b/7-4.sh
```

而如果想限制显示的范围，则可以再添加参数用于限定：

 git log -p -2

如上，则仅显示最近的两次更新。

如上所示，这一选项附带了每次commit的内容变化，这就为代码审查或者浏览某个搭档的修改内容，提供了很好的参考。

## [3]其他git log选项
（1）单词层面对比

Git提供了--word-diff选项，可以显示单词层面的差异。当需要在书籍、论文这种很大的文本文件上，进行对比的时候，这个功能就非常有用。

（2）显示简要的增改行数

Git提供了--stat选项，则可以仅显示增加或者减少了多少行。

（3）pretty选项

使用--pretty 选项选项，可以指定不同的显示属性，如oneline 将每个提交放在一行显示。 short，full 和 fuller 可以指定展示的信息的多少。

# 七.拉取代码
![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346488652-29dd2bac-ca7c-4a65-a91e-1ba6277699fd.png)

我们有时候push代码到远程仓库的时候会有上面的报错，这表明本地分支落后于远程分支，远程仓库中有一些提交记录在你的本地仓库中还没有。

为了防止远程分支的提交记录被覆盖，因此，在推送你的更改之前，应该先从远程仓库拉取最新的更改。

```plain
git pull -u origin main
# 从远程仓库 origin 的 main 分支获取最新的更改，
# 并将这些更改合并到你当前所在的分支中

git pull
```

Git pull其实是git fetch+git merge的组合：

```plain
git fetch origin
git merge origin/main
```

# 八.分支操作
## [1]什么是分支，分支有什么用
当初始化一个版本库并进行第一次提交的时候，如果没有创建指定分支，并切换到该分支，commit操作默认会在本地创建master分支，并将内容提交到master分支。一般我们会在版本库中维护一个master分支，如下图所示：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346489887-f24441f4-a033-407b-9cfb-30899b5e0e46.png)

我们在master分支上，进行了C1、C2、C3三次提交，且当前指针指向C3提交。

**一般情况下，我们只会将已经成熟的代码存放到master分支，而将正在开发的代码或者测试版的代码放到其他分支。**这时，我们就需要新建分支，以在该分支进行开发。如下图：

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346489997-f93d220f-e025-4544-91aa-f722b32f3cfe.png)

当我们在主分支进行了C2提交后，新建了develop分支，并在其上进行了两次提交。此时，工作区指针HEAD指向develop分支。

## [2]创建于切换分支
```plain
# 创建名为new_branch的新分支
git branch new_branch

# 切换到新的分支
git checkout new_branch

# 创建，并切换到了new_branch分支
git checkout -b new_branch
```

## [3]删除分支
```plain
# 删除develop分支
# 通过推送空分支到远程分支，实现删除。 
# 删除远程develop分支，其中origin为远程仓库名
git push origin :develop 

# 通过delete参数删除远程分支
# 删除远程develop分支,其中origin为远程主机名
git push origin --delete develop
```

## [4]分支合并--merge
在协作开发中，团队中每个人可能都只负责一个模块。所以，很有可能，你在开发过程中，需要用到别人所开发的功能。这个时候就需要将别人分支的内容，合并到你自己的分支；或者，develop分支或者master分支有更新，你也需要将它们的修改，合并到你的分支，以跟上产品开发进程；也有可能你为了解决一个bug，创建临时分支，完成开发后，需要将其合并到你的分支。

分支合并需要用到git merge命令

```plain
git merge develop
# 将develop分支合并到当前所在的分支
```

**Git的merge有快进合并和非快进合并(又叫做三方合并)和压缩合并三种。**

**默认就是快进合并和三方合并。如果可以直接快进合并，Git 会执行快进合并；否则，它会执行三方合并。**

**但是我们可以添加参数来操控Git的合并方式。**

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346490119-0305cd85-8dbc-4e5e-8dc5-27725854b126.png)

**接下来先来介绍一下三种合并方式。**

### (1)快进合并[fast-farward merge]
**使用条件：当主分支没有新的提交，特性分支直接基于主分支的最新提交。**

**快进合并会直接将合并分支的HEAD指针直接移动到被合并分支的最新提交，而不会创建新的合并提交。**

比如当需要将右侧分支（develop）合并到左侧分支（master）时，master分支会将其HEAD指针，直接指向develop分支的最新提交。

快进合并不会创建一个额外的合并提交，提交历史看起来像是主分支直接“快进”到了特性分支的最新状态。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346489959-173d94e6-4d4b-4895-922b-265613c49f25.png)

假设main分支的状态如下：

```plain
A --- B  (main)
       \
        C --- D (feature)
```

此时如果执行 git merge feature，由于 main 分支上没有额外的提交，Git 会直接将 main 的 HEAD 快进到D，历史会变为：

```plain
A --- B --- C --- D (main, feature)
```

**这是一个快进合并，没有产生新的合并提交。**

但是需要注意的是：如果主分支有特性分支之外其他提交的时候，这次快进提交会报错。

比如下面这种情况：

```plain
主分支:       A --- B --- C
               \ 
特性分支:       D --- E
```

### (2)三方合并
**适用条件：**当主分支和特性分支都各自有新的提交，无法直接快进合并时。比如上面的情况。

**行为**：

+ 三方合并会创建一个新的合并提交，该提交有两个父提交，一个来自主分支，另一个来自特性分支。它使用共同祖先（即两个分支分叉点的提交）来计算合并的最终状态。
+ 合并后，Git 会保留两个分支的历史，创建一个新的合并提交点，清楚地显示分支是如何合并的。
+ 新的合并提交默认格式是

```plain
Merge branch '被合并分支名称' into '合并分支名称'
```

**示例**：

假设main分支和feature分支各自都有新的提交：

```plain
A --- B --- C (main)
       \
        D --- E (feature)
```

此时执行 git merge feature，因为 main 和 feature 都有额外的提交，Git 将执行三方合并，生成一个新的合并提交 F：

```plain
A --- B --- C --- F (main)
       \       /
        D --- E (feature)
```

在这种情况下，F 是一个三方合并提交，它有两个父提交，分别是 C 和 E。

### (3)压缩合并
如果你使用三方合并后看到"Merge branch..." 的提交信息有点烦，合并的分支树也看着有点烦，那么你可以使用--squash去简化提交历史。

**git merge --squash 是一种合并策略，它会将要合并分支上的所有提交压缩成一个新的提交，然后合并到主分支，而且不会自动创建合并提交记录。**

假设有以下分支结构：

```plain
A --- B --- C (main)
       \
        D --- E (feature)
```

当你在主分支上运行git merge --squash feature时，Git 会将D, E的变更压缩成一个整体应用到主分支上，并且不会有提交信息，也不会有新的合并关系。

结果如下：

```plain
A --- B --- C --- F (main)
       \       
        D --- E (feature)
```

其中，F是由特性分支上的所有变更压缩而成的提交。

**特点：**

1. 压缩提交：特性分支上的所有提交将压缩成一个提交，合并后主分支上只有一个新的提交点。
2. 不创建合并提交 and 不记录合并历史：它不会像普通的三方合并那样创建合并的提交，合并分支也不会显示与被合并分支的合并关系。
3. **手动提交：使用 **`**--squash**`** 后，Git 会将变更放入暂存区（staging area），你需要手动使用 **`**git commit**`** 命令提交这些变更。**

```plain
# 切换到主分支
git checkout main

# 合并特性分支，并压缩所有提交为一个提交
git merge --squash feature

# 手动提交
git commit -m "Merge feature branch with squash"
```

### 常见合并选项
![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346490120-1b0b8c50-536e-4619-9120-1dc1d711364d.png)

+ --no-ff：强制使用合并提交（也就是三方合并，不管是不是符合快进条件，即在创建新分支后，主分支没有新的提交）
+ --ff-noly：仅在符合快进合并的条件的时候进行快进合并，如果不符合就不进行合并
+ --squash：压缩合并
+ -m：指定合并提交（三方合并）的消息

三方合并都会有一个默认的提交消息，默认提交信息是如下的格式：

```plain
Merge branch 'feature' into 'main'
```

如果的话你团队要求使用merge: {简短描述}这种格式，那就可以使用-m对提交信息进行修改

+ --no-commit：不提交合并结果 

此选项会执行合并操作，但不会立即提交合并的结果。它会将合并的更改放入暂存区，之后你可以手动审查和修改这些更改，然后再提交。

如果希望在合并之前检查或修改合并的内容时，可以使用这个选项。

+ 如果两个没有共同提交的分支合并会报错，那么就用下面的关键字：

```plain
--allow-unrelated-histories
```

## [5]分支变基--rebase
### (1)什么是变基
git rebase 是一种将特性分支的提交重新应用到主分支上的技术，它可以让你“重新整理”分支历史，使得历史看起来更线性、更清晰。

**与 git merge 不同，rebase 不会产生新的合并提交，而是将特性分支的提交“重放”到主分支的最新提交之上。相比于merge操作，使用rebase主要会使分支树更为清晰、干净。**

**注：合并冲突是合并冲突，和使用merge和rebase没有关系。**

**我们一般在feature分支上执行git rebase。**

**具体情景：**

假设你的当前分支情况如下：

```plain
A --- B --- C  (main)
       \
        D --- E  (feature)
```

**Rebase 过程**

执行 git rebase main 时，feature 分支的 D 和 E 提交会被重新应用到 main 分支的最新提交（C）之后。

具体步骤如下： 1. 寻找共同祖先：Git 会找到 feature 分支和 main 分支的共同祖先（提交B）。 2. 然后，它会将 feature 分支上的 D 和 E 提交“摘下”。 3. 接着，它会将 main 分支最新的提交（C）应用到 feature 分支。 4. 最后，它会重新将 D 和 E 提交应用到 C 之后。

最后结果如下：

```plain
A --- B --- C  (main)
A --- B --- C --- D' --- E'  (feature)
```

**注意**

D' 和 E' 是经过重放后的提交，理论上内容相同，但它们的哈希值与原始的 D 和 E 提交不同，因为它们的基底提交不同（现在基于 C 而不是 B）。

你在 feature 分支上执行 git rebase main 后的结果就是将 feature 分支的变更（D 和 E）基于 main 最新的提交历史重新应用。

**Git rebase后我们可以直接Git merge直接快进式合并到主分支。**

### (2)rebase操作
**基本操作**

rebase的基本操作是将某个分支的修改到指定分支，其命令格式为：

```plain
git rebase 基分支 源分支
# 其中‘基分支’是我们的新的‘基’，而‘源分支’就是需要进行变基操作的分支。
# 这样就能实现将源分支变基到基分支。具体使用示例如下：
git rebase master develop # 实现将develop变基到master分支

# 将当前分支变基到指定分支，则可以直接使用：
git rebase 基分支
```

**rebase操作产生冲突**

由于变基是将修改作用到一个不同的版本上，因此很可能在rebase的过程中出现冲突。和merge一次性合并所有冲突不同的是，**rebase的冲突是一个一个解决的**。

在解决rebase冲突的过程中，当解决完一个冲突的时候，使用如下命令后，才会出现下一个冲突：

```plain
git add -u 
git rebase --continue
```

冲突全部解决完后，rebase操作就完成了。

**撤销rebase操作**

如果在解决冲突的过程中，想放弃rebase操作，则可以使用如下命令撤销rebase操作：

```plain
git rebase --abort
```

这样就能退出rebase，并回退到rebase前的状态。

### (3)rebase和merge
前面说过rebase不产生新的分支提交，会使得分支树更为清晰、干净。

Git rebase虽然，但是它会修改之前的历史提交。

所以如果是涉及到公共分支之间的合并，用git merge比较好。

如果是操作个人分支，则可以使用git rebase。

# 九. 撤销操作
## [1]版本回退（撤销commit提交）
回退commit操作，不仅仅是

### (1)git revert实现版本回退
**git revert撤销提交时，会保留所撤销的提交的记录和历史，并将撤销操作做为一次新的提交。**即提交一个新的版本，将需要revert的版本的内容再反向修改回去，**版本会递增，不影响之前提交的内容**。

其具体的使用方法如下：

```plain
git revert HEAD          # 撤销当前提交
git revert HEAD^         # 撤销前一次提交
git revert HEAD~1        # 撤销前一次提交
git revert HEAD~2        # 撤销前前一次提交
git revert commit     
# (比如：fa042ce57ebbe5b)撤销指定的版本，撤销也会作为一次提交进行保存
```

### (2)git reset实现版本回退
**git revert是用一次新的commit来回滚之前的commit，git reset是直接删除指定的commit；**

在回滚这一操作上看，效果差不多。但是，在日后继续merge以前的老版本时有区别。

因为git revert是用一次逆向的commit，“中和”之前的提交，因此日后合并老的branch时，导致这部分改变不会再次出现。

但是git reset是把某些commit在某个branch上删除，因而和老的branch再次merge时，这些被回滚的commit应该还会被引入；

**git reset 是把HEAD向后移动了一下，而git revert是HEAD继续前进，只是新的commit的内容和要revert的内容正好相反，能够抵消要被revert的内容。**

git reset用法如下：

```plain
git reset HEAD 
# 回退到当前提交
# 也可以回退单个文件：git reset HEAD 文件名
git reset HEAD^ 
# 回到前一次提交
git reset HEAD~1
# 回到前一次提交
git reset HEAD~2
# 回到前前一次提交
git reset commit 
# 比如：commit = fa042ce57ebbe5b，回到指定的版本，撤销也会作为一次提交进行保存。
```

**另外git reset也可以指定reset的模式：hard、soft、mixed、merged、keep。（默认模式是mixed）**

几种模式的具体使用方法如下：

```plain
#直接丢弃工作区和暂存区的修改
git reset --hard HEAD
#暂存区内容保留，工作区修改丢弃
git reset --mixed HEAD
#暂存区和工作区内容都保留
git reset --soft HEAD
```

注：git revert也有一些参数，可以去了解一下

## [2]撤销工作区已经修改但还未git add进暂存区的修改
如果只是工作区有了修改，则可以直接使用git checkout进行撤销，具体操作如下：

```plain
git chekcout -- hello 
# 将hello文件自上个commit之后，尚未add进暂存区的修改丢弃
```

**但是当将错误的文件add进暂存区后，使用git checkout无法将修改从暂存区中撤销，必须要先使用git reset将修改从暂存区中撤销。**

## [3]删除文件
删除文件需要用到的命令是git rm，且git rm有参数--cached。

```plain
git rm 文件路径 
# 删除暂存区或分支上的文件，同时工作区也不再需要这个文件了
git rm --cached 文件路径
# 当我们需要删除暂存区或分支上的文件，但本地又需要使用，
# 只是不希望这个文件被提交到版本库
```

# 十.Git标签
## [1]为什么要有Git标签
现在你已经成了项目负责人，由你负责发布版本，你需要在发布一个版本之前，给该版本对应的代码打上标签，以便于管理和标识。

在开发过程中，commit ID是一串无序的字符，它虽然能唯一标记一次代码提交，即一个版本。但是，它很难记忆和辨识。所以，为了给不同的版本起一个容易辨识的名字，我们可以给这次提交打上一个标签，用不同的标签来对应不同的版本。这样，就相当于给这次提交生成了一个快照。实际上，在为某次提交创建标签的时候，Git会为标签生成一个指针，以指向其对应的提交。然后，我们就可以通过标签找到对应的提交，这样对我们版本发布和代码审查都很有帮助。

![](https://cdn.nlark.com/yuque/0/2025/png/42768076/1736346490327-71503db8-4264-4f34-a76e-2c149de0a0a4.png)

如上图所示，我们为master分支上的三次提交，分别打上0.1、0.2、0.3三个标签。这样，当我们说0.1版本的时候，就对应了第一次提交的代码。这种方式大大降低了代码审查、团队交流及版本发布的复杂性。

## [2]查看标签
```plain
git tag # 查看标签
```

使用git tag能列出所有的标签，显示的标签按字母顺序排列，所以标签的先后并不表示重要程度的轻重。

如果标签过多，而你指向显示指定的某些标签，则可以加上-l参数使用正则表达式：

```plain
git tag -l 'v5.1.2.*'
```

## [3]创建标签
创建标签的命令格式为：

```plain
git tag 标签名 commitID
```

参数commitID标识了该标签对应的代码版本，如果不提供commitID，就默认为最近一次提交后的代码打标签。例如：

```plain
git tag v1.0 # 为最新一次提交后的代码打上v1.0的标签
git tag v1.0 7f8buir2 # 为指定的版本7f8buir2打上标签v1.0
```

## [4]标签的注释信息
如果需要像提交代码时增加提交日志那样，为每个标签添加说明信息，则需要使用：

```plain
git tag -a 标签名 -m "说明信息"
git tag -a v1.0 -m 'version 1.0' # 为此次打的标签，增加一个version 1.0的说明信息
```

在查看标签时，可以使用git show命令，查看某个标签的附注信息。例如：

```plain
git show v1.0
```

表示要查看标签v1.0对应的附注信息。

## [5]推送指定标签
当你为某个版本打上标签后，就需要将其分享给团队中其他成员，即要将其推送至远程版本库。

推送指定标签到远程仓库的Git命令如下：

```plain
git push 远程主机名 tag名
# 远程主机名为远程Git版本库对应的主机名，tag名为准备推送的标签名
git push origin v1.0 
# 案例：将v1.0标签推送到主机名为origin对应的远程仓库

# -------------------------------------------------------

git push 远程主机名 --tags # 推送全部标签
git push origin --tags # 案例：将全部标签推送至主机名为origin远程仓库
```

## [6]删除标签
```plain
git tag -d 标签名 # 删除本地tag
git tag -d v1.0 # 案例：删除v1.0标签

# ---------------

git push origin --delete tag 标签名 # 方法一：删除远程tag
git push origin :refs/tags/<tagname> 
# 方法二：即推送一个空的tag名到远程仓库，其中tagname指某个标签的名字。
```

# 十一.冲突处理
在团队协作开发过程中，可能你和团队中的其他成员，都修改了某个文件的某一部分内容，且其他成员已将该修改推送到了远程仓库。这样当你需要合并他的代码的时候，可能就会在内容上出现冲突，这个时候就需要你去解决这个冲突以完成合并。

## 1.冲突的产生
### [1]内容冲突
Git内容冲突产生的原因是，针对版本库中某个文件的某项内容，不同的操作对其做了不同的修改，以致于在合并不同的操作时发生矛盾。比如下面的例子：

我们在本地master分支，添加了文件hello，其内容如下：

```plain
Learning English is easy and simple
```

然后，我们由master分支切换到一个新的分支develop，并修改hello文件内容如下：

```plain
Learning English is easy & simple
```

随后将其提交到了本地develop分支。

我们又切换回master分支，并再次对hello内容进行了修改：

```plain
Learning English is easy or simple
```

这样，当我们将develop分支合并到master分支的时候，就会出现冲突提示如下：

```plain
Auto-merging hello
CONFLICT (content): Merge conflict in hello
Automatic merge failed; fix conflicts and then commit the result.
```

冲突出现的原因是，我们在develop分支和master分支上，都对hello文件的内容做了修改，这样当将develop合并到master时，Git就不确定究竟应该采用哪个修改。

### [2]树冲突
方法文件名修改造成的冲突，称为树冲突。比如，A用户把文件C改名为A，B用户把文件C改名为B，那么B合并这两个提交时，就会出现冲突：

```plain
CONFLICT (rename/rename): Rename "C"->"B" in branch "HEAD" rename
Automatic merge failed; fix conflicts and then commit the result.
```

此时如果使用git status查看版本库的状态，会得到如下提示信息：

```plain
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)
Unmerged paths:
  (use "git add/rm <file>..." as appropriate to mark resolution)
        added by them:   A
        added by us:     B
        both deleted:    C
no changes added to commit (use "git add" and/or "git commit -a")
```

树冲突产生的原因是，我们将同一文件名，在不同操作中，修改为不同的名字。

## 2.解决冲突
**简单说解决冲突最好的方法就是让它们不冲突(废话文学hhh，不过确实是这样)**

### [1]内容冲突
当产生内容冲突时，如果你打开冲突发生的文件，你会在冲突区域发现类似于下面的内容：

```plain
<<<<<<< HEAD
Learning English is easy or simple
=======
Learning English is easy & simple
>>>>>>> develop
```

这个就是我们上面所举的内容冲突的例子，冲突文件的内容。从中可以看到<<<<<<< HEAD与=======包括的是我们当前分支的内容，而=======和>>>>>>> develop之间的则是需要合并过来的内容，为了解决冲突我们可以手动解决这些冲突，也可以使用图形化工具帮助解决。如果以手动方式解决，我们可以编辑冲突区域内容为我们想要的内容，比如将其修改成如下内容：

```plain
Learning English is easy and simple
```

然后再执行git add和git commit操作提交，这样就能将冲突解决了。

即解决冲突的一般过程为：

1.手动编辑冲突区域；

2.执行git add，将编辑提交到暂存区；

3.执行git commit，将编辑提交到本地仓库以解决冲突。

### [2]树冲突
解决树冲突时，对于上面示例中的树冲突，如果最终决定采用文件B，我们可以采用如下方式解决：

```plain
git rm A
git rm C
git add B
git commit
```

即从本地仓库中删除A和C文件，然后再添加B文件并最终提交。

# 十二.强制操作
如果远程版本库中的某个分支已经无法使用，需要强制覆盖将其更新，或者你的本地代码已经完全不能用，而需要用远程版本库中的某个分支进行覆盖时，你就需要强制操作。

又或者冲突的话你懒得两头都修改，就用强制操作。

## 1.强制操作的分类
使用最频繁的强制操作，主要在以下几个方面：

强制推送 如果远程的某个分支的内容需要被覆盖，这个时候就需要你进行强制推送，使用本地内容去覆盖该分支。

强制合并 如果本地分支的内容需要被远程内容覆盖，这个时候就需要强制合并远程分支内容到本地。

强制删除 如果你需要强制删除版本库、暂存区或者工作区的内容时，就需要强制删除。比如我们之前介绍的checkout，就可以使用-f参数，强制丢弃本地修改。

## 2.强制操作方法
+ 强制推送 

强制推送和普通推送的区别，就在于在末尾加上了-f参数，即：

```plain
git push 远程主机名 本地分支名：远程分支名 -f
```

具体使用方法如下：

```plain
#将本地分支强制推送到远程主机origin的master分支
git push origin master:master -f
```

+ 强制合并 

强制合并和普通合并的区别，也是其在末尾加上了-f参数，即： 

```plain
git pull 远程主机名 远程分支名：本地分支名 -f
```

具体使用方法示例如下：

```plain
#将远程master分支强制合并到本地master分支
git pull origin master:master -f
```

# 十三.忽略文件--.gitignore
如果你在本地版本库里，放入了仅供本地测试用的文件，但是你并不想将其推送到远程仓库，而且不想每次都被提醒你本地有未提交文件的话，就需要用到Git忽略文件提醒的功能。

在Git工作区的根目录下，有一个特殊的.gitignore文件，把要忽略的文件名或者文件名的通配符填进去，然后将.gitignore提交到本地仓库，这样Git就会在你添加或者提交时，自动忽略这些文件。

如果我们需要自己定义忽略哪些文件，就需要将其添加到.gitignore文件中去。你可以使用文件的全称，或者使用正则匹配的通配符。如下所示：

```plain
# 忽略指定文件
HelloWrold.class
# 忽略指定文件夹
bin/
bin/gen/
# 忽略.class的所有文件
*.class
# 忽略名称中末尾为ignore的文件夹
*ignore/
# 忽略名称中间包含ignore的文件夹
*ignore*/
```

# 十四.远程合并分支（使用Git merge）
**简单说思路就是在本地拉取两个分支先进行合并，然后将合并后的本地分支再推送到远程分支。**

这里不适合用git rebase，因为git rebase会修改之前的会修改既有的 commit 历史，不适合多人使用的分支合并。

## 1.为什么要进行分支合并？
在软件开发中，通常会在版本库中创建多个不同的分支进行开发。例如，最基本的可以有一个测试版分支和一个正式版分支，其中测试版分支用来完成最新功能代码的开发与测试，正式版则用于管理即将发布的版本。

如果某个版本通过了测试，就需要将其推到正式产品线上去。将测试版推送到正式版的一个做法，就是将远程仓库测试版的分支代码，合并到正式版的分支代码中去，这就对应着远程分支合并的操作。

## 2.具体步骤
合并远程分支的一般步骤是：

```plain
第一步，分别获取远程分支内容到本地；
第二步，在本地将两个分支合并；
第三步，将合并后的本地分支推送到远程分支，完成合并。
```

具体的，以将远程develop分支合并到远程master分支为例，操作过程如下：

获取远程develop分支到本地分支（如develop分支）。

如果本地已经有分支对应远程develop分支，则可以直接在该分支上执行pull操作或者fetch/merge操作，以获取远程最新内容。 否则，可以新建分支跟踪远程develop分支，并获取最新内容到本地；

切换到master分支，并获取远程master分支的最新内容到本地；

将本地develop分支合并到本地master分支；

将本地master分支推送到远程master分支。

以合并远程develop分支到远程master分支为例，其具体操作步骤如下：

```plain
# 切换到develop分支
git checkout develop
# 获取远程develop分支的内容到本地
git pull origin develop:develop
# 切换到master分支
git checkout master
# 拉取远程master分支内容到本地
git pull origin master
# 合并本地develop分支到master分支
git merge develop
# 将合并后的分支推送到远程master分支
git push origin master:master
```

# 十五.Git储藏
## 1.为什么要储藏
在开发过程中，当你的开发分支处于一个比较杂乱的状态，而你想转到其他分支上进行另外一些工作。但是，你不想提交进行了一半的工作，也不想将其撤销，这时就可以使用储藏操作。当你完成工作之后，再次回到该分支，可以恢复储藏的内容。然后，就会将之前保存的内容，再次恢复到工作区，就能继续进行开发。

## 2.储藏的概念
“储藏”可以获取你工作目录的中间状态（包括修改过的被追踪的文件和已经暂存的变更），并将其保存到一个未完结变更的堆栈中，而且随时可以重新应用。当你不想提交，也不想丢弃当前工作区中的内容，而想切换到其他分支的时候，可以使用储藏命令先暂存工作区中的内容。然后，再回到当前分支的时候，将储藏起来的内容，恢复到工作区之后，即可恢复之前的工作。

## 3.储藏的基本操作
储藏分为保存和应用两个部分。保存就是将当前工作区的内容保存到一个栈中，而应用就是重新应用被保存的工作。

### [1]保存
保存用到的命令是**git stash**，只需在当前分支执行此命令，即可将当前工作区的内容保存起来。如你在本地版本库创建了helloGit文件，此时查看工作区状态可以得到如下所示提示：

```plain
On branch master
Unt\fracked files:
  (use "git add <file>..." to include in what will be committed)
        helloGit
nothing added to commit but unt\fracked files present (use "git add" to t\frack)
```

当你执行git stash命令，将工作区保存起来之后，再次查看可以得到如下提示：

```plain
On branch master
nothing to commit, working tree clean
```

此时已经将工作区内容保存了起来，所以才会提示工作区是干净（clean）的。

### [2]重新应用
当你需要再次应用被保存的内容的时候，只需执行**git stash apply**即可。

因为可能执行了多次保存，所以你需要查看已经保存起来的内容有哪些。查看已经保存的工作的命令如下：

```plain
git stash list

# 会得到类似于如下输出
# stash@{0}: WIP on master: bguebge add helloGit1
# stash@{1}: WIP on master: 7gder34 add helloGit2
# stash@{2}: WIP on master: 3frfg4g add helloGit3
# 如上所示，可以得知一共有三个保存。
```

使用git stash apply应用被报错的内容：

```plain
# 如果要应用指定的储藏，则可以使用命令：
git stash apply 储藏标识
# 这里的储藏标识就是git stash list中显示的类似于stash@{0}的字符串。如：
git stash apply stash@{2}
# 这样就重新应用了第二次储藏。如果不加储藏标识，就默认应用最近的储藏：
git stash apply
# 上述命令就重新应用了最近的一次储藏。
```

# 十六.命令配置别名
在操作Git的过程中，我们经常需要手动敲入类似于git status或git checkout等命令。而status和checkout这些单词较长，每次都要完整敲入的话，不仅浪费时间，而且还容易输错。如果可以为命令设置简写的话，比如以git st来代替git status，则会使操作变得更加简单方便。实际上，Git允许我们为git命令设置别名，以达到简化操作的目的。

+ 设置别名

需要使用的命令是git config --global alias，其具体使用方法示例如下：

```plain
#为status设置别名st
git config --global alias.st status
#为checkout设置别名co
$ git config --global alias.co checkout
#为commit设置别名ci
$ git config --global alias.ci commit
#为branch设置别名br
$ git config --global alias.br branch
```

需要指出的是--global参数是一个全局参数，即设置的这些别名可以在这台主机的所有Git仓库下使用。如果不加这个参数，则只对当前的仓库起作用。

+ 删除别名

如果需要删除已经设置的别名的时候，则需要执行以下步骤：

删除所有别名:

```plain
git config [--global] --remove-section alias
```

其中，--global是可选参数，加上这个参数也将本主机所有git仓库下的别名都删除，不加这个参数则仅删除本仓库下的别名。

删除指定别名：

```plain
git config [--global] --unset alias.你的别名
```

同样的，--global也是一个全局参数。如果要删除本主机所有仓库下的st别名，则可以执行以下命令：

```plain
git config --global --unset alias.st
```

+ 查看别名

如果要查看当前主机已经设置了哪些别名，则可以执行以下命令：

```plain
git config --list | grep alias
# 会得到类似于alias.st=status的信息，这就是说系统当前已经为status设置了别名st。
```

# 十七.搭建Git服务器
虽然有提供托管代码服务的公共平台，但是对一部分开发团队来说，为了不泄露项目源代码、节省费用及为项目提供更好的安全保护，往往需要搭建私有Git服务器用做远程仓库。Git服务器为团队的开发者们，提供了协作开发平台，开发者可以基于私有的Git服务器进行项目开发。

Git服务器必须搭建在Linux系统下，因此必须准备一台运行Linux系统的主机。

## 具体步骤
TODO

# 十八.应用
## 1.提交前要先git pull一下
记得git push前要先git pull一下拉取代码，因为可能分支其他人已经提交了。

## 2.Merge remote-tracking branch ‘origin/master‘
如果我们在git pull之前已经使用git commit进行了提交，git pull的时候就会发生三方合并，从而产生如上的合并信息。

怎么避免上面这个合并信息的产生了。

**我们可以撤销git commit，先git pull。**

**也可以使用git pull --rebase（还可以还可以使用压缩提交，但是一般不会用哈哈哈）**

**还可以设置自动跟踪远程分支，可以使用下面的命令设置：**

```plain
git branch --set-upstream-to=origin/master master
# 这将确保本地 master 分支与远程 origin/master 进行关联。
```


<meta name="referrer" content="no-referrer"/>

## 分支策略
+ master/main：最稳定的主分支，只能用于生产发布
+ develop：开发主分支，用于日常开发集成
+ release：预发布分支，用于版本发布前的测试和准备
+ hotfix：紧急修复分支，用于生产环境问题修复

## 各个流程
### 功能开发流程
从develop分支创建feature分支：`feature/功能描述`，完成后提交Pull Request到develop分支，经过代码评审后合并，合并后删除feature分支。

### 提交规范
commit message格式：

```plain
<type>(<scope>): <subject>

<body>

<footer>
```

> type类型：
>
> + feat: 新功能
> + fix: 修复bug
> + docs: 文档变更
> + style: 代码格式调整
> + refactor: 重构代码
> + test: 添加测试
> + chore: 构建过程或辅助工具的变动
>

### 版本发布流程
从develop分支创建release分支，在release分支上进行测试和bug修复。

测试通过后合并到master和develop，在master上打tag标记版本号。

### 工作流程规范
每天早上先pull最新代码，经常commit保存工作进度，提交前先进行代码自测，重要功能创建单独分支开发，定期删除已合并的过期分支。

> 1. Feature 分支合并到 Develop 分支： 推荐使用 `git merge --no-ff` (no-fast-forward)方式
> 2. Release 分支合并到 Master 分支： 通常也使用 `git merge --no-ff`
>

## 代码评审要求
所有代码变更必须经过评审

评审关注点：

+ 代码质量和规范
+ 业务逻辑正确性
+ 性能影响
+ 安全隐患

## 合理使用git rebase
#### 拉取最新代码时使用 rebase
```bash
# 不推荐
git pull origin develop

# 推荐
git pull --rebase origin develop
```

原因：避免产生无意义的 merge commit，保持提交历史的清晰。

#### feature 分支开发时与主分支同步
```bash
# 在 feature 分支上
git checkout feature/xxx
git rebase develop
```

好处：保持 feature 分支与主分支代码同步。提前解决冲突，避免合并时出现大量冲突，保持提交历史的线性。

#### 合并多个 commit
```bash
# 合并最近的 3 个 commit
git rebase -i HEAD~3
```

适用场景：

+ 合并开发过程中的临时提交
+ 整理提交信息使之更有意义
+ 在提交 Pull Request 前整理提交历史

#### 不应该使用 rebase 的场景
+ 已经推送到远程的公共分支（如 develop、master）
+ 多人协作的 feature 分支，除非团队达成共识
+ 包含 merge commit 的分支

#### 使用 rebase 的注意事项
+ 一定要理解 rebase 会改写提交历史
+ rebase 前先备份当前分支
+ 如果 rebase 过程中出现冲突，解决后使用：

```bash
git add .
git rebase --continue
```

#### rebase 的最佳实践
+ 每天早上先与主分支同步

```bash
git checkout develop
git pull
git checkout feature/xxx
git rebase develop
```

+ 提交 PR 前整理提交历史

```bash
# 整理最近的提交
git rebase -i HEAD~n

# 常用的 rebase 命令
pick：保留该commit
squash：将该commit合并到前一个commit
fixup：将该commit合并到前一个commit，但不保留该commit的注释信息
drop：删除该commit
```

#### 处理 rebase 冲突的建议：
+ 使用好的 merge 工具（如 VSCode、Beyond Compare）
+ 遇到复杂冲突及时寻求同事帮助
+ 如果 rebase 过程太复杂，可以考虑放弃使用 merge 方式

通过合理使用 rebase，可以:

+ 保持代码提交历史的清晰
+ 减少无意义的 merge commit
+ 提高代码审查的效率
+ 使项目历史更加整洁易读

记住：rebase 是一个强大但危险的命令，在使用时要谨慎，确保理解其影响再操作。

## 其他重要规范
+ 禁止强制push主分支
+ 保持commit历史清晰
+ 重要分支开启保护
+ 定期清理无用分支




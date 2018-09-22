## 1.git是什么？

是一个分布式**版本控制**软件

## 2.git的作用是什么？

版本控制 团队协作

## 3.git的优势是什么？

分布式管理

如何下载git：百度搜索git-scm

工作区、暂存区、本地仓库、远程仓库

## git命令：

#### git本地操作

**git --help**	调出帮助文档

**git +命令--help**	查看某个具体命令的帮助文档

**git init**	生成一个空的本地仓库

**git add**	将文件添加到暂存区

初次commit之前，需要配置用户邮箱及用户名，使用以下命令：

 git config --global user.email "you@example.com"
 git config --global user.name "Your Name"

**git commit** 将暂存区提交到本地仓库

#### git远程操作

git remote	用于管理远程仓库

git push -u origin master	向名字为origin的仓库的master的分支提交变更

git fetch	拉取远程仓库的变更到本地仓库

git merge origin/master	将远程的变更合并到本地仓库的master分支


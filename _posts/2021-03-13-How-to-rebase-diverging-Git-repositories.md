---
layout: post
author: fubar
title: "How to rebase diverging Git repositories?"
tag: programming
tool: git
excerpt: "For the current homepage, I was pushing commits to the **remote** repository on GitHub from two **local** repositories. The older local repository was managed by `Git for windows` client. The newer local repository is managed by `GitHub Desktop`. The commit history on both the local history has diverged. The task at hand is to bring parity with both these repositories. We will use rebase for the same."
date: 13th March, 2021
---

# GitHub remote repository

Let us call this remote repository `R.branch`. To check which remote repository, `L.branch.1` is connected to,

```
$ git remote --verbose
origin  https://github.com/Baalkikhaal/Baalkikhaal.github.io.git (fetch)
origin  https://github.com/Baalkikhaal/Baalkikhaal.github.io.git (push)
```
# Git for windows local repository

Let us call this repository `L.branch.1`. Its current status is

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   _posts/2020-05-24-spintronics.md
        modified:   _posts/2020-06-30-Reviews-of-spintronics.md
        modified:   _posts/2020-09-22-Python-Style-Guide.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        _posts/2020-08-13-Consistent-use-of-units-in-magnetism.md
        _posts/2020-08-14-Questions-and-confusions-pertaining-to-spintronics.md
        _posts/2020-08-18-Galvano-magnetic-effects-in-spin-transport.md
        _posts/2020-10-08-Find-keyword-in-function-arguments.md
        _posts/2020-10-10-Code-refactoring.md
        _posts/2020-10-15-Inside-out-DAQ-card-.md
        assets/images/Git/keep-calm-and-git-it-on.png
        assets/images/Python/keep-calm-and-code-in-python-19.png

no changes added to commit (use "git add" and/or "git commit -a")

```

Now lets fetch the commits added to `R.branch` since the last fetch.

```bash
$ git fetch origin
remote: Enumerating objects: 232, done.
remote: Counting objects: 100% (232/232), done.
remote: Compressing objects: 100% (134/134), done.
remote: Total 232 (delta 125), reused 202 (delta 97), pack-reused 0
Receiving objects: 100% (232/232), 2.82 MiB | 246.00 KiB/s, done.
Resolving deltas: 100% (125/125), completed with 25 local objects.
From https://github.com/Baalkikhaal/Baalkikhaal.github.io
   dc40025..91c3657  master     -> origin/master
 * [new branch]      dependabot/bundler/nokogiri-1.11.1 -> origin/dependabot/bundler/nokogiri-1.11.1
```

After committing the pending work on `L.branch.1` repository, its status reads

```bash
On branch master
Your branch and 'origin/master' have diverged,
and have 5 and 20 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

nothing to commit, working tree clean
```
After the fetch, the log reads

```bash
$ git log --oneline
dc40025 (HEAD -> master) how to design Python code and write-up on some built-in modules
be070f2 removed minimal theme from _config.yml
142134a Merge branch 'master' of https://github.com/Baalkikhaal/Baalkikhaal.github.io travis commits
bf8c6c4 corrected date of post 2020-10-05
f644b0a Set theme jekyll-theme-minimal
cff09b4 updated spintronics review articles
21be578 added travis CI
58592cc updated github-pages gem
f0790c2 enabled MathJax
6cc4db9 update link spintronics review
2fb13ba added liquid link tags
60ad1bf added markdown sources
dee58b9 gemfile configured for github pages
5de484f configured github pages
3226003 (tag: v1.0) yoga kshema sixth post
7c3fcea yoga kshema
9fee4b0 spintronics resources
5c8407f github markdown CSS style and post on HOWTO git PhD thesis
11f05bf Merge branch 'master' of https://github.com/Baalkikhaal/Baalkikhaal.github.io
b9e9079 added clickable SVG images for site navigation
```

Now checking the status, it is clear that `L.branch.1` is behind origin/master.

>It is to be noted that the comparison is done with `origin/master` branch also called `tracking` branch. This tracking branch resides on the local repository.

```bash
$ git status
On branch master
Your branch is behind 'origin/master' by 20 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   _posts/2020-05-24-spintronics.md
        modified:   _posts/2020-06-30-Reviews-of-spintronics.md
        modified:   _posts/2020-09-22-Python-Style-Guide.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        _posts/2020-08-13-Consistent-use-of-units-in-magnetism.md
        _posts/2020-08-14-Questions-and-confusions-pertaining-to-spintronics.md
        _posts/2020-08-18-Galvano-magnetic-effects-in-spin-transport.md
        _posts/2020-10-08-Find-keyword-in-function-arguments.md
        _posts/2020-10-10-Code-refactoring.md
        _posts/2020-10-15-Inside-out-DAQ-card-.md
        assets/images/Git/keep-calm-and-git-it-on.png
        assets/images/Python/keep-calm-and-code-in-python-19.png

no changes added to commit (use "git add" and/or "git commit -a")
```

(optional) To see the log of the `tracking` branch, we can [checkout this branch][1] like any other branch. However there is a catch as shown below

```bash
$ git checkout origin/master
Note: switching to 'origin/master'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 91c3657 (front end) added dark vs light theme switcher

```

So the `tracking` branch holds the commits of the `R.branch` branch as shown below. And our task is to translate these new commits to the `L.branch.1` branch.

```bash
$ git log --oneline
91c3657 (HEAD, origin/master, origin/HEAD) (front end) added dark vs light theme switcher
71db43f post feynman learning technique
6fb0bb5 post cubic and quartic equation analytical solution
6ed916e post spyder IDE advanced features
f53ae5d post origin LabTalk script fundamentals
ed4bdfb post^ sysMain is the new superfetch
a8f7dce post windows services
b10a0c3 post^ corrected date of post
5f52e44 post^ update added figure
2e6bf1a post troubleshoot windows insider build update
2882a0b tool keys corrections
83c119f update css
ab5cad8 update posts with tool key in front matter
b549b73 updated config files
52235c1 resized post specific logo
6ad672f css files update
4f11d8b css files update
7e2dfb6 post linear regression
0ff6bc2 post f-strings
791b4c3 post timeit module
dc40025 how to design Python code and write-up on some built-in modules
be070f2 removed minimal theme from _config.yml
```

Before we continue with this translation, let us checkout to `L.branch.1` again. which reads

```bash
$ git checkout master
Previous HEAD position was 91c3657 (front end) added dark vs light theme switcher
Switched to branch 'master'
Your branch and 'origin/master' have diverged,
and have 5 and 20 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)
```

(optional ends)


# Rebase onto origin/master

[Rebasing][2] is a cleaner alternative to [merging][3].


Before initiating rebasing, it is important to commit the pending works on `L.branch.1` as inferred from below message

```
$ git rebase origin/master
error: cannot rebase: You have unstaged changes.
error: Please commit or stash them.
```

So let us commit the pending work. After committing the log reads

```bash
$ git log --oneline
dbbfd6c (HEAD -> master) add `tool` tags
afaaa9f post daq card working
504b9b1 post git rebase vs merge
922dae3 trade practices in Python
36e3fce trade practices in spintronics
dc40025 how to design Python code and write-up on some built-in modules
be070f2 removed minimal theme from _config.yml
142134a Merge branch 'master' of https://github.com/Baalkikhaal/Baalkikhaal.github.io travis commits
bf8c6c4 corrected date of post 2020-10-05
f644b0a Set theme jekyll-theme-minimal
cff09b4 updated spintronics review articles
21be578 added travis CI
58592cc updated github-pages gem
f0790c2 enabled MathJax
6cc4db9 update link spintronics review
2fb13ba added liquid link tags
60ad1bf added markdown sources
dee58b9 gemfile configured for github pages
5de484f configured github pages
3226003 (tag: v1.0) yoga kshema sixth post
7c3fcea yoga kshema
9fee4b0 spintronics resources
```

Also let us create a backup of `L.branch.1` called `L.branch.3` at a different location in the local system incase rebasing fails!! because there is a warning given in section `[The Perils of Rebasing][2]`

```
fubar@desktop-fubar MINGW64 /e/Databases/GitHub/BackupRepos
$ git clone /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io
Cloning into 'Baalkikhaal.github.io'...
done.

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/BackupRepos
$ ls
Baalkikhaal.github.io/

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/BackupRepos
$ cd Baalkikhaal.github.io/

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/BackupRepos/Baalkikhaal.github.io (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/BackupRepos/Baalkikhaal.github.io (master)
$ git remote --verbose
origin  E:/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (fetch)
origin  E:/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (push)

```

## Rebase commands

- Ensure we have checked out the branch we want to rebase.

`git checkout master`

- We want to rebase this branch onto `tracking` branch. To rebase onto this branch officially called the `origin/master` branch

`git rebase origin/master`

```
$ git rebase origin/master
error: could not apply 922dae3... trade practices in Python
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 922dae3... trade practices in Python
CONFLICT (file location): assets/images/Python/keep-calm-and-code-in-python-19.png added in 922dae3 (trade practices in Python) inside a directory that was renamed in HEAD, suggesting it should perhaps be moved to assets/images/tools/keep-calm-and-code-in-python-19.png.
Auto-merging _posts/2020-09-22-Python-Style-Guide.md

```

Lets check the status. Observe that we are on Step 2 out of 5.

```bash
fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 2/5)
$ git status
interactive rebase in progress; onto 91c3657
Last commands done (2 commands done):
   pick 36e3fce trade practices in spintronics
   pick 922dae3 trade practices in Python
Next commands to do (3 remaining commands):
   pick 504b9b1 post git rebase vs merge
   pick afaaa9f post daq card working
  (use "git rebase --edit-todo" to view and edit)
You are currently rebasing branch 'master' on '91c3657'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   _posts/2020-09-22-Python-Style-Guide.md
        new file:   _posts/2020-10-08-Find-keyword-in-function-arguments.md
        new file:   _posts/2020-10-10-Code-refactoring.md

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        added by them:   assets/images/tools/keep-calm-and-code-in-python-19.png

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   _posts/2020-10-08-Find-keyword-in-function-arguments.md
        modified:   _posts/2020-10-10-Code-refactoring.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        _posts/2020-10-15-Inside-out-DAQ-card-.md
        _posts/2021-03-13-Working-with-remote-git-repositories.md
```

I have use git rebase --skip

```bash
fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 2/5)
$ git rebase --skip
error: The following untracked working tree files would be overwritten by merge:
        _posts/2021-03-13-Working-with-remote-git-repositories.md
Please move or remove them before you merge.
Aborting
hint: Could not execute the todo command
hint:
hint:     pick 504b9b1d2524783a55d4efc2048a546f4b98c4c9 post git rebase vs merge
hint:
hint: It has been rescheduled; To edit the command before continuing, please
hint: edit the todo list first:
hint:
hint:     git rebase --edit-todo
hint:     git rebase --continue
Could not apply 504b9b1... post git rebase vs merge

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 3/5)
$ git rebase --skip
error: The following untracked working tree files would be overwritten by merge:
        _posts/2021-03-13-Working-with-remote-git-repositories.md
Please move or remove them before you merge.
Aborting
hint: Could not execute the todo command
hint:
hint:     pick 504b9b1d2524783a55d4efc2048a546f4b98c4c9 post git rebase vs merge
hint:
hint: It has been rescheduled; To edit the command before continuing, please
hint: edit the todo list first:
hint:
hint:     git rebase --edit-todo
hint:     git rebase --continue
Could not apply 504b9b1... post git rebase vs merge

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 4/6)
$ git status
interactive rebase in progress; onto 91c3657
Last commands done (4 commands done):
   pick 504b9b1 post git rebase vs merge
   pick 504b9b1 post git rebase vs merge
  (see more in file .git/rebase-merge/done)
Next commands to do (3 remaining commands):
   pick 504b9b1 post git rebase vs merge
   pick afaaa9f post daq card working
  (use "git rebase --edit-todo" to view and edit)
You are currently editing a commit while rebasing branch 'master' on '91c3657'.
  (use "git commit --amend" to amend the current commit)
  (use "git rebase --continue" once you are satisfied with your changes)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        _posts/2020-10-15-Inside-out-DAQ-card-.md
        _posts/2021-03-13-Working-with-remote-git-repositories.md

nothing added to commit but untracked files present (use "git add" to track)

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 4/6)
$ git add _posts/2021-03-13-Working-with-remote-git-repositories.md

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 4/6)
$ git rebase --continue
[detached HEAD a47e7ba] post git rebase vs merge
 1 file changed, 14 insertions(+)
 create mode 100644 _posts/2021-03-13-Working-with-remote-git-repositories.md
error: The following untracked working tree files would be overwritten by merge:
        _posts/2020-10-15-Inside-out-DAQ-card-.md
Please move or remove them before you merge.
Aborting
hint: Could not execute the todo command
hint:
hint:     pick afaaa9f9a2cc22236624054f6addae8d686585e4 post daq card working
hint:
hint: It has been rescheduled; To edit the command before continuing, please
hint: edit the todo list first:
hint:
hint:     git rebase --edit-todo
hint:     git rebase --continue
Could not apply afaaa9f... post daq card working

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 6/7)
$ git status
interactive rebase in progress; onto 91c3657
Last commands done (7 commands done):
   pick afaaa9f post daq card working
   pick 504b9b1 post git rebase vs merge
  (see more in file .git/rebase-merge/done)
Next commands to do (2 remaining commands):
   pick afaaa9f post daq card working
   pick dbbfd6c add `tool` tags
  (use "git rebase --edit-todo" to view and edit)
You are currently editing a commit while rebasing branch 'master' on '91c3657'.
  (use "git commit --amend" to amend the current commit)
  (use "git rebase --continue" once you are satisfied with your changes)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        _posts/2020-10-15-Inside-out-DAQ-card-.md

nothing added to commit but untracked files present (use "git add" to track)

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 6/7)
$ git add _posts/2020-10-15-Inside-out-DAQ-card-.md

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 6/7)
$ git rebase --continue
[detached HEAD 67e635d] post daq card working
 1 file changed, 14 insertions(+)
 create mode 100644 _posts/2020-10-15-Inside-out-DAQ-card-.md
dropping afaaa9f9a2cc22236624054f6addae8d686585e4 post daq card working -- patch contents already upstream
error: could not apply dbbfd6c... add `tool` tags
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply dbbfd6c... add `tool` tags
Auto-merging _posts/2020-10-11-Built-in-modules.md
CONFLICT (modify/delete): _posts/2020-10-10-Code-refactoring.md deleted in HEAD and modified in dbbfd6c (add `tool` tags). Version dbbfd6c (add `tool` tags) of _posts/2020-10-10-Code-refactoring.md left in tree.
CONFLICT (modify/delete): _posts/2020-10-08-Find-keyword-in-function-arguments.md deleted in HEAD and modified in dbbfd6c (add `tool` tags). Version dbbfd6c (add `tool` tags) of _posts/2020-10-08-Find-keyword-in-function-arguments.md left in tree.

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 9/9)
$ git status
interactive rebase in progress; onto 91c3657
Last commands done (9 commands done):
   pick afaaa9f post daq card working
   pick dbbfd6c add `tool` tags
  (see more in file .git/rebase-merge/done)
No commands remaining.
You are currently rebasing branch 'master' on '91c3657'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add/rm <file>..." as appropriate to mark resolution)
        deleted by us:   _posts/2020-10-08-Find-keyword-in-function-arguments.md
        deleted by us:   _posts/2020-10-10-Code-refactoring.md

no changes added to commit (use "git add" and/or "git commit -a")

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 9/9)
$ git add _posts/2020-10-08-Find-keyword-in-function-arguments.md

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 9/9)
$ git add _posts/2020-10-10-Code-refactoring.md

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master|REBASE 9/9)
$ git rebase --continue
[detached HEAD 8722317] add `tool` tags
 2 files changed, 36 insertions(+)
 create mode 100644 _posts/2020-10-08-Find-keyword-in-function-arguments.md
 create mode 100644 _posts/2020-10-10-Code-refactoring.md
Successfully rebased and updated refs/heads/master.

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 5 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/Baalkikhaal.github.io (master)
$ git log --oneline
8722317 (HEAD -> master) add `tool` tags
67e635d post daq card working
4b97530 post git rebase vs merge
a47e7ba post git rebase vs merge
1f955a3 trade practices in spintronics
91c3657 (origin/master, origin/HEAD) (front end) added dark vs light theme switcher
```

# GitHub Desktop local repository
Let us call this repository `L.branch.2`. Its current status is

[1]: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
[2]: https://git-scm.com/book/en/v2/Git-Branching-Rebasing
[3]: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merging
[4]:

---
layout: post
author: fubar
title: "How to Git your PhD thesis on GitHub"
tag: physics
tool: git
excerpt: "We will work with GitHub’s repository hosting service to have a remote repository for our PhD thesis"
date: 20th June, 2020
---

# Context

Git is a version control system usually used for software. However it can also be used for versioning any document set. We will see how git can be used to version a PhD thesis. Versioning a PhD thesis is not only useful as a backup option but also can give an overview of how the thesis gets shaped over the course of time. Also since thesis writing is a highly non linear phenomenon, git provides tools to track the non linear development. We will work with GitHub's repository hosting service to have a remote repository for our PhD thesis. It is a good idea to git your thesis as a **private repository**. GitHub private repository provides [unlimited storage](https://github.blog/2019-01-07-new-year-new-github/) as long as the file sizes do not exceed [100MB size limit](https://help.github.com/en/github/managing-large-files/what-is-my-disk-quota).

The following are the steps to have a Git repository for the PhD thesis
- [Setup Git on linux](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
- [Setup a private repository on GitHub](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository)
- [Clone the remote repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
- [Basic snapshotting workflow](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Basic-Snapshotting)
    - [Quick walkthrough](#basic-snapshotting-detailed-description)
    - [Detailed description](#basic-snapshotting-detailed-description)

General references on [Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control), [The Git Parable](https://tom.preston-werner.com/2009/05/19/the-git-parable.html), [Add an existing repository to GitHub](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line), [LaTeX template](https://drive.google.com/drive/folders/1dvkAsN0UHYe0sEJuwbrN9M7MunnZhYjM?usp=sharing)

---
# Setup a private repository on GitHub

Add a `.gitignore` file that tells git to exclude a set of files from version control. Set the `.gitignore` file type to `TeX`. Create a private repository.

![private-repository-on-GitHub](/assets/images/Git/GitHubPrivateRepository.png
)


# Clone the remote repository

Now that a remote repository is created on GitHub, we need to [clone it on a local computer](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github) to work with it. Get the URL of the remote repository and use `git clone <url to remote repo>`

    $ git clone https://github.com/Baalkikhaal/myTestThesis.git
    Cloning into 'myTestThesis'...
    remote: Enumerating objects: 4, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (4/4), done.

# Basic Snapshotting Quick walkthrough

Now that we have a local copy of the remote repository `myTestThesis` to work with, we will describe a typical [workflow for basic snapshotting](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Basic-Snapshotting) involving

1. Creating/modifying files of the repository - `nano newfile.tex`
1. staging files to git tracking system - `git add *`
1. committing files to commit history - `git commit -m "<my message>"`
1. pushing the commits to the remote repo - `git push origin master`
1. go to step 1

# Basic Snapshotting Detailed description

## Creating/modifying files of the repository

The local copy of the repository is created in `myTestThesis`. Now change into the directory and list the files including the hidden files

    $ cd myTestThesis/

    $ ls -al
    total 21
    drwxr-xr-x 1 fubar 197121    0 Jun 20 18:32 ./
    drwxr-xr-x 1 fubar 197121    0 Jun 20 18:32 ../
    drwxr-xr-x 1 fubar 197121    0 Jun 20 18:32 .git/
    -rw-r--r-- 1 fubar 197121 2960 Jun 20 18:32 .gitignore
    -rw-r--r-- 1 fubar 197121   45 Jun 20 18:32 README.md

The hidden folder `.git` holds all the information about the commit history of the repository. The hidden file `.gitignore` contains instructions to exclude files from getting versioned. A preliminary scan of the contents of `.gitignore` shows what kind of files are omitted, usually the `.aux` (auxiliary), `.log`, etc files generated during a typical LaTeX compilation. We do not want to version them as they are not part of the source code, they are output of compilation.

Copy the contents of the [LaTeX template](https://drive.google.com/drive/folders/1dvkAsN0UHYe0sEJuwbrN9M7MunnZhYjM?usp=sharing) to the local repository `myTestThesis`.

    $ cp -r /e/thesis/thesisTemplates/Latex_Thesis/. .

As new files are added to the local repository `myTestThesis`, they hold the status of **untracked files**. The status of every file is given the `git status` command

    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    Untracked files:
    (use "git add <file>..." to include in what will be committed)
           Abhishek_Thesis.pdf
           Abhishek_Thesis.tex
           Bibliography_Clean.bat
           IISc_Logo.pdf
           figures/
           ociamthesis.cls
           oxthesis.cls
           refs.bib
           text/
           ~$apter4_Notes.docx

The  generated pdf files after LaTeX compilation also need to be excluded from tracking as pdf files are binary files. Binary files are [not suitable for gitting](https://stackoverflow.com/questions/17772048/when-should-pdf-files-be-tracked-in-a-git-repository-and-when-not). Included generated pdf files can *bloat* the repo.

To avoid this modify the `.gitignore` file to exclude specifically the pdf file
Change the line

    # Generated if empty string is given at "Please type another file name for out>
    .pdf

to the following line

    ## Generated if empty string is given at "Please type another file name for out>
    Abhishek_Thesis.pdf

After this modification, if you check the status of the repository again using `git status`, you will observe that the main pdf file is ignored from tracking, however the `.gitignore` file shows up as **modified**. This is because the `.gitignore` file was already being tracked by `git` as we cloned it from the remote repository. Now that we modified it, the status of the `.gitignore` file has changed to modified.

> Note that git is aware of other pdf files like `IISc_Logo.pdf `. This is intended as some of our figures are .pdf files and they are not likely to change. If you want to completely all pdf files, add `*.pdf` line in the `.gitignore` file.

    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   .gitignore

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            Abhishek_Thesis.tex
            Bibliography_Clean.bat
            IISc_Logo.pdf
            figures/
            ociamthesis.cls
            oxthesis.cls
            refs.bib
            text/
            ~$apter4_Notes.docx

    no changes added to commit (use "git add" and/or "git commit -a")

## Staging the files to git tracking system

The **untracked** and **modified** files need to be staged. To stage the files use `git add <filename>` for each file or `git add *` for staging all the files at one go.

    $ git add *
    The following paths are ignored by one of your .gitignore files:
    Abhishek_Thesis.aux
    Abhishek_Thesis.bbl
    Abhishek_Thesis.blg
    Abhishek_Thesis.brf
    Abhishek_Thesis.log
    Abhishek_Thesis.pdf
    Abhishek_Thesis.synctex.gz
    Abhishek_Thesis.toc
    abstract.aux
    refs.bib.bak
    Use -f if you really want to add them.

Check the status of the repository and see if the files are staged

    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   Abhishek_Thesis.tex
            new file:   Bibliography_Clean.bat
            new file:   IISc_Logo.pdf
            ...
            ...
            new file:   text/originality.tex
            new file:   ~$apter4_Notes.docx
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   .gitignore

You will see that `.gitignore` is not staged for commit. This is because `git add` command does not add hidden files. You need to manually add the file

    $git add .gitignore

## Committing the files to commit history

Now that all the files are **staged**, they can be **committed** to the commit history using `git commit -m "<A message>"`. A message is needed to summarize what the commit is all about

    $ git commit -m "my first thesis commit"
    [master e42db57] my first thesis commit
    21 files changed, 1171 insertions(+), 1 deletion(-)

### Check the log of the commit history

`git log` gives the summary of the commit history. To check if the commit has been logged into the commit history. The log is a list of 7 character hexadecimal SHA strings (the actual length is 40 character but with `--oneline` a shortened version is printed) and the commit message

    $ git log --oneline
    e42db57 (HEAD -> master) my first thesis commit
    fbcbcde (origin/master, origin/HEAD) Initial commit

## Push the commit to the remote repository

The above commit has updated the commit history of the local repository. However we need to update the commit history of the remote repository as well. This is called **pushing** the commit to the remote repository. The remote repository is called the **origin** and the branch on which the commits are adding up is the **master** branch. To push a commit, the branches on the local and remote need to be same. To push the commit, we use `git push` command

    $ git push origin master
    Enumerating objects: 29, done.
    Counting objects: 100% (29/29), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (26/26), done.
    Writing objects: 100% (27/27), 1.11 MiB | 888.00 KiB/s, done.
    Total 27 (delta 2), reused 0 (delta 0)
    remote: Resolving deltas: 100% (2/2), completed with 1 local object.
    To https://github.com/Baalkikhaal/myTestThesis.git
       fbcbcde..e42db57  master -> master

You can check  if the commit has been pushed to the remote repository either by running `git status` at the local repository or checking at GitHub if the files have been committed

    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean

## Iterate over the workflow
Repeat the workflow when you want to add content to the remote repository

# Summary

In summary we have used many git commands in the process of git workflow to write the PhD thesis. Let us list the commands

- `git clone`
- `git add`
- `git commit`
- `git push`
- `git status`
- `git log`


# References

- In addition to the above mentioned git commands, some other commands are also useful like `git diff`, `git rm`. More on these at [Git's basic snapshotting commands](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Basic-Snapshotting)

- In the current article, we assumed `.Tex` source files for our thesis. However there are other workflows like using Scientific Markdown and Git to write the PhD thesis. [Git + Scientific Markdown workflow for PhD thesis](https://github.com/katrinleinweber/PhD-thesis)

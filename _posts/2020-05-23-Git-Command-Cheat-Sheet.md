---
layout: post
author: fubar
title: Cheat sheet for GIT
tag: programming
tool: git
excerpt: "A reference for the commonly used GIT commands and explanations of the context when they are used"
date: 23rd May, 2020
---

## Abstract

The concepts around Git can be summarized by the taglines

- Distributed is the new centralized

## Introduction

Version control is an essential element of software management. Git is a Swiss Army knife equivalent among the version control systems.

> Git is a version control system that provides tools to probe, build versioned software with key emphasis distributed development

 Let us learn the fundamentals of Git with the guidance of [the Git Parable](https://tom.preston-werner.com/2009/05/19/the-git-parable.html) and apply Git to each step of software sharing that involve

- code reuse
- code build up
- code sharing/shipping

## Code reuse

Reusability of code is essential feature of software development. It sincerely captures of philosophy of **standing on top of the shoulder of giants**, a phrase that was famously used by Stephen Hawking in his book on Celestial mechanics and also used as tagline of Google scholar. To be able to reuse code, firstly it needs to be available for installation. Prior to the internet, code was shared in the form of physical shipping of physical media like floppy disks and CDs. With the advent of internet, physical media sharing was bypassed and code was `downloaded` either directly from others computers or from common repositories. With the evolution of code sharing, came standards for how to share code. Then came the formats like `.tar.gz` and `.zip` files which are bundles for code files, binary or otherwise. With the advent of version control systems, code was accessible from a central repository on the internet. In a centralized version control system, there is a **single host**. A download involved accessing the contents of the repository. In contrast, distributed version control systems like `Git` allowed **multilple hosts**. To host a code all one had to do was download the entire code and provide the link to download. in this anyone can be a potential host and anyone with access to the link can download the code.

For our purpose of learning code reuse we will use [GitHub' code hosting service](https://inkscape.org/develop/extensions/). Code on GitHub is categorized into **Git repositories**. It is to be noted that Git repository cannot be hosted anywhere. Only that GitHub is one of the hosting services. Others include but not limited to [GitLab](https://about.gitlab.com/), older [Sourceforge](https://sourceforge.net/), [Bitbucket](https://bitbucket.org/).

> A Git repository is simply a versioned code that tracks the history of its development.

There are two kinds of Git repositories; private and public type. A public repository is accessible to anyone with an Internet connection in two ways

- download the repository as a **zipped** file to your local machine.
- **cloning the repository** via local Git system.

We will focus on the later.

### Git cloning

> Git clone is basically getting a copy of the Git repository on the local machine.

Before we begin git cloning the repository, we need to [setup Git system on our local machine](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Now that we a working Git on your system, let us take a simple repository as a concrete example to work with. Currently fubar is interested in developing an [Inkscape extension](https://inkscape.org/develop/extensions/) to draw the orbitals of a hydrogen atom by providing the quantum numbers as input parameters to the extension. After reading the documentation, fubar proceeds to work on an extension template hosted as a Git repository at

    https://github.com/Neon22/inkscape_extension_template

From the URL to the Git repository it is understood that the name of the repository is `inkscape_extension_template`, the name of the developer is `Neon22`. To clone the Git repository, we need the URL of the Git repository which is

    https://github.com/Neon22/inkscape_extension_template.git

with a suffix `.git`. Now fubar fires up a `Git Bash on Windows` shell and moves to the directory that hosts Git repositories and executes

    $git clone https://github.com/Neon22/inkscape_extension_template.git

    Cloning into 'inkscape_extension_template'...
    remote: Enumerating objects: 2, done.
    remote: Counting objects: 100% (2/2), done.
    remote: Compressing objects: 100% (2/2), done.
    remote: Total 60 (delta 0), reused 0 (delta 0), pack-reused 58
    Unpacking objects: 100% (60/60), done.

This command has **cloned the Git repository** from the GitHub repository. One of our first Git commands. To check the contents of the clone change into the git repository.

    cd inkscape_extension_template/

Check the contents of the repository including the hidden files and folders

    ls -al

    total 38
    drwxr-xr-x 1 fubar 197121     0 Jun  1 19:41 ./
    drwxr-xr-x 1 fubar 197121     0 Jun  1 19:40 ../
    drwxr-xr-x 1 fubar 197121     0 Jun  1 19:41 .git/
    -rw-r--r-- 1 fubar 197121   702 Jun  1 19:41 .gitignore
    -rw-r--r-- 1 fubar 197121  1098 Jun  1 19:41 LICENSE.md
    -rw-r--r-- 1 fubar 197121   541 Jun  1 19:41 README.md
    -rw-r--r-- 1 fubar 197121  4215 Jun  1 19:41 template.inx
    -rwxr-xr-x 1 fubar 197121 13222 Jun  1 19:41 template.py*

In addition to the usual source files, there is the most important hidden directory **.git** which tracks the entire history of the code development. We will now extract various kinds of information about the project from this hidden directory using appropriate Git commands.

### Remote repository information

Our local Git repository and the host Git repository maintain a parent-child relationship. Just as the local repository is called the **clone** of the host repository, the host is called the **remote** of the local repository. To probe the remote of the local clone, fubar executes

    $git remote -v

    origin	https://github.com/Neon22/inkscape_extension_template.git (fetch)
    origin	https://github.com/Neon22/inkscape_extension_template.git (push)

There are two **remote** listings each. Both are named **origin**. Origin refers to the **original remote** from which the current local Git repository has been cloned from. The location of the origin is given by the URL in the second columns The first is of type **fetch** and the second is of type **push**.

To understand **fetch** and **push** types we have to bear in mind that neither the version of the remote Git repository is frozen nor the version is the local Git repository is frozen. Both undergo **revision** with the course of time. If fubar wants to request the latest revision, fubar does a **fetch** and instead he wants to share his own revision, he does a **push**. We will revisit these Git concepts later we deal with [Code Sharing](#code-sharing)

### Viewing the commit History

Now fubar is curious about how the repository went about getting developed i.e. he wants to get quick snapshot of the history of the repository. This is stored in the **log** of the git repository. To probe the log with a minimal output fubar executes

    $git log --oneline

    d97836c Delete extension information.txt
    4889dc9 Add notepad page docs
    8a3c5c3 Update color
    8049ee6 Update for color example
    c49d5cd Merge pull request #2 from Moini/patch-1
    3d19313 Fix error
    406cfba Merge pull request #1 from Moini/patch-1
    e204ad8 Add hint about meaning of underscores
    fe82878 Update for 0.91
    ac1d702 more info
    c083b0b added enums without minmal appearance
    bac9453 first pass
    1da7b47 MIT license
    4862033 ignore
    1fdb2c9 readme
    15e9eb1 Create README.md
    4d9117c Revert "initial commit"
    3cc5ac8 Create .gitignore
    8d98e82 Create LICENSE.md
    b65b4a1 Create README.md

The output lists a series of what are called **snapshots** of the Git repository. A **snapshot** is an iteration of code development that adds a particular functionality to the existing repository. The functionality can be a adding a new feature, an update to the documentation. Every iteration is labelled by a  **commit message** and a 40 character SHA1 hash over the additional code. The process of adding these iterations to the repository is discussed in [Code Sharing section](#code-sharing). The output summa
With a `--oneline` flag, the output is restricted to the list of commits along with only first 7 hexadecimal digits of the SHA1 encrypted snapshot for brevity. The latest snapshot is listed first. This is one of the first Git commands as part of [Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) as described in the original Git tutorial.


## Code Sharing


## Beginner level GIT command index

    <local/dir/path>$git clone <path/to/repository>

This accesses the remote git repository and clones it at the local directory path `<local/dir/path>`

    $git restore .

Suppose you did some changes to existing files and now intend have a clean slate of the working directory restored upto the last commit. As long as you have not done a commit yet, you are safe simply use the `restore` command to erase the modifications.

    $git clean [-n] [-f] [-d]

If you have added new files which are not yet tracked then restore will not work. You need to use `clean` command. The `-n` flag will list the files that can be possibly cleaned if the `-f` flag is used. So `-f` will clean the files whereas `-d` will clean the directories. This is useful when you do an error in copying files to the working directory and dont intend to keep the files.

This is taken from this [SO post](https://stackoverflow.com/questions/61212/how-to-remove-local-untracked-files-from-the-current-git-working-tree).

## Intermediate level GIT command index

???


## Advanced level GIT command index


???

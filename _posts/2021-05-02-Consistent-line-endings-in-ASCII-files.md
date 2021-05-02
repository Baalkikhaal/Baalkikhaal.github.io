---
layout: post
author: fubar
title: "Consistent line endings in ASCII files"
tag: programming
tool: git
excerpt: "In the circumstance of developing parallelly from a native Windows and virtual Windows Subsystem for Linux, we need a consistent way of ending the lines in ASCII files."
date: 02nd May, 2021
---
## Introduction
The default line ending for Windows ASCII text files is a sequence of characters `Carriage Return(CR)` followed by `LineFeed (LF)` jointly referred as `CRLF`, whereas on Linux, ASCII text files have lines ending with only `LF` character. When the source code files are maintained by versioning system like Git and the development of the code happens on both Windows and Linux systems, We need a consistent way of pushing cross-platform commits to the central repository.

## Git on WSL
Starting with Windows Subsystem on Linux (WSL), there is a tendency to develop parallelly either using the native environments on Windows like (Atom+ Git For Windows) workflow or using the subsystem environment on WSL like (nano + git) workflow.

Mixing the development timeline across native or subsystem can lead to mess up with respect to line endings in the source code.

To illustrate such a mess up, consider the following situation.

- We have a GitHub repository that has commits from a Linux machine up till now. For the purpose of demonstration, let us use the [Neural Networks repository](https://github.com/Baalkikhaal/NeuralNetworks).
  - We need to clone this using Git on either Windows or WSL. We use [Git on Windows Bash shell](https://git-scm.com/downloads) on native Windows, while the pre-installed Git on WSL.
  - Also the repository can be cloned either in the filesystem of
either `NTFS` type of native Windows or the `ext` type of WSL Linux distribution.
- So we will perform **four experiments** combining two options of Git and two options of filesystems.

## Git on Windows

Let us clone the GitHub repo (short for repository) into the Windows filesystem using Git For Windows.
The Git version is

```bash
$ git --version
git version 2.31.1.windows.1
```

The default Git configuration option related to handling line ending is

```
$ git config core.autocrlf
true
```

So when we clone a repository, `Git Bash` does an **auto conversion** of line endings if the remote repository has Linux line endings. Now let us clone using `Git Bash` into both the host `NTFS` and virtual Linux distribution `ext` filesystem.

### Clone into `NTFS`

Let us clone the GitHub repository into E drive at `MyGitHub` directory at `NN_Cloned_By_Windows_Git`.

```bash
fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub
$ git clone https://github.com/Baalkikhaal/NeuralNetworks.git NN_Cloned_By_Windows_Git
Cloning into 'NN_Cloned_By_Windows_Git'...
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 12 (delta 0), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (12/12), 15.38 KiB | 3.84 MiB/s, done.
```

Change to the cloned repository

```bash
fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub
$ cd NN_Cloned_By_Windows_Git/
```

The cloned repository has GitHub pages that we need to enhance. These are located in the `gh-pages` branch.
Let us checkout this branch.

```bash
fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/NN_Cloned_By_Windows_Git (main)
$ git checkout gh-pages
Switched to a new branch 'gh-pages'
Branch 'gh-pages' set up to track remote branch 'gh-pages' from 'origin'.
```

To check the line endings in the ASCII files of this repository, there are two options.

- use Notepad++ editor
- use file command of Git Bash

The first method is a Graphical User Interface (GUI) based where `NotePad++` displays the line ending for convenience of developers at the bottom right of the GUI.

![image-of-notepad++-gui][screenshot-notepad]

 Also the locations of these line endings can be enabled using `View > Show Symbol > Show End of Line`.

![image-of-notepad++-with-display-of-line-endings-enabled][screenshot-notepad-line-endings]

The second method is Command Line Interface (CLI) based where we use the `file` command of bash shell.

`file` [detects the filetype](https://stackoverflow.com/questions/32255747/on-windows-how-would-i-detect-the-line-ending-of-a-file/46548284#46548284)
into three types

- ASCII text
- executable
- binary

For ASCII text it provides information about the line ending. Running

```bash
$ file index.md
index.md: ASCII text, with CRLF line terminators
```

suggests the file has CRLF line endings.


[screenshot-notepad]: /assets/images/Microsoft/WindowsSubsystemForLinux/LineEndings/notepad++_line_ending.png

[screenshot-notepad-line-endings]: /assets/images/Microsoft/WindowsSubsystemForLinux/LineEndings/notepad++_line_ending_lineend_characters.png

### Clone into `ext` file system

To clone into the virtual distro's `ext` filesystem, we need to stringup the filepath for the root of ext filesystem. This can be extracted from the explorer's address bar

![image-of-explorer-displaying-the-filepath-of-virtual-distribution-root][screenshot-explorer-wsl-root]

The default location of root of WSL GNU/Linux distro (Ubuntu 18.04 in my case) is at

```bash
\\wsl.localhost\Ubuntu-18.04
```
Note the `\\` that denotes a Network drive.

Now open a new Git on Windows Bash terminal at the home folder of root, change to the `GitHubProjects` folder of mounted filesystem.

```bash
\\wsl.localhost\Ubuntu-18.04\home\fubar\GithubProjects
```

Clone the GitHub repository at this location with the name `NN_Cloned_By_Windows_Git`

```bash
fubar@desktop-fubar MINGW64 //wsl.localhost/Ubuntu-18.04/home/fubar/GithubProjects
$ git clone https://github.com/Baalkikhaal/NeuralNetworks.git NN_Cloned_By_Windows_Git
...
...
```

Change to `NN_Cloned_By_Windows_Git` folder, checkout the `gh-pages` branch and check the file type.

```bash
$ file index.md
index.md: ASCII text, with CRLF line terminators
```

So, we can infer that irrespective of where the repository is cloned, Git on Windows does auto conversion of Linux line endings to CRLF lineendings.

[screenshot-explorer-wsl-root]: /assets/images/Microsoft/WindowsSubsystemForLinux/LineEndings/root_location_of_WSL_distro.png

## Git on WSL
On WSL, Git comes pre-installed. The Git version used here is

```bash
git  fubar desktop-fubar  ~ $ git --version
git version 2.17.1
```

Now we do not have to worry about the auto CRLF conversion, as Git is primarily built for and on Linux.

So there is no config option called `core.autocrlf`.

### Clone into ext

Let us clone into the `GitHubProjects` folder of the home folder with the name `NN_cloned_By_WSL_Git`.

```bash
 fubar  desktop-fubar  ~  GithubProjects  $  git clone https://github.com/Baalkikhaal/NeuralNetworks.git NN_cloned_By_WSL_Git
Cloning into 'NN_cloned_By_WSL_Git'...
...
...
```

Change to `NN_cloned_By_WSL_Git` repository folder and `gh-pages` branch and check the line ending

```bash
 fubar  desktop-fubar  ~  GithubProjects  NN_Cloned_By_WSL_Git   gh-pages  $  file index.md
index.md: ASCII text
```

It is a LF character if nothing extra is printed alongside ASCII text.

### Clone into `NTFS`

To clone into `E:\Databases\GitHub\MyGitHub` on `NTFS` via WSL, we need the filepath in the WSL. The E drive is mounted at

```bash
/mnt/e/
```

So change to the `MyGitHub` directory and clone the repository with the name `NN_Cloned_By_WSL_Git`

```bash
 fubar  desktop-fubar  mnt  c  Users  fubar  $  cd /mnt/e/Databases/GitHub/MyGitHub/
 fubar  desktop-fubar  mnt  e  Databases  GitHub  MyGitHub  $  git clone https://github.com/Baalkikhaal/NeuralNetworks.git NN_Cloned_By_WSL_Git
```

Change to `NN_Cloned_By_WSL_Git` repository folder and `gh-pages` branch and check the line ending
```bash
fubar  desktop-fubar  mnt  e  …  GitHub  MyGitHub  NN_Cloned_By_WSL_Git   gh-pages  $  file index.md
index.md: ASCII text
```

## Inference of the experiments

From the last two experiments, we can infer that irrespective of the where the repository is cloned, Git on WSL ends lines Unix style where Git on Windows ends lines Windows style.

## Consistent way of developing source code

As a result, it is advised to stick to a consistent line ending. We can do this by disabling the auto-conversion that Git on Windows enforces if it notices Linux style line endings.

We can [enforce Linux style line ending](https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-containers-resulting-in-many-modified-files) while developing on Windows either on a

- per repository basis, or
- system wide basis

In the first method, add a `.gitattributes` at the root of the repository `NN_Cloned_By_Windows_Git` on Windows host with the following lines

```bash
* text=auto eol=lf
*.{cmd,[cC][mM][dD]} text eol=crlf
*.{bat,[bB][aA][tT]} text eol=crlf
```

With this, other than the Windows batch files that require `CRLF` ending, all the ASCII files are forced to end with `LF`. To check the changes are in place, open a new Git bash and

```
fubar@desktop-fubar MINGW64 /e/Databases/GitHub/MyGitHub/NN_Cloned_By_Windows_Git (gh-pages)
$ file index.md
index.md: ASCII text
```

Even the Notepad++ shows the changes are applied.

![image-notepad++-forced-lineending][screenshot-notepad-forced-lineending]

In special situations, where we are sure we do not have Windows batchfiles, we can apply the second method, wherein we disable auto-conversion system-wide using

```bash
git config --global core.autocrlf false
```

[screenshot-notepad-forced-lineending]: /assets/images/Microsoft/WindowsSubsystemForLinux/LineEndings/notepad++_forced_lineend_LF_character.png

## Summary

It is essential to have a consistent environment setup for source code development both on the host Windows and the virtual WSL, when the workflow involves a central  Git repository. So it is advised to disable the auto-conversion of End-of-Line characters in the windows version of Git client.

## References

- [Get started with Git on WSL](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git#git-line-endings).
- [Resolving Git line ending issues in containers](https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-containers-resulting-in-many-modified-files).
- [Tool to check file ending cross platform](https://stackoverflow.com/questions/32255747/on-windows-how-would-i-detect-the-line-ending-of-a-file/46548284#46548284).
- [File utility on *nix systems](https://stackoverflow.com/questions/3569997/how-to-find-out-line-endings-in-a-text-file).

---
layout: post
author: fubar
title: "Git client configuration (basics)"
tag: programming
tool: git
excerpt: "Git is a cross-platform utility and it is essential to understand the way it is configured. In certain circumstances, it is required to modify the configuration to suit the needs. We will discuss one such circumstance when we need to carry cross platform development on both native Windows and virtual Windows Subsystem for Linux (WSL) GNU/Linux distribution."
date: 03rd May, 2021
---

## Introduction

Git has numerous commands running into hundreds. Most of these commands have various options/parameters that have default values configured. These parameter-value pairs are stored at various configuration files; yes Git has more than one configuration file, but more on this later. `git config` command configures these parameters.

## Syntax

```bash
git config option value
```

The basic syntax has two arguments. The first argument name is the option that has a `section`.`key` syntax while the second argument is the `value` of the option. For example, the most conspicuous among the configuration parameters is the username of the Gitter who carries out the various [actions in the Git universe][post-0]. This parameter is categorized into the `user` section with `name` key

### Set the keys

The various configuration commands can be classified into `set-type` and `get-type` commands. To [set the username for the Gitter](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup), probably when we first install the Git client, we run

```bash
$ git config --global user.name "Gandalf the Grey"
```

We will discuss more on `--global` in [configuration scopes](#configuration-scopes).

### Get the keyvalues

In case we want to get the value configured for the same key, we prepend the parameter with a `--get` flag and run

```bash
$ git config --get user.name
Gandalf the Grey
```

In addition to the `name`, there are other keys in the section `user`. To fetch the keys that have already been set, we use [regular expressions]({% post_url 2021-03-29-Commonly-used-Regular-expressions %}). We prepend a `--get-regex` flag to the regex `user.*` to get

```bash
$ git config --get-regexp user.*
user.email wizard.gandalf@fellowship.middleearth
user.name Gandalf the Grey
```

## Configuration scopes

Git provides a heirarchy of control over the way the repository is configured. The heirarchy is nested into scopes. Each scope is configured by a configuration file (see #configuration-origins)

Scope | Origin(File) | Scope flag
---|---|---
system | /etc/gitconfig | `--system`
global | ~/.gitconfig | `--global`
local | .git/config | `--local`

Every parameter can be configured at any scope. To set a local scope for `user.name` key, we prepend it with a `--local` flag.

```bash
$ git config --local user.name "Frodo Baggins"
```

If we try getting the `user.name` key's value as done in [Get the key values](#get-the-keyvalues)

```bash
$ git config --get user.name
Frodo Baggins
```

To get the scope of `user.name` key, we prepend it with a `--show-scope` flag

```bash
$ git config --show-scope --get user.name
local   Frodo Baggins
```

So it might appear that the earlier value of `user.name` key has been replaced from `Gandalf the Grey` (see [Set the key values](#set-the-keys)) to that in the local scope `Frodo Baggins`. The appropriate description here is not replacement, but rather a supercedence of the global scope by the local scope. `Gandalf the Grey` was set in the global scope, while `Frodo Baggins` was set in the local scope. If the parameter has been configured at more than one scope, the final configuration is resolved by the following precedence rule

```bash
system < global < local
```
To list all the occurences across the various scopes, we use `--get-regex` flag.

```bash
$ git config --show-scope --get-regex user.name
global  user.name Gandalf the Grey
local   user.name Frodo Baggins
```

## Configuration files (origins)

In the [Syntax](#syntax) section, the various get and set commands interact with a **configuration file**. A `set-type` command writes to, while a `get-type` command reads from a configuration file. This file is the **origin** of the configuration. To get the configuration-origin, we prepend the parameter name with `--show-origin`

```bash
$ git config --show-origin --get user.name
file:.git/config        Frodo Baggins
```

So the key is sourced from the above file located at the root of the git repository `.git/config `. Let us view its contents

```bash
$ cat .git/config
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[submodule]
        active = .
[remote "origin"]
        url = https://github.com/Baalkikhaal/wsl2-gui.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
        remote = origin
        merge = refs/heads/main
[auto]
        crlf = input
        crlf = input
[user]
        name = Frodo Baggins
```

The file is sectioned into sections with section headings delimited by square brackets. More on the sections in [Sections](#sections). We have earlier mentioned about the [configuration scopes](#configuration-scopes). Every configuration scope is associated with a configuration file. Now if we would like to show the origins for every occurence of the key-value pair, we replace `--get` with the `--get-regex` flag. Additionally, let us use `--show-scope` flag to display the scope

```bash
$ git config --show-scope --show-origin --get-regex user.name
global  file:C:/Users/fubar/.gitconfig  user.name Gandalf the Grey
local   file:.git/config        user.name Frodo Baggins
```

The global scope configuration is handled by the `C:/Users/fubar/.gitconfig` configuration file. Let us view its contents

```bash
[user]
        email = wizard.gandalf@fellowship.middleearth
        name = Gandalf the Grey
[filter "lfs"]
        clean = git-lfs clean -- %f
        smudge = git-lfs smudge -- %f
        process = git-lfs filter-process
        required = true
[core]
        autocrlf = false
```

## Sections

The configuration is sectioned into various sections. Some of them are

Section | Description
---|---
User | Committer information on name, email id
Core | Hosts the core variables (lots of them)

As an example, let us set the `core.autocrlf` to input. This will disable conversion of `LF` endings in the repository (`.git/`) to `CRLF` in the working directory(`wsl-gui`). Refer to [consistent  line endings during cross-platform development]({% post_url 2021-05-02-Consistent-line-endings-in-ASCII-files %}) and [Formatting and Whitespace](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_formatting_and_whitespace) subheading of Chapter "Customizing Git" of Pro Git Book.

```bash
git config --global core.autocrlf input
```

## Quick hacks

To list all the keys in the configuration files (system, global, local)

```bash
git config --list
```

To list all the keys in a specific scope, prepend the corresponding flag

```bash
$ git config --system --list
```

To get help on a particular Git command, prepend with `--help` flag

```bash
git config --help
```

## Summary

`git config` is a powerful command and is extensively used along with `git help` command (See more on [Git help][post-3]) for common [everyday tweaking and referencing][ref-3]. In fact, most of the information above can be attained by

```bash
git help config
```

## See Also

[Git Actions](post-0)

[Regular expressions]({% post_url 2021-03-29-Commonly-used-Regular-expressions %})

[consistent  line endings during cross-platform development]({% post_url 2021-05-02-Consistent-line-endings-in-ASCII-files %})

[Git help](post-3)

<!-- post-0: post_url 2021-05-03-Git-client-actions-basics  -->

<!-- post-3: post_url 2021-05-03-Git-client-help-basics -->

## References

[Git config man page](https://man7.org/linux/man-pages/man1/git-config.1.html)

[Pro Git Book on Git configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_git_config)

[Pro Git on Git configuration Appendix][ref-3]

[ref-3]: https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config#_setup_and_config

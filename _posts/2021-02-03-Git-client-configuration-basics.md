---
layout: post
author: fubar
title: "Git client configuration (basics)"
tag: programming
tool: git
excerpt: "Git is a cross-platform utility and it is essential to understand the way it is configured. In certain circumstances, it is required to modify the configuration to suit the needs. We will discuss one such circumstance when we need to carry cross platform development on both native Windows and virtual Windows Subsystem for Linux (WSL) GNU/Linux distribution."
date: 03nd May, 2021
---

## Introduction

Git has numerous commands running into hundreds. Most of these commands have various options/parameters that have default values configured. These parameter-value pairs are stored at various configuration files; yes Git has more than one configuration file, but more on this later. `git config` command configures these parameters.

## Syntax

```bash
git config option value
```

The basic syntax has two arguments. The first argument name is the option that has a `section`.`key` syntax while the second argument is the `value` of the option. For example, the most conspicuous among the configuration parameters is the username of the Gitter who carries out the various [actions in the Git universe]( {% post_url post_on_git_actions % }). This parameter is categorized into the `user` section with `name` key

The various configuration commands can be classified into `set-type` and `get-type` commands. To [set the username for the Gitter](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup), probably when we first install the Git client, we run

```bash
$ git config --global user.name "Sreekar Guddeti"
```

More on `--global` in [configuration scopes](#configuration-scopes). In case we want to get the value configured for the same key, we prepend the parameter with a `--get` flag and run

```bash
$ git config --get user.name
Sreekar Guddeti
```

In addition to the `name`, there are other keys in the section `user`. To fetch the keys that have already been set, we use [regular expressions]( {% post_on_regular_expressions %}). We prepend a `--get-regex` flag to the regex `user.*` to get

```bash
$ git config --get-regexp user.*
user.email colonel.sreekar@gmail.com
user.name Sreekar Guddeti
```

## Sections

The configuration is sectioned into various sections. Some of them are



## Configuration origins

In the Syntax section, the various get and set commands interact with a configuration file. A `set-type` command writes to, while a `get-type` command reads from a configuration file. This file is the origin of the configuration. To get the configuration-origin, we prepend the parameter name with `--show-origin`

```bash
$ git config --show-origin user.name
file:C:/Users/fubar/.gitconfig  Sreekar Guddeti
```

So the key is sourced from the above file located at the home folder `C:/Users/fubar/`. Let us view at the contents

```bash
$ cat ~/.gitconfig
[user]
        email = colonel.sreekar@gmail.com
        name = Sreekar Guddeti
[filter "lfs"]
        clean = git-lfs clean -- %f
        smudge = git-lfs smudge -- %f
        process = git-lfs filter-process
        required = true
[gui]
        recentrepo = C:/Users/fubar/Desktop/TestingGit2/FinalPresentation
[core]
        autocrlf = false
[auto]
        crlf = false
```

## References

[Canonical source for Git configuration ञान](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_git_config)

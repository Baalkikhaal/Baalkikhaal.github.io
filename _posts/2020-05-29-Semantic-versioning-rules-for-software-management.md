---
layout: post
author: fubar
title: "Semantic versioning rules for software management"
tag: programming
tool: git
excerpt: "We will describe the rules for versioning software to avoid dependency hell"
date: 29th May, 2020
---

## Abstract

[Semantic versioning](https://semver.org/) rules to update a software at a version `MAJOR.MINOR.PATCH` recommend
- incrementing `MAJOR` version when you make incompatible API changes
- incrementing `MINOR` version when you add functionality in a backwards compatible manner
- incrementing `PATCH` version when you make backwards compatible bug fixes.

Software development is a multi user multi platform multi-organization endeavour. Each piece of program depends on other libraries.
Just as a program goes through iterative process of development, the dependencies undergo their own cycles of development. Lets say we develop a `program P` that provides a `plugin p1`. Let this be the current `version x` of `program P` and denote it by `P(x)`. `P(x)` depends on the current `version y` of `library L`. Let us denoted this version of `library L` by `L(y)`. `L(x)` has certain **functionalities** like `f1` and `f2`, of which `p1` needs `f1`. So we build on top of the API of the `L(x)` by using only `f1` in our program `P`.

So far so good. However in the course of time, we progress with our development and add an extra `plugin p2` to our `program P`. `p2` depends on both `f1` and `f2`. Parallelly, the developers of `library L` have iterated through their own cycle of development. In the latest iteration, they improved implementation of `f1` keeping the interface to `f1` unaltered. However, they realized that `f2` needs a reformation of the interface also. Additionally they developed a new `functionality f3` and released these improvements in their latest `version ( y + 1 )`. Let us denote this version by `L( y + 1 )`.

Now there are two impending questions here. The first question is how does the `library L` developer community communicates to their users of their new changes. The second question is how does the `program P` community go about adopting the latest version `L( y + 1 )`.

One way to address the first question is  through extensive documentation of the new version so that that application developers can go through the documentation and take note of the changes and accordingly take the decision of migrating to the newer version of the `dependency L`.

>However developers are poor documenters.

Instead, a set of rules evolved with the community to convey quickly what might have possibly changed in the new version. This collection of rules for versioning software is called **semantic versioning**.

The second question is what leads to the possibility of **software dependency hell**.

---

## Semantic Versioning

[Semantic versioning](https://semver.org/) is a way to avoid what is commonly called the **software dependency hell**. Software dependency hell swings the choice of upgrading software between two limiting scenarios.

### Dependency hell spectrum : Version locking vs version promiscuity
At the one end of what is called as **version locking**, the developer community of program P makes a choice to upgrade P without depending on the latest version of `L` as the interface of `functionality f2` has changed and would break the implementation of `plugin p2`. By version locking of the `dependency L`, we loose out on the performance improvements of `plugin p1` as the latest version of L has improved version of `functionality f1` on which `plugin p1` depends. It does not mean the `program P` cannot be upgraded. The latest version `p( x + 1)` can contain `plugin p2` with dependency `L(y)`.

At the other end of the spectrum of dependency hell, the developer community decides to upgrade P by depending on the latest version `L( y + 1 )` to gain the performance improvement of `plugin p1` (as there is improvement of `functionality f1` on which `p1` depends) even at the cost of **breaking** `plugin p2`. Additionally there is a possiblity of developing a new `plugin p3` that might use `functionality f3`. The possibility of breaking code might seriously affect the end user of the program and this sort of upgradation of software comes under what is called as **version promiscuity**.

Either ends of the spectrum are harmful to software development. To choose a middle path, semantic versioning helps one take an informed judgement on if and when to upgrade software.

### Semantic versioning specification

The developer community over the course of years have come up with a set of rules on how to version their individual softwares so that software interdependency can be resolved in a sane way. A typical iteration of software development involves three steps

- feature enhancement
- feature testing
- feature release or shipping

#### Feature enhancement

The semantic versioning rules are closely associated with these steps. A feature enhancement can be of type **MAJOR** like a rework on the Application Programmer's Interface(API). This needs to send alarm bells to the users of this API as their programs will not be compatible with this new API. As a result this enhancement is called being **backwards incompatible**. A feature enhancement can be of type **MINOR** like adding new functionality without breaking existing API. This enhancement is called being **backwards compatible**. This feature may improve implementation of existing functionality or be a complete new functionality in which case it **adds to the API** and at the same is being backwards compatible. A third type of feature enhancement is fixing bugs. A bug is a wrong implementation of a feature leading to erroneous behaviour of the program using the API. An enhancement  that fixes bugs is called a **PATCH**. A patch neither improves existing functionality nor adds new functionality. It only corrects/fixes existing functionality.

The above is for a particular iteration of the development of the program. To capture the entire timeline of the development, the type of feature enhancements ever done are coded in the **version** of software with a format `MAJOR.MINOR.PATCH` of dot separated numerical identifiers for `MAJOR`, `MINOR` and `PATCH`. Each of these numerical identifiers are whole numbers.

>With every iteration of the development, depending on the type of feature enhancement carried out, the corresponding identifier is incremented by 1 and is called a **release**.

For example, let the current version of `program P` is `v1.0.0` and current version of `library L` is `v1.1.2`. This means till now there has been one API release for L and followed by 1 minor release of backwards compatible enhancements in the functionalities followed by 2 releases of bug fixes. Similarly program P has only a major release after which there is no further development. However nothing is known of previous major releases and its sub releases of minors and patches.

It should be noted that once a version is released, there is no going back. At the most, one can do a bug fix for the release in future.

#### Feature testing

The above releases are called **normal releases** or **stable releases**. Since version releases are only forward directional, developers of large projects **pre-release** a software prior to the actual release. The reason is two fold;to let the common user know that they are **unstable** and therefore stay away from it as they can potentially break the global system like the Operating system and what not. These release are intended for power users in the hope that they fish out remaining bugs. Pre-release is distinguished from a normal release by suffixing terms like **alpha**, **beta**, **rc** with a hyphen.

- Alpha pre-release may not contain all the features planned for the final release, but at the end of the alpha phase, the software is feature complete. Proprietary software do not release their alpha-pre releases to the general public unlike open source software.
- Beta pre-relase phase starts with feature complete software but has bugs. This is pre-released in the open source community for bug testing.
- Release candidate (rc) pre-release has the potential to be **stable**.

For more info, check this [Wikipedia article on Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle#Pre-alpha).

### Feature release

Once there is reasonable certainty that the pre-releases are stable, they are released with versioning following the rules of semantic versioning.

### Precedence of versions

When comparing releases with respect to the time ordering of the releases, the precedence is calculated by comparing separately the major, minor, and path and pre-release identifiers.
- 1.x.y < 2.p.q for any x, y, p, q
- 1.0.y < 1.1.q for any y, q
- 1.0.0-<pre-release> < 1.0.0
- 1.0.0-alpha < 1.0.0-beta < 1.0.0-rc

## A concrete example of Inkscape development

Inkscape is a mature project with a history of more than 16 years. The current release as of 29th of May, 2020 is 1.0.0. Prior versions were of the type 0.x.y

The major version increment means there is some backwards incompatible. From the [Inkscape v1.0.0 release documentation](https://wiki.inkscape.org/wiki/index.php?title=Release_notes/1.0#python3), it is clear that Inkscape has migrated to using GTK+3. Earlier v0.x.y versions were using GTK+2. GTK (Gimp Tool Kit) is a widget based took kit for creating graphical user interfaces. However the major version increment is not due to shifting to GTK+3, but it is due to backwards incompatible SVG?? (I dont know what that means) I think it means that SVG standard has upgraded itself. To incorporate the newer SVG standard, Inkscapes API has been modified (remember that Inkscape provides a command line mode.. so in effect inkscape can be used as an API as in for Inkscape extensions!!!)

---

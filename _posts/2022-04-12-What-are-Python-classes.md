---
layout: post
author: fubar
title: "What are Python classes?"
tag: programming, architecture
tool: python
excerpt: "The organization of python program is discussed with class as an entity."
date: 12th April, 2022
---

## Abstract

Class is a high level unit of program organization. 
They facilitate a new kind of programming style called the **object oriented programming (OOP)** style.
In contrast to the procedural programming style that constitutes functions,
the OOP style constitutes classes where data is given precedence over flow of logic.
This trade-off leads to new ways implementing behaviour and turns out to be more natural for certain use cases,
for which procedural programming either has no solution or the solution it offers is cumbersome.

As it is a modern approach to progamming, it is pedagogical to compare and contrast classes with other structural units that Python offers like [functions]({% post_url 2022-04-12-What-are-Python-functions %}),
 [modules]({% post_url 2019-09-14-What-are-Python-modules %}).
 
## What is a class?

In the most general sense, a class is ~~a placeholder~~ an interface that encapsulates data.
In contrast, functions encapsulate logic, whereas modules hold both data and logic.

The data within a class is termed its **attributes**.
To perform data manipulation operations like transformation, and mutation,
the corresponding logic can be defined within the **methods** which are attributes by themselves.

```python
class my_class(arguments):
	attributes
```

As an example, let us consider implementing the behaviour of circles on an inkscape document.
A circle can be mathematically defined by the coordinates of its center and its radius.
Additionally, as an inkscape primitive, it have additional attributes like
 fillcolor, strokecolor, strokewidth, etc. However, for pedagogical purposed, 
 let us restrict to minimalistic mathematical definition. So, a circle has three attribues.

```python
class Circle(center_x, center_y, radius):
	self.center_x = center_x
	self.center_y = center_y
	self.radius = radius
```

> In contrast, funcitons per se cannot hold the state of the system; they need to use global variables.
Modules, on the other hand, provide an interface to model a stateful behaviour.

In Python, interfaces are used to defined objects.
A class interface can be used to define class object called **instance**.
The instance then has as its attributes, the attributes of the class.
In other words, these attributes denote the **state** of the object.

```python
my_instance = my_class()
```
To define an instance of `Circle` class,

```python
unit_circle = Circle(0, 0, 1)
```

Multiple instances of the class can also be defined so that each of the instance
has a unique set of attributes. So in effect, they are different objects,
 but **belonging** to the same class. 
 Technically, a class is a **generator** that provides the necessary template to spawn instances
that reflect the class behaviour.
 
```python
small_circle = my_class(1, 2, 1)
big_circle = my_class(2, 1, 5)
```
> In contrast, module is not a generator and defines the state only for the file.

### Flow of logic

Since the data is encapsulated within a class instance, when such instances interact with each other
only logic can flow across their interfaces.







Furthermore, a class can inherit attributes of other classes
 and equivalently propagate its own attributes to other classes.
 Both functions and module lack this unique interface called **attribute inheritance**.
 


## References

Chapter "OOP: The Big Picture" of "Learning Python" by Mark Lutz.
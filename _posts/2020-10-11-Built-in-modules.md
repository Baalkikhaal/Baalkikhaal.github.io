---
layout: post
author: fubar
tag: programming
title: "Useful built-in Python modules"
excerpt: "A list of commonly used Python built-in modules."
date: 11th October, 2020
---

## The Python Standard Library

From the [documentation](https://docs.python.org/3/library/index.html) of the Python Standard library,

> Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.

Module | description
---------|------
File and Directory Access | -
[pathlib](https://docs.python.org/3/library/pathlib.html) | This module offers classes representing filesystem paths with semantics appropriate for different operating systems. Path classes are divided between pure paths, which provide purely computational operations without I/O, and concrete paths, which inherit from pure paths but also provide I/O operations.
[os](https://docs.python.org/3/library/os.path.html)  | This module implements some useful functions on pathnames.
Runtime services | -
[inspect](https://docs.python.org/3/library/inspect.html?highlight=inspect#module-inspect) | The inspect module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks, frame objects, and code objects.
Cryptographic services | -
[hashlib](https://docs.python.org/3/library/hashlib.html) | This module implements a common interface to many different secure hash and message digest algorithms. 

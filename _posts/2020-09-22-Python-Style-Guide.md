---
layout: post
author: fubar
title: "How to design Python code?"
tag: programming
tool: python
excerpt: "Style guidelines for commonly encountered style decisions to be made while coding in python. We rely on the PEP guidelines to resolve them."
date: 22nd September, 2020
---

We primarily rely on the [Python Enhance Proposal 8 (PEP8)](https://www.python.org/dev/peps/pep-0008/)

A [stylized version of PEP8](https://pep8.org/) for humans is created by Kenneth Reitz for better readability

A more [Comprehensive explanation for styling](https://realpython.com/python-code-quality/)


# [On Imports](https://www.python.org/dev/peps/pep-0008/#id23)


[Comprehensive explanation on imports](https://realpython.com/absolute-vs-relative-python-imports/#relative-imports)

    Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

    Imports should be grouped in the following order:

        Standard library imports.
        Related third party imports.
        Local application/library specific imports.

    You should put a blank line between each group of imports.

# The Zen of Python

    !python
    import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

## Way 3 : Simple is better than complex

This way is with reference to Python coding in general.

From Mark Lutz's ''Learning Python'' Section on Dictionaries, on the choice of using `for` loop or functional programming tools like 'map', and 'filter' to iterate over list comprehensions (or an `**iterable**` object in general), the author mentions that functional programming tools run faster than `for` loops. However,


    A major rule of thumb in Python is to code for simplicity and readability first and worry about performance later, after your program is working, and after you’ve proved that there is a genuine performance concern.


## Way 5 : Flat is better than nested

This way is with reference to nested functions. Nested function definition are inherited from functional programming practices.

From Mark Lutz ''Learning Python'' on Arbitrary scope nesting (Chapter 17)

    **Arbitrary scope nesting**
    Before ending this discussion, I should note that scopes may nest arbitrarily, but only enclosing function def statements (not classes, described in Part VI) are searched:
        >>> def f1():
        ...     x = 99
        ...     def f2():
        ...         def f3():
        ...             print(x) # Found in f1's local scope!
        ...         f3()

In the above code, `f1()` is the enclosing function, `f2()` is the enclosed/nested function, `x` is the variable of the enclosing function being referenced by the enclosed/nested function.

Python allows arbitrary scope nesting. And variables of the outer nest can be referenced in the inner nest. To resolve the scope of the variable that is referenced, Enclosing(E) step of the LEGB rule is enforced.

    However it is to be noted that the resolution exercise is limited only to the enclosing `defs`. In contrast, classes provide extended scope resolution.

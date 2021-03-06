---
layout: post
author: fubar
title: "How to get the filepath of an imported module?"
tag: programming
tool: python
excerpt: "Python module can be imported within a script as well as in another module. This post describes two ways to get the filepath of an imported module."
date: 11th October, 2020
---

While working on the [KerrPy](https://github.com/Baalkikhaal/KerrPy) project, there is a global configuration file `globalVariables.py` from which the **relative** folder paths of postprocessed folder is extracted. This folder path is relative to the parent directory.
As a result, we need to form the absolute filepath using the parent directory absolute filepath and post processing folder relative path.

## Previous implementation

In the previous implementation, the script for processing was run from the parent directory. So using the `os` module, we get the absolute path of the parent directory. Using

    os.getcwd()

and the absolute filepath is passed onto subsequent methods.
However since the callbacks are deeply nested(more than 6 levels), with each inner callback, the number of arguments passed increase. This behaviour violates the following codes of Zen of Python.

>Readability counts.
>
>Flat is better than nested.

## Possible implementations

One way to resolve this design decision is to pass the arguments as arbitrary length tuple

    space = processData(*pargs)

and extract the parent_directory

```python
def processData(*pargs):
    parent_dir_abs = pargs[0]
```

This implementation improves readabiliy, however it still violates nesting.
One recommendation can be passing the variable via an import statement.

>The challenge is getting the absolute filepath of the parent directory.

Placing an `os.getcwd()` in the `globalVariables.py` is not going to work.

```python
#globalVariables.py
import os, os.path
post_processing_folder  = 'PostProcessing'
parent_dir_abs          = os.getcwd()
```

When `globalVariables.py` is imported

```python
#processData.py
from globalVariables import parent_dir_abs
print(parent_dir_abs)
```

Running the script `processData.py` gives

```bash
python processData.py
```

## Current implementation


### `__file__` attribute of module
There are two possiblities to get the absolute path to parent_dir_abs
First, create an intermediate module to 'string-up' the filepaths `loadFilePaths.py` to import the `__file__` attribute of the globalVariable. Here we **assume** that `globalVariables.py` is in the parent_directory. `__file__` stores the absoluted filepath of the `.pyc` byte code of the `globalVariables.py`. We can extract the folder hosting the file using `os.path.dirname()` method.

```python
#loadFilePaths.py
from globalVariables import post_processing_folder, __file__

parent_dir_abs = os.path.dirname(__file__)
```

However, as noted in the [SO post on retrieving module path](https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path/12154601#12154601), this will fail if we try to extract the `__file__` attribute from within the module itself.

```python
#globalVariables.py
post_processing_folder = 'PostProcessing'
print(__file__)
```
In Python 3.8, the `__file__` attribute of the module can be used within  the module.

Since we are importing the variable from an intermediate file, `__file__` attribute as implemented in the [KerrPy commit 052555d8393abc3a80b21a3d388a795a7ddb8557](https://github.com/Baalkikhaal/KerrPy/commit/052555d8393abc3a80b21a3d388a795a7ddb8557)


### `inspect` module

The `inspect` [built-in]({% post_url 2020-10-11-Built-in-modules %}) module provides methods to get information about live objects. From its [documentation]((https://docs.python.org/3/library/inspect.html?highlight=inspect#module-inspect)),

> The inspect module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks, frame objects, and code objects.

However since variables are not considered as objects, we need to use `import` statement instead of `from` statement. `inspect.getfile()` provides the filename of the file where the object is defined in.

```python
#globalVariables
import os

post_processing_folder = 'PostProcessing'
print(os.getcwd())
print(__file__)

def func():
    pass
```

```python
import inspect

from globalVariables import post_processing_folder, func

import globalVariables

print(post_processing_folder)

print(inspect.getfile(globalVariables))

code = inspect.getsource(func)

print(code)
```

gives output

```bash
C:\Users\fubar\OneDrive\Desktop
C:\Users\fubar\OneDrive\Desktop\globalVariables.py
PostProcessing
C:\Users\fubar\OneDrive\Desktop\globalVariables.py
def func():
    pass
```

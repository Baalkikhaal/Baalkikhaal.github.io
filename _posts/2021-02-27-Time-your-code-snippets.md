---
layout: post
author: fubar
title: "Testing performance of Python code"
tag: programming
tool: python
excerpt: "Python standard library consists timeit module that gives execution time for Python code."
date: 27th February, 2021
---

# Context
Code that computes what it is intended to compute is a first requirement of writing code. After that is accomplished, we are interested in optimizing the code in terms of readability, faster execution time.

Python focuses a lot more on [readability]({% post_url 2020-09-22-Python-Style-Guide %}) than other languages. However, it also provides datastructures to improve performance. This is roughly measured in the execution time. To measure this time, Python standard library has the [timeit](https://docs.python.org/3/library/timeit.html) module.

Let us compare the execution time to create an array of natural numbers. A simple but slower implementation is to use `list` datastructure.

```python
import timeit

N = 100 # number of naturals

def list_array():
    L = [each for each in range(N)]
    return L
```

A better alternative is to create  `numpy` arrays

```python
import numpy as np

def numpy_array():
    A = np.arange(N)
    return A
```
To compare the execution time, pass these functions as argument to `timeit()` method. This method executes the code for default N=100000 i.e. million times.
Invoke this method to time the two ways.

```python
if __name__ == '__main__':

    # timeit.timeit() method repeats the code for default
    # N=100000 i.e. million times

    # to time a function
    time_list = timeit.timeit("list_array()", setup="from __main__ import list_array")
    print(f'time for list comprehension is {time_list}')

    time_array = timeit.timeit('numpy_array()', globals=globals())
    print(f'time for numpy array is {time_array}')    
```

The console output clearly shows better performance for the latter method.
```python
time for list comprehension is 5.16344269999999
time for numpy array is 1.093457199999989
```

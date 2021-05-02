---
layout: post
author: fubar
title: "Memory management of Python built-ins"
tag: programming
tool: python
excerpt: "Python has variety of built-ins crafted for specific purposes. Some of these derive direct inspiration from mathematical theory of sets. From a programming perspective, these are handled differently internally. Let us investigate their 'static' properties."
date: 20th March, 2021
---

Let us concepts from physics to steer clear of the seemingly confusing memory management of data structures and their names.

# name

Name is a dynamic property.

# id()

Memory is a static property. It has physical basis


To get the memory id, we have `id()` method. Calling `id()` returns a 13 digit decimal number

# strings

strings are immutable sequences of characters

```python
In [34]: 'a'
Out[34]: 'a'

In [35]: id('a')
Out[35]: 2260893262704

In [36]: 'a' + 'b'
Out[36]: 'ab'

In [37]: id('ab')
Out[37]: 2260900953904

In [38]: id('b')
Out[38]: 2260893247472
```

Assigning names to the physical objects is not going to change the static property. Only that the dynamic property changes.

```python
In [41]: sa = 'a'

In [42]: id(sa)
Out[42]: 2260893262704

In [43]: sb = 'b'

In [44]: id(sb)
Out[44]: 2260893247472

In [45]: sab = 'ab'

In [46]: id(sab)
Out[46]: 2260900953904
```

# tuples

Tuples are also immutable sequences. There add more functionality than strings in that these can hold objects other than characters.

```python
In [49]: ('a',)
Out[49]: ('a',)

In [50]: type(('a',))
Out[50]: tuple

In [51]: id(('a',))
Out[51]: 2261142837712
```

Concatenating tuples leads to creation of new tuple as indicated by different memory id for the concatenated tuple

```python
In [52]: ('b',)
Out[52]: ('b',)

In [53]: id(('b',))
Out[53]: 2261142836944

In [54]: ('a',) + ('b',)
Out[54]: ('a', 'b')

In [55]: id(('a','b'))
Out[55]: 2261103945856
```

However, assigning names to tuples **does** change its static properties.

```python
In [56]: ta = ('a',)

In [57]: type(ta)
Out[57]: tuple

In [58]: id(ta)
Out[58]: 2261118428736

In [59]: tb = ('b',)

In [60]: id(tb)
Out[60]: 2261142837136

In [61]: tab = ta + tb

In [62]: tab
Out[62]: ('a', 'b')

In [63]: id(tab)
Out[63]: 2261103950976
```

This difference between the memory management of strings and tuples is further exemplified by assigning new names to the same objects as shown below

```python
In [64]: id(sa)
Out[64]: 2260893262704

In [65]: sa
Out[65]: 'a'

In [66]: sa1 = 'a'

In [67]: id(sa1)
Out[67]: 2260893262704

In [68]: ta
Out[68]: ('a',)

In [69]: id(ta)
Out[69]: 2261118428736

In [70]: ta1 = ('a',)

In [71]: id(ta1)
Out[71]: 2261118430992

In [72]: sa1 is sa
Out[72]: True

In [73]: ta1 is ta
Out[73]: False
```
`sa1` and `sa` are names referring to the same object `'a'`. Hence, calling `id()` returns the same memory location `...2704`. However, `ta1` and `ta` are names referring to different objects `('a',)` even if the objects have the same value. This is clearly indicated by calling `id()` that returns different memory locations `...8736`, `...0992`.

>Python provides `is` operator that compares the memory footprint of two names.

Clearly, the string names return `True` as they point to string object at the same memory location, whereas the tuple names return `False` as they point to string object at the same memory location.

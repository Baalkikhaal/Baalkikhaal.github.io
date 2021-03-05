---
layout: post
author: fubar
tag: programming
title: "Handling string literals in matplotlib"
excerpt: "String literals appear at various places in a plot like the labels for the axes, legend description, text annotations. They may also contain non standard unicode characters. Sometimes we need to typset mathematical formulae. Matplotlib in conjunction with Python's string literal handling lets us do these task seamlessly."
date: 05th March, 2021
---

# Context
While presenting scientific data in the form of graphs, we need to present the important parameters characterizing the data. These parameters can be of statistical nature, controls of the experiment. We need truncate these parameter values upto reasonable precision (usually 6 significant digits after the decimal is sufficient). Frequently, we need to variabilize so that changing the parameters changes the data and the graphs track these changes. f-strings and r-strings help to ease this task.

# Content

A Python [literal](https://docs.python.org/3/reference/lexical_analysis.html#literals) is a notation to describe a constant value of built-in type. Built-in types of Python are bytes, string, numeric, floating and imaginary. For example, to denote a decimal number, the notation can only include digits 0-9 and an optional dot. In this post, let us focus on the rules for string literals.

The lexical definition for a string literal is

```python
stringliteral   ::=  [stringprefix](shortstring | longstring)
stringprefix    ::=  "r" | "u" | "R" | "U" | "f" | "F"
                     | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
shortstring     ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
longstring      ::=  "'''" longstringitem* "'''" | '"""' longstringitem* '"""'
```

The syntax is to be read in such a way that that assignment of variable within `[]` is optional, `()` is mandatory, `|` separates options available.

Some valid string literals are

```python
In [152]: 'a'
Out[152]: 'a'

In [153]: "a"
Out[153]: 'a'
```
with `shortstring` syntax and

```python
In [156]: """a"""
Out[156]: 'a'

In [157]: '''a'''
Out[157]: 'a'
```
with `longstring` syntax.

Now coming to optional prefix `stringprefix`. There are two broad categories: the raw and formatted string literals

## Raw string literals

Usually the above notations are sufficient for typical situations. However there are some special sequence of characters usually starting with backslash `\` that have special meaning. These sequence of characters are called **escape sequences**. Some of these escape sequences and their functions are


 escape sequence | action
 --- | ---
 \n    | end of line
 \t    | tab   

If our string contains his sequence, and we don ot want initiate the corresponding actions, we need to prefixed the notation with `r` or `R`. This string literal defines a **raw string**.

```python
In [158]: '\n'
Out[158]: '\n'

In [159]: r'\n'
Out[159]: '\\n'
```

## Formatted string literals alias f-strings

[Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals) are a relatively new addition (version 3.6 onwards) to format strings. It was proposed in [PEP498](https://www.python.org/dev/peps/pep-0498/#id2) titled **Literal String Interpolation** to improve upon previous string formatting methods like

- %-formatting
- str.format()

 In the context of plotting, strings formatting task include
-
- adding whitespaces prior or later to string for justified values in tabular output.
- truncating the significant digits of floating point numbers for easier reading.

f-strings share the same syntax as regular string literals.

> While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

To evaluate these expressions are f-strings have `replacement fields` to hold the variables that can be interspersed within character sequences. The replacement fields are enclosed withing `{}` as in

```python
In [29]: print(f'{t}')
300

In [27]: t = 300

In [28]: print(f'T = {t} K')
T = 300 K

In [30]: print(f'{t=}')
t=300
```
The third variant directly prints the expression name along with its value if ending with `=` (version 3.8 onwards). This is useful while debugging.

[Format Specification Mini language](https://docs.python.org/3/library/string.html#format-specification-mini-language)

[Pyformat](https://pyformat.info/)

## Formatted raw strings fr'{}'

The motivation for writing this post came after reading this [SO post](https://stackoverflow.com/a/58302703/2830552)    

## String literals in Matplotlib

Frequently, we use Greek characters to denote physical quantities. We can use unicode sequence for these character

```python
plt.figure()
plt.xlabel('\u03bb (in nm)')
```

Additionally, we need to add mathematical expressions also. To write [mathematical expressions in matplotlib](https://matplotlib.org/stable/tutorials/text/mathtext.html), there are two ways:

- using `mathtext`, an inbuilt TeX parser.
- [text rendering with LaTeX](https://matplotlib.org/stable/tutorials/text/usetex.html?highlight=latex)

The `mathtext` way is easier. It requires, however, to use raw strings with math text enclosed within `$`

```python
plt.figure()
plt.ylabel(r'$\omega$ (in THz)')
```
<img src="/assets/images/Matplotlib/stringLiteralsInMatplotlib.png" alt="string-literals-in-matplotlib" width="300"/>

The LaTeX way adds for flexibility and aesthetics at the expense of additional set up of a working LaTex installation.

```python
import matplotlib.pyplot as plt
# use custom style sheet
mpl.style.use('myMatplotlibStylesheet.mplstyle')
# use LaTeX rendering
mpl.rcParams['text.usetex']=True

plt.figure()
plt.xlabel(r'$\lambda$ (in nm)')
plt.ylabel(r'$\omega$ (in THz)')
```

<img src="/assets/images/Matplotlib/stringLiteralsInMatplotlibLaTeX.png" alt="string-literals-in-matplotlib-LaTeX" width="300"/>

From [text rendering with LaTeX]()
> Certain characters require special escaping in TeX, such as
> # $ % & ~ _ ^ \ { } \( \) \[ \]

So in the LaTeX mode, using unicode characters will not work

# Conclusion

Formatted raw 'fr'-strings are a pleasant improvement in the string formatting capability of Python version 3.8 onwards when dealing with scientific data.

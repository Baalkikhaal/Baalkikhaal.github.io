---
layout: post
author: fubar
title: "Matplotlib configuration parameters"
tag: programming
tool: matplotlib
excerpt: "Let us look at how to access the configuration parameters and update them for customizing matplotlib plots."
date: 21st March, 2021
---

# Access the `rcParams`

Matplotlib has various plot parameters and offers freedom to tweak them. For default settings, matplotlib uses a configuration file called `rcParams` in colloquial language for setting default values to these parameters. The file is located at [1][1]

> INSTALL/matplotlib/mpl-data/matplotlibrc, where INSTALL is something like /usr/lib/python3.7/site-packages on Linux, and maybe C:\Python37\Lib\site-packages on Windows.

We also can get the file location of the file by

```python
import matplotlib as mpl
mpl.matplotlib_fname()
```

[1]:https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-matplotlibrc-file

The params are listed in a **dictionary-like** object `mpl.rcParams` as key-value pairs for each parameter and its default value.

```python
type(mpl.rcParams)
matplotlib.RcParams

type(mpl.rcParams) is dict
False
```
Though `mpl.rcParams` is not exactly a dictionary, it is dictionary-like. As a result, the dictionary methods are applicable. For example, to list the available keys, use

```python
print(mpl.rcParams.keys)
RcParams({...,
          'font.size': 8.0,
          'font.stretch': 'normal',
          'font.style': 'normal',
          'font.variant': 'normal',
          'font.weight': 'bold',
          ...,
          })

len(mpl.rcParams.keys())
305
```
>There are more than 300 keys!

The keys are categorized logically into

```python
## Matplotlib configuration are currently divided into following parts:
##     - BACKENDS
##     - LINES
##     - PATCHES
##     - HATCHES
##     - BOXPLOT
##     - FONT
##     - TEXT
##     - LaTeX
##     - AXES
##     - DATES
##     - TICKS
##     - GRIDS
##     - LEGEND
##     - FIGURE
##     - IMAGES
##     - CONTOUR PLOTS
##     - ERRORBAR PLOTS
##     - HISTOGRAM PLOTS
##     - SCATTER PLOTS
##     - AGG RENDERING
##     - PATHS
##     - SAVING FIGURES
##     - INTERACTIVE KEYMAPS
##     - ANIMATION
```

If we want to get the value of a particular key, use

```python
mpl.rcParams.get('font.size')
8.0
```

Now if we need to change the value of a particular key, use

```python
mpl.rcParams['font.size'] = 10.0
```
Sometimes, we need change more than a single key-value pair. In such a sitution, create a dictionary of these pairs, and pass to  `update()` method.

```python
dictLaTeX = {'text.usetex' : True, "text.latex.preamble": r"\usepackage{amsmath}" }
mpl.rcParams.update(dictLaTeX)
```

# Different `rcParams` file

After optimizing the keys, we want to have a repeatable behaviour across all the scripts. Instead of updating the keys per script, we can [use our own matplotlibrc file][2] in a different `rcParams` file. The original file is at

[2]: https://matplotlib.org/stable/tutorials/introductory/customizing.html#defining-your-own-style`

```python
mpl.matplotlib_fname()
'd:\\databases\\pythonprojects\\numscimat\\env\\lib\\site-packages\\matplotlib\\mpl-data\\matplotlibrc'
```

A portion of the file corresponding to LaTeX keys reads

```python
## ***************************************************************************
## * LaTeX                                                                   *
## ***************************************************************************
## For more information on LaTex properties, see
## https://matplotlib.org/tutorials/text/usetex.html
#text.usetex: False  # use latex for all text handling. The following fonts
                     # are supported through the usual rc parameter settings:
                     # new century schoolbook, bookman, times, palatino,
                     # zapf chancery, charter, serif, sans-serif, helvetica,
                     # avant garde, courier, monospace, computer modern roman,
                     # computer modern sans serif, computer modern typewriter
                     # If another font is desired which can loaded using the
                     # LaTeX \usepackage command, please inquire at the
                     # matplotlib mailing list
#text.latex.preamble:   # IMPROPER USE OF THIS FEATURE WILL LEAD TO LATEX FAILURES
                        # AND IS THEREFORE UNSUPPORTED. PLEASE DO NOT ASK FOR HELP
                        # IF THIS FEATURE DOES NOT DO WHAT YOU EXPECT IT TO.
                        # text.latex.preamble is a single line of LaTeX code that
                        # will be passed on to the LaTeX system. It may contain
                        # any code that is valid for the LaTeX "preamble", i.e.
                        # between the "\documentclass" and "\begin{document}"
                        # statements.
                        # Note that it has to be put on a single line, which may
                        # become quite long.
                        # The following packages are always loaded with usetex, so
                        # beware of package collisions: color, geometry, graphicx,
                        # type1cm, textcomp.
                        # Adobe Postscript (PSSNFS) font packages may also be
                        # loaded, depending on your font settings.
```

Let us copy this file to the project working directory `pwd` and modify lines corresponding to LaTeX keys to

```python
text.usetex: True
text.latex.preamble: r"\usepackage{amsmath}", # for the align enivironment
```

To use this file, we need to **reload** the matplotlib package as it has already been configured to use the default `rcParams` file. We use `reload()` method from `importlib` built-in module

```python
pwd
'E:\\Databases\\CheggProjects\\NuclearShellTemperature'

mpl.matplotlib_fname()
 'd:\\databases\\pythonprojects\\numscimat\\env\\lib\\site-packages\\matplotlib\\mpl-data\\matplotlibrc'

from importlib import reload

reload(mpl)
<module 'matplotlib' from 'd:\\databases\\pythonprojects\\numscimat\\env\\lib\\site-packages\\matplotlib\\__init__.py'>

mpl.matplotlib_fname()
'E:\\Databases\\CheggProjects\\NuclearShellTemperature\\matplotlibrc'
```

# Use custom stylesheet

Instead of using a custom `matplotlibrc` file, we can [use a custom stylesheet][3] that contains only the optimized keys.

Instead of writing down all the keys, the file contains key-value pairs of only the ones we want to change. On importing the style file, the values of the **default** `rcParams` get updated.

[3]: https://matplotlib.org/stable/tutorials/introductory/customizing.html#defining-your-own-style

>It is necessary that file has extension `.mplstyle`.

A portion of the file `mystyle.mplstyle` reads
```python

#text-font parameters

font.family : Arial
font.size : 8.0
font.weight : bold

#math-font parameters
mathtext.fontset : cm
mathtext.default : regular

#LaTeX parameters
text.usetex : True
text.latex.preamble: r"\usepackage{amsmath}", # for the align enivironment
```

>Before importing the `.mplstyle` file, we assume there is no file named `matplotlibrc`.

To use this custom style sheet,

```python
mpl.style.use('myMatplotlibStylesheet.mplstyle')
```


# References

[Customize matplotlib style sheet](https://matplotlib.org/stable/tutorials/introductory/customizing.html)

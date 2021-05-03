# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:19:07 2021

@author: fubar

Aligning equations in ax.text() using align environment

Reference:
    https://stackoverflow.com/questions/30515888/align-latex-math-text-in-matplotlib-text-box
    Using `eqnarray environment produces under par results
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('default')        # to reset any previous
# changes done in the current console that are not taken
# into account by the custom stylesheet
mpl.style.use('myMatplotlibStylesheet.mplstyle')


custom_preamble = {
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath}", # for the align enivironment
    }

mpl.rcParams.update(custom_preamble)

fig, ax = plt.subplots()
ax.set_label('x')
ax.set_ylabel('y')

ax.text(0.3, 0.6, r'array environment')
ax.text(0.3, 0.5, r"$$ |x| = \left\{ \begin{array}{rl} -x & \text{if } x < 0,\\ 0 & \text{if } x = 0,\\ x & \text{if } x > 0. \end{array} \right. $$", transform= ax.transAxes)

ax.text(0.2, 0.3, r'align environment')
ax.text(0.2, 0.2, r"\begin{align}f(x) &=  \sin x \\ &= \sin^2 (x) \end{align}", transform= ax.transAxes)

ax.text(0.2, 0.9, r'eqnarray environment')
ax.text(0.2, 0.8, r"\begin{eqnarray*}f(x) &=  \sin x \\ &= \sin^2 (x) \end{eqnarray*}", transform= ax.transAxes)

fig.savefig('alignEnvironmentInMatplotlib.png')
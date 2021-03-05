# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:14 2021

@author: fubar

Linear regression using scipy routines

Reference
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
"""

import numpy as np
from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('myMatplotlibStylesheet.mplstyle')



x1D = np.arange(-10, 11, 1)

# generate error1D random numbers array
# of uniform distribution in [-1, 1)
error1D = np.random.uniform(-1, 1, 21)

# y 1D array
y1D = 2.0 * x1D + error1D

# linregress() methods returns linregressResult instance
# with attributes slope, intercept, rvalue, pvalue, stderr,
# intercept_stderr

result = stats.linregress(x1D, y1D)

#print the results in tabular format with 6 significant digits
# after decimal and adjustable whitespace/padding so that total length  of the string for each replacement is 10 characters long
# we use the format specifier mini language so that the format 
# specifier is {:10.6f}

# Reference: https://docs.python.org/3/library/string.html#format-specification-mini-language

p = 'Parameter'
v = 'Value'
e = 'Error'

p1 = 'Slope'
p2 = 'Intercept'
p3 = 'r-value'
p4 = 'p-value'

# align the first column to the left {:10} 
# default alignment is left for strings
# whilst the second and third column to the rgight {:>10}
# Reference:
# https://pyformat.info/#string_pad_align

# list of f-strings
list_s = [30*'=',
          f'{p:10}{v:>10}{e:>10}',
          '-'*30,  # default alignment is right for numbers
          f'{p1:10}{result.slope:10.6f}{result.stderr:10.6f}',
          f'{p2:10}{result.intercept:10.6f}{result.intercept_stderr:10.6f}',
          f'{p3:10}{result.rvalue:10.6f}',
          f'{p4:10}{result.pvalue:10.6f}',
          '='*30
          ]
# string for parameters
params_s = ''
for each in list_s:
    params_s += f'{each}\n'
    print(each)
    
# plot the data and fit with linear regression

fit1D = x1D * result.slope + result.intercept

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x1D, y1D, 'o', label='data')
ax.plot(x1D, fit1D, '-', label='fit')
ax.legend()
# ALERT! It is required to use monospace font for proper
# indenting of the columns.
ax.text(0.3, 0.0, params_s, transform = ax.transAxes, fontsize = 6, family = 'monospace', usetex = False)
fig.savefig('linearRegression.png')







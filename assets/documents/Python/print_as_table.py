# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:37:30 2021

@author: fubar

title: Format a 2D list as a table.

excerpt: We explore different ways to format a 2D list as table:
- Index the rows and columns using for loops.
- Map a custom formatter to the elements of a row using `map()` built-in method.
- Extend the above implementation by defining the custom formatter in-line using `lambda`.

"""

# %% Global flags.

debug = False

# %% Function definition.

def transpose_list(_list):
    """
    Transpose a 2D list.
    """
    # Get the shape of list.
    ncols, nrows = len(_list), len(_list[0])
    # Initialize empty list.
    list_transpose = []
    # Append empty lists to store rows.
    for i in range(nrows):
        list_transpose.append([])
        # Append column element to row.
        for j in range(ncols):
            list_transpose[i].append(_list[j][i])
    if debug: print('transpose of list is')
    if debug: print(list_transpose)
    return list_transpose

# %% Test the above function.

_list = [[1, 2], [3, 4]]

transpose_list(_list)

# %% Print formatted table (versions).

def formatter_loop(_list, padding):
    """
    Print the `_list` with formatting
    such as flexible `padding`
    """
    if debug: print('Formatting by formatter_loop()')
    for row in _list:
        # Initialize an empty formatted-row-string 
        formatted_row_string = ''
        for col in row:
            # Format the column.
            formatted_col = f'{col:>{padding}}'
            # Concatenate to formatted-row-string.
            formatted_row_string += formatted_col
        # Print the formatted-row-string.
        print(formatted_row_string)


def formatter_map(_list, padding):
    """
    Use functional programming tools `map()` to condense
    the code.
    """
    if debug: print('Formatting by formatter_map()')
    # Get the number of columns.
    ncols = len(_list[0])
    # Define list of paddings.
    paddings = [padding for i in range(ncols)]
    # Define custom str() method to return formatted string
    def my_str(_str, padding):
        """
        Format `_str` with flexible `padding`.
        """
        return f'{_str:>{padding}}'

    for row in _list:
        # Map `my_str()` to the iterable `row`.
        # The return is an iterable of strings.
        # Interleave the strings with `join()` of empty string ''.
        print(''.join(map(my_str, row, paddings)))


def formatter_lambda(_list, padding):
    """
    Let us circumvent the limitation in version 3 of not able
    to provide `padding` as an argument by using lambda function.
    `map()` requires a function object as the first argument.
    `lamda` can take more than one argment and return a function object on the fly (runtime). Let us club these tools to avoid
    the `def` statement of helper function mystr().
    """
    if debug: print('Formatting by formatter_lambda()')
    # Get the number of columns.
    ncols = len(_list[0])
    # Define list of paddings.
    paddings = [padding for i in range(ncols)]
    for row in _list:
        print(''.join(map(lambda _str, padding: f'{_str:>{padding}}', row, paddings)))


# %% Test the above functions.

header = [
            ['NN', 'act. fn.', 'cost fn.', 'optimizer'],
            ['Sequential', 'linear', 'quadratic', 'none'],
            ['Convolutional', 'sigmoid', 'softmax', 'adam'],
            ['Autoencoder', 'ReLU', '', ''],
         ]

print('='*15)
print('Using version 1')
print('='*15)
formatter_loop(header, 12)

print('='*15)
print('Using version 2')
print('='*15)
formatter_map(header, 15)

print('='*15)
print('Using version 3')
print('='*15)
formatter_lambda(header, 18)
# %% Print as table.

def print_as_table(header, data, padding=10, **kwargs):
    """
    Print 2D list of `data` along with a top `header`
    and LaTeX like line separators.
    Every column of `data` and `header` is a logical entity.
    Also additional keyword arguments can be specified.
    'formatter': which formatter to use.
        Options are
        'formatter_loop', 'formatter_map', 'formatter_lambda'.
    """
    # Dictionary of formatters.
    dict_formatters = {'formatter_loop': formatter_loop,
                       'formatter_map': formatter_map,
                       'formatter_lambda': formatter_lambda
                       }
    # Fetch the keyword arguments.
    # And assign function conditionally
    # For more info,
    # check Section "Apply functions generically"
    # of Chapter "Arguments" of 
    # "Mark Lutz's Learning Python."
    if kwargs.get('formatter'):
            formatter = dict_formatters[kwargs.get('formatter')]
    else:
        formatter = dict_formatters['formatter_loop']

    # Get the number of columns
    ncols = len(data)
    # Print double line separator.
    print("="*padding*ncols)
    # Get the transpose of header.
    header_transpose = transpose_list(header)
    # Print the header.
    formatter(header_transpose, padding)
    # Print single line separator.
    print('-'*padding*ncols)
    # Get the transpose of data
    data_transpose = transpose_list(data)
    formatter(data_transpose, padding)
    # Print double line separator.
    print("="*padding*ncols)


# %% Test the above function.

header = [['linear scale'],
          ['log scale'],
          ['logit scale']
          ]
formats = [['IndexFormatter', 'NullFormatter', 'FixedFormatter', 'FuncFormatter', 'FormatStrFormatter', 'StrMethodFormatter', 'OldScalarFormatter', 'ScalarFormatter'],
            ['LogFormatter', '', '', '', '', '', '', ''],
            ['LogitFormatter', '', '', '', '', '', '', '']
          ]


print_as_table(header, formats, 18, formatter='formatter_loop')

print_as_table(header, formats, 18, formatter='formatter_map')

print_as_table(header, formats, 18, formatter='formatter_lambda')
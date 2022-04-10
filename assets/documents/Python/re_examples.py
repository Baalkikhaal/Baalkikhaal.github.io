# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:01:27 2021

@author: fubar

Regular expression module examples
"""

# %% Import statements.

import re

# %% Define functions.

def match_full_string():
    """
    Match the complete string.
    Match any character with `.`.
    """
    pattern = '.+'
    string = r'any string.'
    result = re.search(pattern, string)
    print(result)


def match_decimals():
    """
    Match the decimal numbers.
    Match a digit with `[0-9]`.
    Extend the match to more digits with `+`.
    """
    pattern = r'[0-9]+'
    string = r"Today's date is 29th March 2021."
    result = re.findall(pattern, string)
    pattern1 = r'[0123456789]+'
    result1 = re.findall(pattern1, string)
    print(f'{result=}')
    print(f'{result1=}')


def match_article_the():
    """
    Match the article 'the' in a sentence.
    """
    pattern = r'[tT]he'
    string = r"Find the occurences of the article 'the'. The sentence can start sometimes with the article."
    result = re.findall(pattern, string)
    print(f'{result=}')


def print_match(match):
    """
    Return the start and end of match object.
    """
    start = match.start()
    end = match.end()
    print(f'match at {start=} and {end=}')


def match_spaces(string):
    """
    Match the spaces in a sentence.
    Use `finditer()` method to return iterable match object.
    Use `print_match()` helper method to print
    start and end index of match.
    """
    pattern = r' '
    for match in re.finditer(pattern, string):
        print_match(match)

#%% Test function.

def test_match_spaces():
    """
    Test match_spaces().
    """
    string = 'Find the number of spaces in this sentence.'
    match_spaces(string)
    string1 = 'This is a sentence with  more than single whitespace.'
    match_spaces(string1)

# %% Print function.

def print_match_with_segments(match):
    """
    Return the start and end of match object.
    """
    # segment length prior and post the match segment
    length = 5
    segment = match.group()
    span = match.span()
    start = match.start()
    end = match.end()
    string = match.string
    before = string[start-length : start]
    after = string[end : end+length]
    print(f'match at {span=} ...{before}{segment}{after}...')

#%% Define function.

def match_valid_and_invalid_spaces(string):
    """
    Match all spaces, valid or invalid.
    """
    pattern = r' +'
    for match in re.finditer(pattern, string):
        print_match_with_segments(match)

#%% Test function.

def test_match_valid_and_invalid_spaces():
    """
    Test match all spaces, valid or invalid.
    """
    string = 'This is a sentence with  more than single whitespace.'
    match_valid_and_invalid_spaces(string)

#%% Define function.

def match_only_invalid_spaces(string):
    """
    Match only invalid spaces.
    """
    pattern = r'  +'
    for match in re.finditer(pattern, string):
        print_match_with_segments(match)

#%% Test function.

def test_match_only_invalid_spaces():
    """
    Test match only invalid spaces.
    """
    string = 'This is a sentence with  more than single whitespace. This sentence has three   whitespaces.'
    match_only_invalid_spaces(string)

#%% Define function.

def match_vowels_and_consonants():
    """
    Match vowels and consonants.
    """
    pattern_vowels = r'[aeiou]'
    string = 'abcdefghijklmnopqrstuvwxyz'
    result_vowels = re.findall(pattern_vowels, string)
    print(f'{result_vowels=}')
    pattern_consonants = r'[^aeiou]'
    result_consonants = re.findall(pattern_consonants, string)
    print(f'{result_consonants=}')


def match_invalid_spaces_at_start(string):
    """
    Match invalid spaces at the start of a sentence.
    """
    pattern = r'\.  +'
    for match in re.finditer(pattern, string):
        print_match_with_segments(match)

#%% Test function.

def test_match_invalid_spaces_at_start():
    """
    Test the function that matches invalid
    spaces at the start of a sentence.
    """
    string = 'This is a sentence with  more than single whitespace.  The start of this sentence has invaid spaces.'
    match_invalid_spaces_at_start(string)

# %% Define function.

def match_within_delimiters(string):
    """
    Match expression within '(...)' delimiters.
    Escape `(` using `\`.
    Match complement of set of characters with `[^]`.
    Extend match to more than one occurence with `+`.
    """
    pattern = r'\([^)]+\)'
    result = re.findall(pattern, string)
    print(result)

#%% Test function.

def test_match_within_delimiters():
    """
    Test match expression with '(...)' delimiters.
    """
    string = r'Pick up the ball (red one). Here is another (delimited expression). Here is a (nested (delimiter) ). Does it match empty delimited expression ()?'
    match_within_delimiters(string)

# %% Use flags 

def match_newline_as_character(string):
    """
    Match newline as any other character.

    Returns
    -------
    None.

    """
    pattern = 'START.+END'
    result = re.findall(pattern, string, flags=re.DOTALL)
    print(result)


# %% Test function.

def test_match_newline_as_character():
    """
    Test function that matches newline as character.
    

    Returns
    -------
    None.

    """
    proverb='STARTShips are safe at the harbour.\nBut thats not what they are built for.END'
    match_newline_as_character(proverb)
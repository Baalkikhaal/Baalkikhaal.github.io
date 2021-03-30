---
layout: post
author: fubar
title: "Commonly used Regular expressions"
tag: programming
tool: python
excerpt: "Let us learn the syntax and rules of evaluating regular expressions by solving commonly needed tasks."
date: 29th March, 2021
---
# Regular expression

Regular expressions (RE) are pattern identifiers used for matching patterns in strings. They have a special syntax and follow simple rules to perform simple to complex pattern matching tasks. REs are commonly used for search operations, parsing and lexical analysis. The [concept of regular expression][1] was developed by mathematician Stephen Cole Kleene as part of the theory of regular languages.

[1]: https://en.wikipedia.org/wiki/Regular_expression

# DOs

RE is itself a string that is used as a pattern identifier for match pattern in another string. As we will see soon, REs reserve special meaning to the character `\`. Since Python strings also reserves special meaning for  `\`, it is necessary to always use **raw RE strings** to avoid complicated RE strings. For the difference between simple string literal and raw string literal, refer to [my post on strings in matplotlib]({% post_url 2021-03-05-Handling-string-literals-in-matplotlib  %}).

In this post, we represent normal strings with `'normal string'` and raw string with `r'raw string'`.

# Rules

The pattern identifiers are formed using a simple set of rules. These rules when combined in various permutations and combinations can lead to increasingly complex interpretation of the RE. Some of the generic rules of generation are

## Concatenation

> If A is a RE and B is a RE, then AB is a RE.

If REs constitute a group (which it actually does), then concatenation is the group operation.

This rule of concatenation can be used to generate complex REs from simple REs.

## Simple REs

The simplest REs are single character strings like `r'a'`, `r'0'`, `r' '`. These match themselves i.e. `'a'`, `'0'`, `' '`.

Using concatenation property, we can create compound REs. So `r'ab'` matches string `'ab'`.

Now to spice up the REs, we introduce special characters that have special interpretation.

## Special characters

There are many special characters whose meaning depends on where they occur in a RE string and which RE they neighbour. Some of these characters are `r'.'`, `r'+'`, etc. However, there is even a more special characters among the special characters -- `r'\'`.

| special character | interpretation | examples |
|--------|-------|----------|
| `r'\'`  | Escapes special characters. | `r'\.'` matches `'.'`. |
| `r'.'` |  Matches any character except `NEWLINE` | `r'.'` matches `'a'` or `'0'`, etc. |
| `r'+'` | Matches one or more repetitions of the preceding RE. | `r' +'` matches whitespace of any non zero length. but `\. +` matches only whitespace of any non zero length at the start of sentence.


## Special delimiters

| special delimiter | interpretation | examples |
|--------|-------|----------|
| `r'[...]'` | Match from the set of characters. **Note:** Special characters loose their special meaning inside a set.| `r'[aeiou]'` matches any vowel. `r'[.]'` matches `'.'` |
| `r'[^...]'` | Match from the complement of set of characters.  **Note:** `r'^'` has no special meaning if it’s not the first character in the set.  | `r[^aeiou]` matches any consonant (assuming string has only alphabets). |
| `r'[0-9]'` | Match a range of characters |


# Methods

| methods | docstring |
|--------|-------|
| `re.match(pattern, string)` | Applies the `pattern` **only** at the start of the string; returns a `Match` object, or `None` if no match was found. |
| `re.search(pattern, string)` | Scans through the `string` and returns **only** the first match to the `pattern`. |
| `re.findall(pattern, string)` | Returns list of all the **non-overlapping** matches of `pattern` in `string`. |
| `re.finditer(pattern, string)` | Returns an iterator over all **non-overlapping** matches in the `string`. |

## Usage

```python
re.match(r'Hello', 'Hello, world!')
Out[129]: <re.Match object; span=(0, 5), match='Hello'>

In [130]: re.match(r'world', 'Hello, world!') is None
Out[130]: True

In [131]: re.search(r'world', 'Hello, world!')
Out[131]: <re.Match object; span=(7, 12), match='world'>

In [132]: re.findall(r'o', 'Hello, world!')
Out[132]: ['o', 'o']

In [133]: for match in re.finditer(r'l', 'Hello, world!'):
     ...:     print(match.span())
     ...:     
(2, 3)
(3, 4)
(10, 11)
```
# Examples

Let us apply some of the rules above to create REs for common tasks.

## Match the spaces in a sentence

```python
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


string = 'Find the number of spaces in this sentence.'
match_spaces(string)

match at start=4 and end=5
match at start=8 and end=9
match at start=15 and end=16
match at start=18 and end=19
match at start=25 and end=26
match at start=28 and end=29
match at start=33 and end=34
```

However, sometimes there are typos and we insert more than single whitespace between words. Let us term these invalid spaces. So an invalid space of two whitespace characters is counted twice.

```python
string1 = 'This is a sentence with  more than single whitespace.'
match_spaces(string1)

match at start=4 and end=5
match at start=7 and end=8
match at start=9 and end=10
match at start=18 and end=19
match at start=23 and end=24
match at start=24 and end=25
match at start=29 and end=30
match at start=34 and end=35
match at start=41 and end=42
```

The occurence of invalid space with two whitespace characters at index 23 is matched twice at 23 and 24 using RE `r' '`.

## Find occurrences of invalid spaces in a sentence

To match such invalid spaces only once, we can use RE `r' +'` that matches one or more of continuous whitespaces. This includes both the valid and invalid spaces.

We can use `r'+'` special character along with `r' '` to match whitespace of any non zero length. So `r' +'` RE matches even the invalid spaces.

```python
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


def match_valid_and_invalid_spaces(string):
    """
    Match all spaces, valid or invalid.
    """
    pattern = r' +'
    for match in re.finditer(pattern, string):
        print_match_with_segments(match)


string = 'This is a sentence with  more than single whitespace.'

match at span=(4, 5) ... is a ...
match at span=(7, 8) ...is is a sen...
match at span=(9, 10) ... is a sente...
match at span=(18, 19) ...tence with ...
match at span=(23, 25) ... with  more ...
match at span=(29, 30) ... more than ...
match at span=(34, 35) ... than singl...
match at span=(41, 42) ...ingle white...
```

We have used an enhanced helper function `print_match_with_segments()` to print the neighbourhood segments around the matched span. It is clear that `r' +'` matches both valid and invalid spaces. Also the double whitespace is counted as a single occurrence spanning from (23,25).

To match **only** the invalid spaces, there should be **at least** two whitespaces. The RE for at least one whitespace is `r'  +'`. Since `r'+'` checks for one or more repetition of only the immediate preceding RE, which in this case is a single whitespace `' '`, the first whitespace ensures that the match has at least two whitespaces.

```python
def match_only_invalid_spaces(string):
    """
    Match only invalid spaces.
    """
    pattern = r'  +'
    for match in re.finditer(pattern, string):
        print_match_with_segments(match)

string = 'This is a sentence with  more than single whitespace. This sentence has three   whitespaces.'
match_only_invalid_spaces(string)

match at span=(23, 25) ... with  more ...
match at span=(77, 80) ...three   white...
```



## Match the complete string

Any non empty string is made up any of the ASCII characters. `r'.'` is RE special character that matches any character except `NEWLINE`. To match one or more of any character we use `r'+'` RE. Concatenating these REs, we have `r'.+'` that matches any character one or more times resulting in matching the complete string.

```python
import re

pattern = '.+'
string_ = r'any string.'
result = re.search(pattern, string_)
print(result)

<re.Match object; span=(0, 11), match='any string.'>
```
## Find all invalid spaces at the start of the sentence

To find the invalid spaces only at the start of the sentence, the first character of the match should be `'.'`. Since `r'.'` is a special character, we shall use the RE `r'\.'`. And the RE for double or more whitespaces is `r'  +'` as discussed in [invalid spaces example](#find-occurrences-of-invalid-spaces-in-a-sentence). So the complete RE is `r'\.  +'`. Since special characters loose their meaning inside sets, we can use the equivalent RE `r'[.]  +'`.

```python
def match_invalid_spaces_at_start(string):
    """
    Match invalid spaces at the start of a sentence.
    """
    pattern = r'\.  +'
    for match in re.finditer(pattern, string):
        print_match_with_segments(match)


string = 'This is a sentence with  more than single whitespace.  The start of this sentence has invaid spaces.'
match_invalid_spaces_at_start(string)

match at span=(52, 55) ...space.  The s...
```

## Find all the decimal numbers

A number is made up of one or more digits. A digit is a charcter from 0 to 9. To match a digit, we can use a set `r'[...]'` containing the digits 0 to 9. There are two ways of listing the digits

- `r'[0123456789]'` matches a single character from 0 to 9.
- A more concise syntax is `r'[0-9]'` which uses the `-` special character. The hyphen specifies a range of characters.

To match one or more digits, we use `r'+'` as preceding example. So the RE `r'[0-9]+'` matches any decimal number.

To find all the occurrences of the RE match, use `re.findall()` method.

```python
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

match_decimals()

result=['29', '2021']
result1=['29', '2021']
```

## Finding vowels and consonants

```python
pattern_vowels = r'[aeiou]'
string = 'abcdefghijklmnopqrstuvwxyz'
result_vowels = re.findall(pattern_vowels, string)
print(f'{result_vowels=}')

result_vowels=['a', 'e', 'i', 'o', 'u']

pattern_consonants = r'[^aeiou]'
result_consonants = re.findall(pattern_consonants, string)
print(f'{result_consonants=}')

result_consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
```

## Find `'the'`s in a string.

The article `'the'` is a common occurence in English language. It can occur at the start of sentence, or in the middle of a sentence. So there are two possibilities.

- `The`
- `the`

The firt character has two choices `t` or `T`. So `r'[tT]'` RE matches this choice. Since the trailing characters are fixed, the character sequence itself can be used as RE.

So `r'[tT]he'` finds the occurrences of the article `'the'`.

```python
def match_article_the():
    """
    Match the article 'the' in a sentence.
    """
    pattern = r'[tT]he'
    string = r"Find the occurences of the article 'the'. The sentence can start sometimes with the article."
    result = re.findall(pattern, string)
    print(f'{result=}')

match_article_the()

result=['the', 'the', 'the', 'The', 'the']
```

## Find all expressions within delimiters

Commonly used delimiters are brackets `'(...)'`, `'{...}'`, `'[...]'`, `'<...>'`.

For this example, let us find expression within brackets `'(...)'`.

The first character of our match is `'('`. Since `r'('` is a special character we need to escape its special meaning by using `r'\'`. So the RE starts with `r'\('`.

Similarly as the last character of our match is `')'`, RE must end with `r'\)'`.

Now, the RE that matches any character should be a set of characters `r'[...]'`. One way to define the characters within the set is to use hyphenated ordered characters. For example, `r'[0-9A-Fa-f]'` matches a hexadecimal character. However to include even the non alphanumeric characters, we can use complement of set `r'[^]'` that matches all the ASCII characters. However, we need to exclude the closing delimiter `')'`. So the RE that matches all characters except `')'` is `r'[^)]'`.

> Here we are assuming that the nesting of brackets is legal.

Now we do not know *apriori* the number of characters within the delimiters. The only constraint is there should be at least one character. To match one or more characters we use `r'+'`. It matches one or more repetitions of the RE preceding the `r'+'`. In this case the preceding RE is the complete RE within the delimiters `r'[^)]'`. So the RE matching more than one character except `')'` is `[^)]+`.

Therefore, the complete RE for matching any expression within the delimiters `'(...)'` is `r'\([^)]+\)'`.

```python
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


string = r'Pick up the ball (red one). Here is another (delimited expression). Here is a (nested (delimiter) ). Does it match empty delimited expression ()?'
match_within_delimiters(string)

['(red one)', '(delimited expression)', '(nested (delimiter)']
```

It is to be noted from above example, that the RE does not account correctly for nested delimiters as well as *empty* delimiters.

# Summary

So we have applied some of the basic rules of REs and used some of the special characters and special delimiters. Let us review some of the intermediate rules, characters and delimiters in a later post.

# File Downloads

[re_examples.py](/assets/documents/Python/re_examples.py)

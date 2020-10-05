---
layout: post
author: fubar
tag: programming
title: "How to render LaTeX equations using MathJax?"
excerpt: "A quick hack to render LaTeX equations in HTML pages using MathJaX"
date: 05th October, 2020
---

## What is MathJaX?

[MathJax](https://www.mathjax.org/) is a Javascript display engine for mathematics that works in all browsers. To enable
Add the MathJax script to the head of the html for the current site.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Test Site</title>

        <!-- Add MathJax rendering for LaTeX style rendering -->

        <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

        <!-- MathJax rendering configuration ends here  -->
    </head>
    <body>
        test body        
    </body>
</html>
```

## Block line equation

To typset a block line equation, like

$$ \exp^{i \pi} = -1, $$

use

    $$ \exp^{i \pi} = -1, $$

Even delimiters `\\[ \\]` can also be used instead of `$$ $$`.

## Inline equation

To typeset inline equation,

The function \\( f(x) \\) returns the value 0 if even.

use

    The function \\( f(x) \\) returns the value 0 if even.

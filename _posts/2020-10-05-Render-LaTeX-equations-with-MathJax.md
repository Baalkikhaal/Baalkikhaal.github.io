---
layout: post
author: fubar
title: "How to render LaTeX equations using MathJax?"
tag: programming
tool: javascript
excerpt: "A quick hack to render LaTeX equations in HTML pages using MathJaX"
date: 05th October, 2020
---

## What is MathJaX?

- [MathJax](https://www.mathjax.org/) is a Javascript display engine to display mathematics notation on web browsers.
- It processes mathematics given in LaTeX and MathML notation and renders them in web-based fonts that scale at high resolution without distortion.
- MathML is the WWW consortium's standard for displaying mathematics on web browsers. MathJaX is a pre-processor that converts TeX and LaTeX notation into MathML.
- MathJaX 2.0 has new features like equation numbering.

## Enable MathJaX

- There are two ways to enable MathJaX processing of mathematics notation.
  - Link our webpages to an installation of MathJaX hosted on a Content Delivery Network (CDN).
  - Link our webpages to a local installation of MathJaX

- The former is a convenient option for beginners. Add the MathJax script to the head of the html for the current site.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Test Site</title>

        <!-- Add MathJax rendering for LaTeX style rendering -->

        <script type="text/javascript" async
			src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.5.3/MathJax.js?config=TeX-MML-AM_CHTML">
		</script>

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

## Activate MathJaX in Jekyll powered site

The MathJaX Javascript can be added to a Jekyll powered site by [using Jekyll's Liquid tags](https://xkdog.github.io/2017-02-06-mathjax/.

- Define a `mathjax.html` file containing the line

```html
 <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
```
and include it in the `_html` folder at the root of the Jekyll site source.

- Now in the markdown file for the post add the following Jekyll preprocessor statement

```jekyll
{% include mathjax.html %}
```
In this way, mathjax can be enabled on a per post basis

- Alternatively, if you use a jupyter notebook, the above line can be added as a cell with the cell type as `RawNBConvert` with a new line above and below.

```jekyll

{% include mathjax.html %}

```

The second option has been implemented in the [my notebooks on Spintronics review](https://baalkikhaal.github.io/Spintronics/).


## References

For more information on how to use MathJax, and its latest features, refer to the [canonical documentation on MathJax](https://docs.mathjax.org/en/v2.5-latest/index.html)
---
layout: post
author: fubar
title: "Programmatic access with Jekyll"
tag: programming, architecture
tool: jekyll
excerpt: "Jekyll leverages Liquid filters and tags to provide programmatic access to variety of elemetns of a static website built using Jekyll."
date: 12th April, 2022
---

## Abstract

In the [introductory post on Jekyll]({% post_url 2019-10-13-Building-Jekyll-website %}),
we discussed how to build static websites using Jekyll.
The HTML source of the websites can be generated iteratively if the relevant data is categorized logically.
Once the data is logically separated, we can define templates that define the structure of theses pages.

Using [YAML](yaml.org/) programming language, iterative data can be accessed from within Jekyll and corresponding act upon it.

In this post, we shall describe the extended features of Jekyll
where the content of the webpage itself can be programatically accessed and changed.
Jekyll leverages [Liquid](https://shopify.github.io/liquid/basics/introduction/) language features.

## Architecture of Jekyll

If we take the analogy of civil engineering, the website is like a high rise tower,
template files act as beams and pillars of the website, whereas the data act as bricks.
Jekyll plays the role of a tower-crane to grab the bricks and place them to across the length, breadth and height.

Therefore, we need to come up with a layout before we start building up. Just as the layout,
 also called the master plan or blue-print,
 is first drawn out, we must design the layout of the website.
 In this process, numerous design decisions need to be made like
 
- the kind of content,
- the presentation of the content,
- the categorization of content,
- the relationship between the categories,
- style of the content

For example, the data of the current website can be categorized into posts, tags, etc.
These can be defined in the "hidden" directories with names starting with "_" like `_posts`, `_data/tags.yml`, etc.
Jekyll can then be asked to crawl over these directories to fetch the content.

Further, these categories can have different presentations; these presenations can be defined in corresponding template files.
Using these template files, Jekyll can then populate these with the fetched content.


## Liquid - Jekyll under the hood

Alternatively, if we look at the webpage as a unit, its content can be broadly categorized into 

- static content that defines the structure of the webpage and acts as a template, and
- dynamic content that fills the template leading to the actual webpage.

While the static content can be handled by `HTML`, the dynamic content needs a template language.
A template language compiles the source file, looks for the placeholders of the dynamic content,
preprocesses and replaces it with actual HTML elements in the final html.
[PHP](https://www.php.net/) can be used for the task.

However, Jekyll uses the [Liquid](https://www.rubydoc.info/gems/liquid/5.3.0) [template](https://shopify.dev/api/liquid) [language](https://shopify.github.io/liquid/).

While most of the times the fate of the dynamic content is to simply output to the website source, sometimes logical operations need to be performed on it.

Liquid provides two kinds of elments for processing the dynamic content

- output objects delimited by {% raw %} {{  }} {% endraw %}.
- logic objects delimited by {% raw %} {%  %} {% endraw %}.

The logic are further classified into into

- tags
- filters

### Objects

While some of the objects are **reserved** to Jekyll, others can be user defined.
Also, objects have attributes that can be accessed using  `object.attribute` syntax.

| Reserved Objects | Object attributes |
|-----|----|
| site | site.url, site.baseurl |
| page | user-defined |

To output the site,

{% raw %}

	The url of this webpage is {{ site.url }} and baseurl is {{ site.baseurl }}.

{% endraw %}

The output is

	The url of this webpage is {{ site.url }} and baseurl is {{ site.baseurl }}.	

	
In the case of `page`, we can add new attributes to the reserved objects in the front matter of a webpage that Jekyll pre-processes.

For example, the present webpage has the following front matter

{% raw %}

	---
	layout: post
	author: fubar
	title: "Programmatic access with Jekyll"
	tag: programming, architecture
	tool: jekyll
	excerpt: "Jekyll leverages Liquid filters and tags to provide programmatic access to variety of elemetns of a static website built using Jekyll."
	date: 12th April, 2022
	---

{% endraw %}

In order to access, the title of the page, we use {% raw %} {{ page.title }} {% endraw %} object.

{% raw %}

	The title of this webpage is {{ page.title }}.

{% endraw %}

So that the result is

	The title of this webpage is {{ page.title }}.
	
Alternatively, objects can also be defined within the dynamic content using tags.
Tags provide provide control over the logic governing the content.
Here, let us use {% raw %} {% assign %} {% endraw %} tag to assign value to a variable.


{% raw %}

	{% assign date = page.date %}
	This page was published on {{ date }}.

{% endraw %}

	{% assign date = page.date %}
	This page was published on {{ date }}.

As we mostly deal with strings, Liquid offers filters to perform string manipulations.
The filter tag is recognized by the  `|` pipe that filters output through the pipe
after necessary manipulations have been performed.

For example, to output the year, time and timezone separately, we use the `split` filter 
that requires a separator argument. In this case it is whitespace ` `.
 
{% raw %}

	{% assign splits = date | split: " " %}
	{% for split in splits %}
		{{ split }}
	{% endfor %}

{% endraw %}

The output is

	{% assign splits = date | split: " " %}
	{% for split in splits %}
	{{ split }}
	{% endfor %}

Here, we have used the `for` loop to iterate over the splits.



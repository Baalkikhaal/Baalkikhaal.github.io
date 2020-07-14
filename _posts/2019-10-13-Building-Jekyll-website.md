---
layout: post
author: fubar
title: "What is Jekyll?"
tag: programming
tool: jekyll
excerpt: "An introduction to Jekyll, an awesome static website generator."
date: 13th October, 2019
---

<div>
<img src="{% link /assets/images/Jekyll/jekyllLogo.svg %}"
alt="jekyll-logo"
width = 150px >
</div>

![jekyll-logo]({% link /assets/images/Jekyll/jekyllLogo.svg %})

{% if page.tool %}
    {% for tool in site.data.tools %}
        {% if tool.name == page.tool %}
            <!--- ![{{ tool.alt }}]({{ tool.link }}) --->
![jekyll-logo]({% link /assets/images/Jekyll/jekyllLogo.svg %})
        {% endif %}
    {% endfor %}
{% endif %}

# Abstract

Jekyll is a static site generator. It gives programmatic access to the various tools used for creating static websites. With a prime focus on handling static content, Jekyll, a Ruby gem provides objects to handle various elements present in a web page like
- content structuring by the use of content asset variablizing (posts, interlinking and intra-linking between and within posts, authors, layout, includes, data, support for Markdown),
- content styling by the use of style asset variablizing  (CSS, SCSS, SASS) and
- multimedia asset handling by the use of global placeholders (for images, Java Scripts)

![Jekyll the Content Keeper](/assets/images/static-assets.svg "Image taken from ... ")

Find the source of the above image #TODO

## What is a static website?
In simple terms, static websites are read only websites. The tools required for such websites include but not limited to the standard web tools like HTML, CSS, JS. Historically, static websites generation involved tools used for making complex websites like databases for content handling, preprocessors for generating the HTML content using PHP, serving the content using server all combined in a package called LAMP (Linux Apache MySQL PHP), WAMP (Windows Apache MySQL PHP). Howver, this posed high maintenance overhead in terms of security, upgradation. As a website administrator, a simple no-frills solution with source code based on simple text files was a great boon. Jekyll is one among the new generation of static site generators.

## What is a dynamic website?
Responsive websites which have forms, have preprocessing tools liks PHP

---

## What Jekyll is **not**?

Jekyll cannot generator responsive websites. Webpages that enable server side heavy duty programming tasks like cloud computation (what it is #TODO), graphic rendering. As such, it is intended to make websites which are read only, journal keeping as typical in  the case of Wordpress-based webpages.

Responsiveness from readers can be added in the form of widgets like Disqus widgets. which essentially is a link to the disqus server that does the processing. My feeling is that a java script handles such responses.

In that way, Jekyll can partially generate responsive websites with the help of JS

---

## Which Jekyll?

Jekyll v4 is production ready using HTML5, CSS3 and JS(version ?).

---

## Why Jekyll? Why not others?

Other static generators like Python based Zim Desktop wiki also generate static sites. However Jekyll offers a seamless integration of desktop and web interfaces in the form of support for Markdown, version control using Git and easy deployment to GitHub for web hosting, and content editing using Atom text editor.

---

## What are static assets?

HTML, CSS, JS

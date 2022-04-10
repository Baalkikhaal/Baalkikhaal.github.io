---
title: Architecture Posts
---

<ul>
    {% for post in site.posts %}
        {% if post.tag == "architecture" %}
            <li>
                <a href="{{ post.url }}">{{ post.title }}
                </a>
            </li>
        {% endif %}
    {% endfor %}
</ul>

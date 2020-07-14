---
title : Programming Posts
---

<ul>
    {% for post in site.posts %}
        {% if post.tag == "programming" %}
            <li>
                <a href="{{ post.url }}">{{ post.title }}
                </a>
            </li>
        {% endif %}
    {% endfor %}
</ul>

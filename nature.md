---
title : Nature Posts
---

<ul>
    {% for post in site.posts %}
        {% if post.tag == "nature" %}
            <li>
                <a href="{{ post.url }}">{{ post.title }}
                </a>
            </li>
        {% endif %}
    {% endfor %}
</ul>

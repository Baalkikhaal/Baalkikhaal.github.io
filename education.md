---
title : Education Posts
---

<ul>
    {% for post in site.posts %}
        {% if post.tag == "education" %}
            <li>
                <a href="{{ post.url }}">{{ post.title }}
                </a>
            </li>
        {% endif %}
    {% endfor %}
</ul>

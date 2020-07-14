---
title : Yoga Posts
---

<ul>
    {% for post in site.posts %}
        {% if post.tag == "yoga" %}
            <li>
                <a href="{{ post.url }}">{{ post.title }}
                </a>
            </li>
        {% endif %}
    {% endfor %}
</ul>

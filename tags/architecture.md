---
title: Architecture Posts
---

From the source code of [the mother fucking website](https://motherfuckingwebsite.com/),

> Good design is as little design as possible.
> - some German motherfucker.

<ul>
    {% for post in site.posts %}
		{% assign tags = post.tag  | split: ", " %}
		{% for tag in tags %}
			{% if tag == "architecture" %}
				<li>
					<a href="{{ post.url }}">{{ post.title }}
					</a>
				</li>
			{% endif %}
		{% endfor %}
    {% endfor %}
</ul>



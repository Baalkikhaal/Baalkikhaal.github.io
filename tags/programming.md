---
title : Programming Posts
---

<ul>
    {% for post in site.posts %}
		{% assign tags = post.tag  | split: ", " %}
		{% for tag in tags %}
			{% if tag == "programming" %}
				<li>
					<a href="{{ post.url }}">{{ post.title }}
					</a>
				</li>
			{% endif %}
		{% endfor %}
    {% endfor %}
</ul>

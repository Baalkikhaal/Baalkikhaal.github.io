---
title : Scipy Posts
---

<ul>
    {% for post in site.posts %}
		{% assign tools = post.tool  | split: ", " %}
		{% for tool in tools %}
			{% if tool == "scipy" %}
				<li>
					<a href="{{ post.url }}">{{ post.title }}
					</a>
				</li>
			{% endif %}
		{% endfor %}
    {% endfor %}
</ul>

---
title : PhD Posts
---

<ul>
    {% for post in site.posts %}
		{% assign tools = post.tool  | split: ", " %}
		{% for tool in tools %}
			{% if tool == "phd" %}
				<li>
					<a href="{{ post.url }}">{{ post.title }}
					</a>
				</li>
			{% endif %}
		{% endfor %}
    {% endfor %}
</ul>

---
layout: default
title: Credentials
---

# My projects


{% for item in site.data.projects %}
<div class="project">
	<h3>
		{{ item.name }}
	</h3>
	<p>
		{{ item.description }}
	</p>
</div>
<div class="project-image">
	<img src="{{ item.image }}" alt="{{ item.alt }}"/>
</div>
<div class="project-reference">
	<p>
		For more details, please refer to
		<a
			href="{{ item.link }}" {% if page.url == item.link %}class="current"{% endif %}>
			{{ item.name }} Github repository
		</a>
		.
	</p>
</div>
{% endfor %}


## Résumé

[Résumé](/assets/documents/Resume/resume_sreekar.pdf)
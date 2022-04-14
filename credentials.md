---
layout: default
title: Credentials
---

## Projects


{% for item in site.data.projects %}
<div class=project>
	<h3>
		{{ item.name }}
	</h3>
	<p>
		{{ item.description }}
	</p>
</div>
<div class=project-reference>
	<p>
		For more details, refer to
		<a
			href="{{ item.link }}" {% if page.url == item.link %}class="current"{% endif %}>
				<!-- comment out the image hrefs
				<img src="{{ item.image }}" alt="{{ item.alt }}"/>
				-->
			{{ item.name }}
		</a>
	</p>
</div>
{% endfor %}


## Résumé

[Résumé](/assets/documents/Resume/resume_sreekar.pdf)
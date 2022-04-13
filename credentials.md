---
layout: default
title: Credentials
---

## Projects

<div class=project>
  {% for item in site.data.projects %}
    <h3>
		{{ item.name }}
    </h3>
	<p>
		{{ item.description }}
	</p>
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
</div>

## Résumé

[Résumé](/assets/documents/Resume/resume_sreekar.pdf)
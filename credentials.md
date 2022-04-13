---
layout: default
title: Credentials
---

## Projects

<div class=project>
  {% for item in site.data.projects %}
	<h2>
		{{ item.name }}
	</h2>
	<p>
		{{ item.description }}
	</p>
    <a
        href="{{ item.link }}" {% if page.url == item.link %}class="current"{% endif %}>
            <!-- comment out the image hrefs
            <img src="{{ item.image }}" alt="{{ item.alt }}"/>
        -->
            {{ item.name }}
    </a>
  {% endfor %}
</div>

## Résumé

[Résumé](/assets/documents/Resume/resume_sreekar.pdf)
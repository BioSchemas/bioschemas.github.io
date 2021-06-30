---
layout: default
title: News Tags
---
# Bioschemas News by Tag

{% comment %}
=======================
Extracts all the tags from your posts and sort tags, so that you do not need to manually collect your tags to a place.
=======================
{% endcomment %}
{% assign rawtags = "" %}
{% for post in site.posts %}
	{% assign ttags = post.tags | join:'|' | append:'|' %}
	{% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% comment %}
=======================
Remove dulpicated tags and invalid tags like blank tag.
=======================
{% endcomment %}
{% assign tags = "" %}
{% for tag in rawtags %}
	{% if tag != "" %}
		{% if tags == "" %}
			{% assign tags = tag | split:'|' %}
		{% endif %}
		{% unless tags contains tag %}
			{% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
		{% endunless %}
	{% endif %}
{% endfor %}

{% comment %}
=======================
List all the tags you have in your site.
=======================
{% endcomment %}
{% for tag in tags %}
[{{tag}}](#{{ tag | slugify }})
{% endfor %}

{% comment %}
=======================
List all posts with a certain tag.
=======================
{% endcomment %}
{% for tag in tags %}
## {{tag}}
  {% for post in site.posts %}
    {% if post.tags contains tag %}
{% include post-snippet.html %}
    {% endif %}
  {% endfor %}
{% endfor %}

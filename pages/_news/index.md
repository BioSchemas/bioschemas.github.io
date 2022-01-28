---
layout: default
title: News
---
# Bioschemas News

{%- for post in site.news %}
  {%- if post.layout == 'post' %}
  {% include post-snippet.html %}
  {%- endif %}
{%- endfor %}

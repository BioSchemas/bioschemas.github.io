---
layout: default
title: Live Deploys
---

# {{ page.title }}

Below we list the services/sites that use [Bioschemas](http://bioschemas.org) markup to describe what they are offering. We provide a direct link to the site and also a link to Google's Structured Data Testing Tool ([SDTT](https://search.google.com/structured-data/testing-tool)) visualisation of the site's markup.
The link to Google’s SDTT shows one example from the site; however, many more may exist. For example, Biosamples have marked up all of their content (currently over 10 million samples).
Please remember that Google sets minimum requirements for [schema.org](http://schema.org) markup, which may differ with those of [Bioschemas](http://bioschemas.org). As such, Google's [SDTT](https://search.google.com/structured-data/testing-tool) may provide warnings or errors when the markup is perfectly compliant with both [schema.org](http://schema.org) and [Bioschemas](http://bioschemas.org).
If your Bioschemas compliant site is not listed below, please email us at [enquiries@bioschemas.org](mailto:enquiries@bioschemas.org).

To view an ELIXIR only list of live deploys [click here](./elixir).

{% assign liveDeploys = site.data.live_deployments.resources | sort: "name" %}

##### Services/sites implementing Bioschemas's markup

__{{liveDeploys | size}}__ resources using Bioschemas.

{{liveDeploys}}

{% for resource in liveDeploys %}
  <details>
    <summary><h3>{{resource.name}}<a href="{{resource.url}}" target="_blank" style="border-bottom: none"> <i class="fas fa-external-link-alt"></i></a></h3>
    </summary>

    <ul>
      {% if resource.keywords %}
        <li><strong>Keywords:</strong>
          {% for keyword in resource.keywords %}
            {{ keyword }}
          {% unless forloop.last %}
            ,
          {% endunless %}
        {% endfor %}
        </li>
      {% endif %}
      {% if resource.description %}
        <li><strong>Description:</strong> {{ resource.description }}</li>
      {% endif %}
      {% if resource.sitemap %}
        <li><strong>Sitemap:</strong> <a href="{{ resource.sitemap }}">{{ resource.sitemap }}</a></li>
      {% endif %}
      {% if resource.nodes %}
        <li><strong>Nodes:</strong>
        {% for node in resource.nodes %}
          {{ node }}
          {% unless forloop.last %}
            ,
          {% endunless %}
        {% endfor %}
        </li>
      {% endif %}
    </ul>
  </details>
{% endfor %}

> ###### Note:
> As we do not maintain the websites listed above we can not guarantee the list is up to date, the sites are live and feature appropriate content or the links work.
>
> Help us keep it updated: [Join](/howtojoin/) the community and/or create a pull request on the [Bioschemas GitHub](https://github.com/Bioschemas/bioschemas.github.io) community project.

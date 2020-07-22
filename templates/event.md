{% autoescape false %}
<button onclick="window.location='{{ event.button_url }}'">register</button>

###### Price

{{ event.price }}

---

###### Description

{{ event.description }}

---

###### Dates

{{ event.date }}

---

###### Location

{% if event.location %}
{{ event.location }}
{% endif %}

{% if event.map_src %}
<iframe src="{{ event.map_src }}" width="100%" height="450" frameborder="0" style="border: 0" allowfullscreen></iframe>
{% endif %}

---

{% if event.lodging %}
###### Lodging

{{ event.lodging }}

---
{% endif %}

{% if event.food %}
###### Food

{{ event.food }}

---
{% endif %}

{% if event.travel %}
###### Travel

{{ event.travel }}

---
{% endif %}

{% if event.other %}
###### Other

{{ event.other }}

---
{% endif %}

###### Refunds

{{ event.refunds }}
{% endautoescape %}

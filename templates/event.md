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

{{ event.location }}

<iframe src="{{ event.map_src }}" width="100%" height="450" frameborder="0" style="border: 0" allowfullscreen></iframe>

---

###### Lodging

{{ event.lodging }}

---

###### Food

{{ event.food }}

---

###### Travel

{{ event.travel }}

---

###### Other

{{ event.other }}

---

###### Refunds

{{ event.refunds }}
{% endautoescape %}

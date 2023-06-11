---
layout: default
---

# Welcome

Thank you for visiting! This is my playground of random little things that I found that helps me learn what overlooked simple problems computers can solve. The answers could be somewhere out there, in pieces or multiple versions. My goal here is to organize my thoughts of what I found helpful. It is all a constant learning experience.

If you have any suggestions or find any issues please reach out on GitHub by following the red buttons to this project on the left of this site.

<!-- This loops through the paginated posts -->
{% for post in paginator.posts %}
  <h1><a href="{{ post.url }}">{{ post.title }}</a></h1>
  <p class="author">
    <span class="date">{{ post.date }}</span>
  </p>
  <div class="content">
    {{ post.content }}
  </div>
{% endfor %}

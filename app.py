from flask import Flask, render_template_string
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

@app.route('/')
@app.route('/<username>')
def home_page(username='World!'):
    return render_template_string('''
{% extends "bootstrap/base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
<div class="container">
  <h1>Hello and Welcome {{ username }}</h1>
</div>
{% endblock %}
''', username=username)

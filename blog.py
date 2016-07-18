from flask import Flask, render_template, redirect, url_for, abort
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from collections import OrderedDict
from datetime import datetime
import jinja2
import os
import sys

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'tables']
FLATPAGES_ROOT = 'content'
FREEZER_IGNORE_404_NOT_FOUND = True
FREEZER_DESTINATION_IGNORE = ['.git/', 'CNAME']
PYGMENTS_STYLE = 'tango'
PAGE_DIR = 'pages'
POST_DIR = 'posts'
SITE = {
    'title': 'lanmaster53.com',
    'tagline': 'A hacker looking out for people thru (<span style="color: orange;">working</span>|<span style="color: blue;">coding</span>|<span style="color: red;">teaching</span>|<span style="color: green;">sharing</span>).',
    'author': {
        'name': 'Tim Tomes',
        'email': 'timothy.tomes@gmail.com',
        'gravatar': 'http://www.gravatar.com/avatar/0a6d9b1ad59ad436bf9d9d16b2a7133e.png',
        'meta': {
            'bitbucket': {'username': 'lanmaster53', 'url': 'https://bitbucket.org/'},
            'github': {'username': 'lanmaster53', 'url': 'https://github.com/'},
            'twitter': {'username': 'lanmaster53', 'url': 'https://twitter.com/'},
            'linkedin': {'username': 'lanmaster53', 'url': 'https://www.linkedin.com/in/'},
            'youtube': {'username': 'lanmaster53', 'url': 'https://www.youtube.com/user/'},
        },
    },
    'navigation': [
        'projects',
        'training',
        'archive',
        'categories',
        'about',
        #'contact',
        #'services',
    ],
    'analytics': {
        'googleUA': {
            'tracking_id' : 'UA-52269615-1',
            'property_name' : 'lanmaster53.com',
        },
    },
}

app = Flask(__name__, static_url_path='')
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

# create the 404 page for GH Pages
@freezer.register_generator
def error_handlers():
    yield "/404.html"

# custom loader to look for template-based pages
custom_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([
        os.path.join(FLATPAGES_ROOT, PAGE_DIR),
        '/templates'
    ]),
])
app.jinja_loader = custom_loader

# add posts to the site config item
_posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
_posts.sort(key=lambda item:item['date'], reverse=True)
app.config['SITE']['posts'] = _posts

# add categories to the site config item
_categories = {}
for _post in _posts:
    for _category in _post.meta['categories']:
        if _category not in _categories:
            _categories[_category] = []
        _categories[_category].append(_post)
app.config['SITE']['categories'] = _categories

# add the site jinja global as an alias to the main config item
app.jinja_env.globals['site'] = app.config['SITE']
app.jinja_env.globals['date'] = datetime.now()

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs(PYGMENTS_STYLE), 200, {'Content-Type': 'text/css'}

@app.route('/')
def home():
    return render_template('home.html')

# support for old links to the specific project
@app.route('/burp/visual-aids/')
def burp_visual_aids():
    return redirect(url_for('page', name='burp-visual-aids'))

# post rendering view
@app.route('/<int:year>/<int:month>/<string:name>/')
def post(year, month, name):
    path = os.path.join(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

# page rendering view
@app.route('/<string:name>/')
def page(name):
    # detect and render a template
    if os.path.isfile(os.path.join(FLATPAGES_ROOT, PAGE_DIR, '{}.html'.format(name))):
        return render_template('{}.html'.format(name))
    # detect and render markdown
    path = os.path.join(PAGE_DIR, name)
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)

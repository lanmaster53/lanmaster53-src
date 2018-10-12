from flask import Flask, render_template, render_template_string, redirect, url_for, abort, has_app_context
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from datetime import datetime
import jinja2
import json
import markdown
import os
import re
import sys

##### configuration options

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
    'tagline': '',
    'author': {
        'name': 'Tim Tomes',
        'emails': {
            'personal': 'timothy.tomes@gmail.com',
            'business': 'tim.tomes@practisec.com',
        },
        'gravatar': 'https://www.gravatar.com/avatar/0a6d9b1ad59ad436bf9d9d16b2a7133e.png',
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
        'archive',
        'categories',
        'company',
        'training',
        'faq',
        'about',
    ],
    'freeze': [
        'cef',
        'drafts',
        'restmail',
        'test',
        'testimonials',
    ],
    'analytics': {
        'googleUA': {
            'tracking_id' : 'UA-52269615-1',
            'property_name' : 'lanmaster53.com',
        },
    },
    'posts': [],
    'drafts': [],
    'events': json.load(open('events.json')).get('events'),
    'testimonials': open('testimonials.html').read().decode('utf-8')
}

##### app initialization

app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)

##### app overrides

# clean up white space left behind by jinja template code
app.jinja_env.trim_blocks = True

# custom loader to look for template-based pages
custom_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([
        os.path.join(FLATPAGES_ROOT, PAGE_DIR),
        '/templates'
    ]),
])
app.jinja_loader = custom_loader

# custom renderer to render jinja prior to markdown
# this allows markdown files to include jinja processing
# only works with an app context
def my_renderer(text):
    prerendered_body = text
    if has_app_context():
        prerendered_body = render_template_string(text)
    return markdown.markdown(prerendered_body, app.config['FLATPAGES_MARKDOWN_EXTENSIONS'])
app.config['FLATPAGES_HTML_RENDERER'] = my_renderer

##### pre-request context processing

def parse_date_from_path(s):
    date_str = '-'.join(s.split(os.path.sep)[-1].split('-')[:3])
    return datetime.strptime(date_str, '%Y-%m-%d')

def parse_name_from_path(s):
    return '-'.join(s.split(os.path.sep)[-1].split('-')[3:])

# add posts to the site config item
_posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
for _post in _posts:
    _post.meta['date'] = parse_date_from_path(_post.path)
    _post.meta['name'] = parse_name_from_path(_post.path)
    # create intros for the home page
    marker = '<!-- READMORE -->'
    if marker in _post.html:
        _post.meta['intro'] = _post.html[:_post.html.find(marker)]
_posts.sort(key=lambda item:item['date'], reverse=True)
for _post in _posts:
    if _post['publish'] is True:
        app.config['SITE']['posts'].append(_post)
    else:
        app.config['SITE']['drafts'].append(_post)

# add categories to the site config item
_categories = {}
for _post in app.config['SITE']['posts']:
    for _category in _post['categories']:
        if _category not in _categories:
            _categories[_category] = []
        _categories[_category].append(_post)
app.config['SITE']['categories'] = _categories

# add the site jinja global as an alias to the main config item
app.jinja_env.globals['site'] = app.config['SITE']
app.jinja_env.globals['date'] = datetime.now()

##### frozen content generators

# create the 404 page for GH Pages
@freezer.register_generator
def error_handlers():
    print 'Freezing error handlers...'
    yield "/404.html"

# create pages not linked with url_for
@freezer.register_generator
def page():
    print 'Freezing unlinked pages...'
    for p in app.config['SITE']['freeze']:
        yield {'name': p}

# create events not linked with url_for
@freezer.register_generator
def events():
    print 'Freezing events...'
    for event in app.config['SITE']['events']:
        if event['freeze_page']:
            yield event['link_href']

# create old post urls
@freezer.register_generator
def old_post():
    print 'Freezing old post URLs...'
    for p in app.config['SITE']['posts']:
        yield {
            'year': p['date'].year,
            'month': p['date'].month,
            'name': p['name'],
        }

##### legacy support controllers

# support for old links to the specific project
@app.route('/burp/visual-aids/')
@app.route('/burp-visual-aids/')
def burp_visual_aids():
    return redirect(url_for('page', name='/projects/burp-visual-aids'))

# support for old links to posts without the day
@app.route('/<int(fixed_digits=4):year>/<int(fixed_digits=2):month>/<string:name>/')
def old_post(year, month, name):
    # regex pattern to find a filename that includes the day
    regex = '\d{4}\-\d{2}\-(\d{2})\-' + re.escape(name) + '\.md'
    for root, dirs, files in os.walk(os.path.sep.join((FLATPAGES_ROOT, POST_DIR))):
        for file in files:
            match = re.search(regex, file)
            if match:
                day = match.group(1)
                return redirect(url_for('post', year=year, month=month, day=day, name=name))
    abort(404)

##### controllers

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/static/css/pygments.css')
def pygments_css():
    return pygments_style_defs(PYGMENTS_STYLE), 200, {'Content-Type': 'text/css'}

# post rendering view
@app.route('/<int(fixed_digits=4):year>/<int(fixed_digits=2):month>/<int(fixed_digits=2):day>/<string:name>/')
def post(year, month, day, name):
    # flatpages index is the relative file path without the extension
    name = '{:04d}-{:02d}-{:02d}-{}'.format(year, month, day, name)
    path = os.path.join(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

# page rendering view
# this does not work if flask serves static files from the web root
@app.route('/<path:name>/')
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

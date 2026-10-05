from flask import Flask, render_template, url_for, abort
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from datetime import datetime
from markupsafe import Markup
import os
import sys

##### configuration options

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'tables', 'attr_list']
FLATPAGES_ROOT = 'content'
FREEZER_DESTINATION_IGNORE = ['.git/', 'CNAME']
FREEZER_REDIRECT_POLICY = 'error'
# drafts are only served by the dev server, never frozen
SHOW_DRAFTS = True
PYGMENTS_STYLE = 'tango'
PAGE_DIR = 'pages'
POST_DIR = 'posts'
READMORE = '<!-- READMORE -->'
SITE = {
    'title': 'lanmaster53.com',
    'tagline': '',
    'url': 'https://www.lanmaster53.com',
    'description': 'Articles, information, and projects related to development and web application security.',
    'author': {
        'name': 'Tim Tomes',
        'gravatar': 'https://www.gravatar.com/avatar/0a6d9b1ad59ad436bf9d9d16b2a7133e.png',
        'meta': {
            'github': {'username': 'lanmaster53', 'url': 'https://github.com/'},
            'twitter': {'username': 'lanmaster53', 'url': 'https://twitter.com/'},
            'linkedin': {'username': 'lanmaster53', 'url': 'https://www.linkedin.com/in/'},
            'youtube': {'username': 'lanmaster53', 'url': 'https://www.youtube.com/user/'},
            'vimeo': {'username': 'lanmaster53', 'url': 'https://vimeo.com/'},
        },
    },
    'navigation': [
        'projects',
        'archive',
        'categories',
        'about',
    ],
}

##### app initialization

app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.trim_blocks = True
# template-based pages live alongside markdown pages
app.jinja_loader.searchpath.append(os.path.join(FLATPAGES_ROOT, PAGE_DIR))
flatpages = FlatPages(app)
# routes are frozen explicitly via generators so drafts are never included
freezer = Freezer(app, with_no_argument_rules=False)

##### content index

def load_posts():
    posts = []
    for page in flatpages:
        if not page.path.startswith(POST_DIR + '/'):
            continue
        filename = page.path.split('/')[-1]
        page.meta['date'] = datetime.strptime(filename[:10], '%Y-%m-%d')
        page.meta['slug'] = filename[11:]
        page.meta['intro'] = page.html.split(READMORE)[0] if READMORE in page.html else None
        page.meta['summary'] = summarize(page.meta['intro'] or page.html)
        posts.append(page)
    posts.sort(key=lambda p: p['date'], reverse=True)
    published = [p for p in posts if p.meta.get('publish') is True]
    drafts = [p for p in posts if p.meta.get('publish') is not True]
    return published, drafts

def summarize(html, length=160):
    text = Markup(html).striptags()
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + '…'

def load_categories(posts):
    categories = {}
    for post in posts:
        for category in post['categories']:
            categories.setdefault(category, []).append(post)
    return categories

with app.app_context():
    POSTS, DRAFTS = load_posts()
CATEGORIES = load_categories(POSTS)

def find_post(year, month, day, slug, include_drafts=False):
    posts = POSTS + DRAFTS if include_drafts else POSTS
    for post in posts:
        d = post['date']
        if (d.year, d.month, slug) == (year, month, post['slug']) and day in (None, d.day):
            return post
    abort(404)

# markdown and template-based pages
def page_names():
    names = [p.path.split('/', 1)[1] for p in flatpages if p.path.startswith(PAGE_DIR + '/')]
    names += [f[:-5] for f in os.listdir(os.path.join(FLATPAGES_ROOT, PAGE_DIR)) if f.endswith('.html')]
    return sorted(names)

##### template helpers

def post_url(post):
    d = post['date']
    return url_for('post', year=d.year, month=d.month, day=d.day, slug=post['slug'])

def absolute_url(path):
    return SITE['url'] + path

app.jinja_env.globals.update(
    site=SITE,
    posts=POSTS,
    drafts=DRAFTS,
    categories=CATEGORIES,
    post_url=post_url,
    absolute_url=absolute_url,
    now=datetime.now,
)

##### frozen content generators

@freezer.register_generator
def post():
    for p in POSTS:
        yield {'year': p['date'].year, 'month': p['date'].month, 'day': p['date'].day, 'slug': p['slug']}

@freezer.register_generator
def legacy_post():
    for p in POSTS:
        yield {'year': p['date'].year, 'month': p['date'].month, 'day': p['date'].day, 'slug': p['slug']}

@freezer.register_generator
def legacy_post_no_day():
    for p in POSTS:
        yield {'year': p['date'].year, 'month': p['date'].month, 'slug': p['slug']}

@freezer.register_generator
def page():
    for name in page_names():
        yield {'name': name}

@freezer.register_generator
def static_routes():
    for endpoint in ('home', 'not_found_page', 'pygments_css', 'feed', 'sitemap', 'robots'):
        yield endpoint, {}

##### legacy support controllers

# static hosting can't issue real redirects, so serve a redirect stub
def redirect_stub(location):
    return render_template('redirect.html', location=location)

# old post urls without the /blog prefix
@app.route('/<int(fixed_digits=4):year>/<int(fixed_digits=2):month>/<int(fixed_digits=2):day>/<string:slug>/')
def legacy_post(year, month, day, slug):
    return redirect_stub(post_url(find_post(year, month, day, slug)))

# older post urls without the day
@app.route('/<int(fixed_digits=4):year>/<int(fixed_digits=2):month>/<string:slug>/')
def legacy_post_no_day(year, month, slug):
    return redirect_stub(post_url(find_post(year, month, None, slug)))

##### controllers

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/static/css/pygments.css')
def pygments_css():
    return pygments_style_defs(PYGMENTS_STYLE), 200, {'Content-Type': 'text/css'}

@app.route('/blog/<int(fixed_digits=4):year>/<int(fixed_digits=2):month>/<int(fixed_digits=2):day>/<string:slug>/')
def post(year, month, day, slug):
    post = find_post(year, month, day, slug, include_drafts=app.config['SHOW_DRAFTS'])
    return render_template('post.html', post=post)

@app.route('/drafts/')
def drafts():
    if not app.config['SHOW_DRAFTS']:
        abort(404)
    return render_template('drafts.html')

@app.route('/feed.xml')
def feed():
    return render_template('feed.xml', posts=POSTS[:20]), 200, {'Content-Type': 'application/xml'}

@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml', pages=page_names()), 200, {'Content-Type': 'application/xml'}

@app.route('/robots.txt')
def robots():
    return 'Sitemap: {}\n'.format(absolute_url(url_for('sitemap'))), 200, {'Content-Type': 'text/plain'}

@app.route('/404.html')
def not_found_page():
    return render_template('404.html')

# page rendering view
# this does not work if flask serves static files from the web root
@app.route('/<path:name>/')
def page(name):
    # detect and render a template
    if os.path.isfile(os.path.join(FLATPAGES_ROOT, PAGE_DIR, '{}.html'.format(name))):
        return render_template('{}.html'.format(name))
    # detect and render markdown
    page = flatpages.get_or_404(os.path.join(PAGE_DIR, name))
    return render_template('page.html', page=page)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        app.config['SHOW_DRAFTS'] = False
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)

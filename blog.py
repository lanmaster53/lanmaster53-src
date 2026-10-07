from flask import Flask, render_template, url_for, abort
from flask_flatpages import FlatPages
from pygments.formatters import HtmlFormatter
from flask_frozen import Freezer
from datetime import datetime
from markupsafe import Markup
from urllib.parse import urlparse
import os
import sys
import yaml

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
PYGMENTS_STYLE_DARK = 'github-dark'
PAGE_DIR = 'pages'
POST_DIR = 'posts'
SITE_FILE = os.path.join(FLATPAGES_ROOT, 'site.yaml')
TALKS_FILE = os.path.join(FLATPAGES_ROOT, 'talks.yaml')
PROJECTS_FILE = os.path.join(FLATPAGES_ROOT, 'projects.yaml')
READMORE = '<!-- READMORE -->'

##### app initialization

app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.trim_blocks = True
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

def load_tags(posts):
    tags = {}
    for post in posts:
        for tag in post['tags']:
            tags.setdefault(tag, []).append(post)
    return dict(sorted(tags.items()))

def load_yaml(path):
    with open(path) as fp:
        return yaml.safe_load(fp)

with app.app_context():
    POSTS, DRAFTS = load_posts()
TAGS = load_tags(POSTS)
SITE = load_yaml(SITE_FILE)
TALKS = load_yaml(TALKS_FILE)
PROJECTS = load_yaml(PROJECTS_FILE)

def find_post(year, month, day, slug, include_drafts=False):
    posts = POSTS + DRAFTS if include_drafts else POSTS
    for post in posts:
        d = post['date']
        if (d.year, d.month, slug) == (year, month, post['slug']) and day in (None, d.day):
            return post
    abort(404)

def page_names():
    return sorted(p.path.split('/', 1)[1] for p in flatpages if p.path.startswith(PAGE_DIR + '/'))

##### template helpers

def post_url(post):
    d = post['date']
    return url_for('post', year=d.year, month=d.month, day=d.day, slug=post['slug'])

def hostname(url):
    return urlparse(url).hostname

def absolute_url(path):
    return SITE['url'] + path

app.jinja_env.globals.update(
    site=SITE,
    posts=POSTS,
    drafts=DRAFTS,
    tags=TAGS,
    post_url=post_url,
    absolute_url=absolute_url,
    hostname=hostname,
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
def tag():
    for name in TAGS:
        yield {'name': name}

@freezer.register_generator
def page():
    for name in page_names():
        yield {'name': name}

@freezer.register_generator
def static_routes():
    for endpoint in ('home', 'blog', 'talks', 'projects', 'legacy_archive', 'legacy_categories', 'not_found_page', 'pygments_css', 'feed', 'sitemap', 'robots'):
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

# archive and categories were merged into the blog index
@app.route('/archive/')
def legacy_archive():
    return redirect_stub(url_for('blog'))

@app.route('/categories/')
def legacy_categories():
    return redirect_stub(url_for('blog'))

##### controllers

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/static/css/pygments.css')
def pygments_css():
    light = HtmlFormatter(style=PYGMENTS_STYLE).get_style_defs('.codehilite')
    dark = HtmlFormatter(style=PYGMENTS_STYLE_DARK).get_style_defs('.codehilite')
    css = '{}\n@media (prefers-color-scheme: dark) {{\n{}\n}}\n'.format(light, dark)
    return css, 200, {'Content-Type': 'text/css'}

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/blog/tags/<string:name>/')
def tag(name):
    if name not in TAGS:
        abort(404)
    return render_template('blog.html', tag=name)

@app.route('/blog/<int(fixed_digits=4):year>/<int(fixed_digits=2):month>/<int(fixed_digits=2):day>/<string:slug>/')
def post(year, month, day, slug):
    post = find_post(year, month, day, slug, include_drafts=app.config['SHOW_DRAFTS'])
    return render_template('post.html', post=post)

@app.route('/drafts/')
def drafts():
    if not app.config['SHOW_DRAFTS']:
        abort(404)
    return render_template('drafts.html')

@app.route('/talks/')
def talks():
    return render_template('talks.html', talks=TALKS)

@app.route('/projects/')
def projects():
    return render_template('projects.html', projects=PROJECTS)

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

# markdown page rendering view
# this does not work if flask serves static files from the web root
@app.route('/<path:name>/')
def page(name):
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

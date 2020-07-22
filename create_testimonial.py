import codecs
import json
from urllib.request import urlopen

base_url = 'https://publish.twitter.com/oembed?url={}?&hide_media=true&hide_thread=true&omit_script=true'

urls = [u for u in open('tweets.txt').read().split() if not u.startswith('#')]

left = []
right = []
i = 0
for i in range(0, len(urls)):
    url = base_url.format(urls[i])
    print(url)
    resp = urlopen(url)
    markup = json.load(resp)['html']
    markup = markup.replace('class="twitter-tweet"', 'class="twitter-tweet tw-align-center"')
    if not i%2:
        left.append(markup)
    else:
        right.append(markup)

with codecs.open('testimonials.html', 'w', encoding="utf-8") as fp:
    fp.write(u'''\
<div class="row">
<div class="six columns">
{}
</div>
<div class="six columns">
{}
</div>
</div>
'''.format(''.join(left).strip(), ''.join(right).strip()))

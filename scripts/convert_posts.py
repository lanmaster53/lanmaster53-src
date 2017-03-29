import os

os.chdir('content/posts')
posts = os.listdir('.')
for post in posts:
    new = post.split('-', 3)[-1]
    print '{} ---> {}'.format(post, new)
    os.rename(post, new)

'''
import os
import re

pat = "date: (.*)"
mydir = '.'
for arch in os.listdir(mydir):
    if arch.endswith('.md'):
        with open(arch) as f:
            txt = f.read()
        s = re.search(pat, txt)
        date = s.group(1)
        newpath = '-'.join((date, arch))
        print arch, newpath
        os.rename(arch, newpath)


os.chdir('content/posts')
posts = os.listdir('.')
for post in posts:
    with open(post) as fp:
        content = fp.readlines()
        year, month, day = content[1].split()[1].split('-')
    new = '{}-{}-{}-{}'.format(year, month, day, post)
    print '{} ---> {}'.format(post, new)
    os.rename(post, new)

posts = os.listdir('content/posts')
for post in posts:
    date = '-'.join(post.split('-')[:3])
    name = post.replace(date, '')[1:]
    with open('content/posts/'+post) as fp:
        content = fp.readlines()
        content[4] = '\n'
        del content[1]
        del content[0]
        content.insert(1, 'date: {}\n'.format(date))
    with open('content/posts/'+name, 'w') as fp:
        fp.writelines(content)
    print '{} ---> {}'.format(post, name)
'''

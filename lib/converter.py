from HTMLParser import HTMLParseError
import os
import html2text


front_matter = {
    "title": "",
    "date": "",
    "tags": "",
    "slug": "",
    "old_url": "",
    "new_url": "",
    "content_type": ""}


def list_files(directory):
    r = []
    subdirs = [x[0] for x in os.walk(directory)]
    for subdir in subdirs:
        files = os.walk(subdir).next()[2]
        if len(files) > 0:
            for f in files:
                r.append(subdir + "/" + f)
    return r


def parse_article(article):
    with open(article, 'r') as f:
        text = f.readlines()
        parsed_article = {}
        for line in text:
            for key in front_matter:
                if key + ': ' in line:
                    parsed_article[key] = line.replace(key + ': ', '').replace('\n', '')
    parsed_article["body"] = ''.join(text[8:]).decode('utf-8')

    for k in front_matter:
        if k not in parsed_article:
            parsed_article[k] = ""
    return parsed_article


def parse_tumblr(article):
    with open(article, 'r') as f:
        text = f.readlines()
        parsed_article = {'layout': 'post', 'title': text[2], 'tags': '', 'body': '\n'.join(text[5:])}
        name = article.split('/')[-1]
        name = name.split('.')[0]
        name = name.split('-')
        new_url = "%s-%s" % ('-'.join(name[0:-1]), parsed_article['title'].replace('title: ', '').replace(' ', '-').lower())
        parsed_article['new_url'] = new_url
        return parsed_article


for article in list_files('/Users/matt/src/gale/articles'):
    parsed = parse_article(article)
    with open('/Users/matt/src/gale/posts/%s.md' % parsed['new_url'].replace('/', '-')[0:-1], 'w') as post:
        try:
            body = html2text.html2text(parsed['body'])
            post.write('layout: post\n')
            post.write('%s\n' % parsed['title'])
            post.write('tags: %s\n' % parsed['tags'])
            post.write('%s' % body.encode('utf-8'))
        except HTMLParseError, e:
            print 'Failed to convert: %s' % parsed['new_url'].replace('/', '-')[0:-1]
            print e.msg

for article in list_files('/Users/matt/Dropbox/src/octopress/source/_posts/tumblr'):
    parsed = parse_tumblr(article)
    filename = parsed['new_url'].replace('/', '-')
    filename = filename.replace('?', '').replace('.', '').replace('!', '').replace('---', '-')
    filename = filename.replace('--', '').replace("'", '').replace('[', '').replace(']', '')
    filename = filename.replace('(', '').replace(')', '').replace('&amp;', '').replace('amp;', '')
    filename = filename.replace('?', '').strip('\n')
    with open('/Users/matt/src/gale/posts/%s.md' % filename, 'w') as post:
        try:
            body = html2text.html2text(parsed['body'])
            post.write('layout: post\n')
            post.write('%s' % parsed['title'])
            post.write('tags: %s\n' % parsed['tags'])
            post.write('\n')
            post.write('%s' % body.encode('utf-8'))
            print 'success'
        except HTMLParseError, e:
            print 'HTMLParseError - Failed to convert: %s' % parsed['new_url'].replace('/', '-')[0:-1]
            print e.message
        except UnicodeDecodeError, e:
            print 'UnicodeDecodeError - Failed to convert: %s' % parsed['new_url'].replace('/', '-')[0:-1]
            print e.message
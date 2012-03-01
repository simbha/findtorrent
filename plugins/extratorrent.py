#!/usr/bin/env python2

import urllib


def search(keywords):
    keywords = urllib.quote(keywords)
    page = urllib.urlopen('http://extratorrent.com/search/?search=%s' % keywords)
    lines = page.readlines()
    page.close()
    index = 0
    torrents = {}
    for linenum, line in enumerate(lines):
        if '<br /><table class="tl">' in line:
            for i in line.split('<td><a href="/torrent_download/')[1:]:
                index += 1
                item = {}
                item['index'] = index
                item['name'] = \
                    i.split('title="Download ')[1] \
                    .split(' torrent">')[0]
                item['url'] = \
                    'http://extratorrent.com/download/' \
                    + i.split('" title="')[0]
                item['size'] = \
                    i.split('</span></td><td>')[1] \
                    .split('</td>')[0] \
                    .replace('&nbsp;', ' ')
                item['seed'] = \
                    i.split('<td class="s')[1][3:] \
                    .split('</td>')[0] \
                    .replace('---', 'N/A')
                item['leech'] = \
                    i.split('<td class="l')[1][3:] \
                    .split('</td>')[0] \
                    .replace('---', 'N/A')
                item['files'] = "N/A"
                torrents[index] = item
    return torrents, index

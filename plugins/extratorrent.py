#!/usr/bin/env python2

import urllib


def search(keywords):
    keywords = urllib.quote(keywords)
    page = urllib.urlopen('http://extratorrent.com/search/?search=%s' % keywords)
    lines = page.readlines()
    page.close()
    torrents = []
    for linenum, line in enumerate(lines):
        if '<br /><table class="tl">' in line:
            for i in line.split('<td><a href="/torrent_download/')[1:]:
                item = {}
                item['name'] = \
                    i.split('title="Download ')[1] \
                    .split(' torrent">')[0]
                item['url'] = \
                    'http://extratorrent.com/download/' \
                    + i.split('" title="')[0]
                filesize = \
                    i.split('</span></td><td>')[1] \
                    .split('</td>')[0] \
                    .replace('&nbsp;', ' ')
                if 'GB' in filesize.split():
                    item['size'] = float(filesize.split()[0]) * 1024 * 1024 * 1024
                elif 'MB' in filesize.split():
                    item['size'] = float(filesize.split()[0]) * 1024 * 1024
                elif 'KB' in filesize.split():
                    item['size'] = float(filesize.split()[0]) * 1024
                else:
                    item['size'] = int(filesize.split()[0])
                item['seed'] = \
                    int(i.split('<td class="s')[1][3:] \
                    .split('</td>')[0] \
                    .replace('---', '-1'))
                item['leech'] = \
                    int(i.split('<td class="l')[1][3:] \
                    .split('</td>')[0] \
                    .replace('---', '-1'))
                item['files'] = -1
                torrents.append(item)
    return torrents

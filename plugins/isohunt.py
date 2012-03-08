#!/usr/bin/env python2

import urllib


def search(keywords):
    keywords = urllib.quote_plus(keywords)
    page = urllib.urlopen("http://isohunt.com/torrents/?ihq=%s" % keywords)
    lines = page.readlines()
    page.close()
    torrents = []
    for linenum, line in enumerate(lines):
        if '<table id=serps' in line:
            for i in line.split("<a id=link")[1:]:
                item = {}
                item["name"] = \
                    i.split("summary'>")[1]\
                    .split("</a>")[0]\
                    .replace('<span title="', "")\
                    .split('">')[0]\
                    .replace('<b>', "")\
                    .replace('</b>', "")\
                    .split('<br>')[-1]
                item["url"] = \
                    "http://ca.isohunt.com/download/"\
                    + i.split("/")[2]\
                    + "/" + urllib.quote_plus(item["name"]) + ".torrent"
                filesize = \
                    i.split("'>")[2]\
                    .split("<")[0]
                if 'GB' in filesize.split():
                    item['size'] = float(filesize.split()[0]) * 1024 * 1024 * 1024
                elif 'MB' in filesize.split():
                    item['size'] = float(filesize.split()[0]) * 1024 * 1024
                elif 'KB' in filesize.split():
                    item['size'] = float(filesize.split()[0]) * 1024
                else:
                    item['size'] = int(filesize.split()[0])
                item["seed"] = \
                    int(i.split('<td class="row3">')[1]\
                    .split("</td>")[0])
                item["leech"] = \
                    int(i.split('<td class="row3">')[2]\
                    .split("</td>")[0])
                item["files"] = \
                    int(i.split('<td class="row3" title=\'')[1]\
                    .split()[0])
                torrents.append(item)
    return torrents

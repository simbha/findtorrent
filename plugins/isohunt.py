#!/usr/bin/env python2

import urllib


def search(keywords):
    keywords = urllib.quote_plus(keywords)
    page = urllib.urlopen("http://isohunt.com/torrents/?ihq=%s" % keywords)
    lines = page.readlines()
    page.close()
    index = 0
    torrents = {}
    for linenum, line in enumerate(lines):
        if '<table id=serps' in line:
            for i in line.split("<a id=link")[1:]:
                index += 1
                item = {}
                item["index"] = index
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
                item["size"] = \
                    i.split("'>")[2]\
                    .split("<")[0]
                item["seed"] = \
                    i.split('<td class="row3">')[1]\
                    .split("</td>")[0]
                item["leech"] = \
                    i.split('<td class="row3">')[2]\
                    .split("</td>")[0]
                item["files"] = \
                    i.split('<td class="row3" title=\'')[1]\
                    .split()[0]
                torrents[index] = item
    return torrents, index

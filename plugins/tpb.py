#!/usr/bin/env python2

import urllib


def search(query):
    query = urllib.quote(query)
    page = urllib.urlopen("http://thepiratebay.se/search/%s/0/99/0" % query)
    lines = page.readlines()
    page.close()
    index = 0
    torrents = {}
    for linenum, line in enumerate(lines):
        if '<div class="detName">' in line:
            index += 1
            item = {}
            item["index"] = index
            end = linenum + 4
            while (linenum < end):
                line = lines[linenum].strip()
                if 'class="detLink" title="' in line:
                    item["name"] = \
                        line.split('">')[2]\
                        .split("</a></div>")[0]
                elif '<a href="http://' in line:
                    item["url"] = \
                        line.split('<a href="')[2]\
                        .split('" title="')[0]
                elif 'class="detDesc"' in line:
                    item["size"] = \
                        line.split(" ")[4]\
                        .replace("&nbsp;", " ")\
                        .replace("i", "")\
                        .replace(",", "")
                elif '</td>' in line:
                    item["seed"] = \
                        lines[linenum + 1].strip()\
                        .split(">")[1]\
                        .split("<")[0]
                    item["leech"] = \
                        lines[linenum + 2].strip()\
                        .split(">")[1]\
                        .split("<")[0]
                item["files"] = "N/A"
                linenum += 1
            torrents[index] = item
    return torrents, index

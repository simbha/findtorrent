#!/usr/bin/env python2

import urllib
import re


def search(query):
    query = urllib.quote(query)
    page = urllib.urlopen("http://kat.ph/usearch/%s" % query)
    lines = page.readlines()
    page.close()
    index = 0
    torrents = {}
    for linenum, line in enumerate(lines):
        if 'id="torrent_' in line:
            index += 1
            item = {}
            item["index"] = index
            end = linenum + 12
            while (linenum < end):
                line = lines[linenum].strip()
                if "?name=" in line:
                    item["name"] = \
                        urllib.unquote_plus(\
                        line.split("?name=")[-1]\
                        .split("'+'")[-2])
                elif "Download torrent file" in line:
                    item["url"] = \
                        line.split('Download torrent file" href="')[-1]\
                        .split('" onclick="')[-2]\
                        .replace(".torrent?title=", "/")\
                        + ".torrent"
                elif "nobr center" in line:
                    item["size"] = \
                        line.split('"nobr center">')[-1]\
                        .split("</span>")[-2]\
                        .replace("<span>", "")
                elif re.compile('<td class="center">[0-9]*</td>').search(line):
                    item["files"] = \
                        line.split('<td class="center">')[-1]\
                        .split("</td>")[-2]
                elif "&nbsp;" in line:
                    item["age"] = \
                        line.split('<td class="center">')[-1]\
                        .split("</td>")[-2]\
                        .replace("&nbsp;", " ")
                elif "green center" in line:
                    item["seed"] = \
                        line.split('<td class="green center">')[-1]\
                        .split("</td>")[-2]
                elif "red lasttd center" in line:
                    item["leech"] = \
                        line.split('<td class="red lasttd center">')[-1]\
                        .split("</td>")[-2]
                linenum += 1
            torrents[index] = item
    return torrents, index

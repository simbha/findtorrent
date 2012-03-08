# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import urllib
import re


def search(keywords):
    keywords = urllib.quote(keywords)
    page = urllib.urlopen("http://kat.ph/usearch/%s" % keywords)
    lines = page.readlines()
    page.close()
    torrents = []
    for linenum, line in enumerate(lines):
        if 'id="torrent_' in line:
            item = {}
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
                    filesize = \
                        line.split('"nobr center">')[-1]\
                        .split("</span>")[-2]\
                        .replace("<span>", "")
                    if 'GB' in filesize.split():
                         item['size'] = float(filesize.split()[0]) * 1024 * 1024 * 1024
                    elif 'MB' in filesize.split():
                        item['size'] = float(filesize.split()[0]) * 1024 * 1024
                    elif 'KB' in filesize.split():
                        item['size'] = float(filesize.split()[0]) * 1024
                    else:
                        item['size'] = int(filesize.split()[0])
                elif re.compile('<td class="center">[0-9]*</td>').search(line):
                    item["files"] = \
                        line.split('<td class="center">')[-1]\
                        .split("</td>")[-2]
                elif "green center" in line:
                    item["seed"] = \
                        int(line.split('<td class="green center">')[-1]\
                        .split("</td>")[-2])
                elif "red lasttd center" in line:
                    item["leech"] = \
                        int(line.split('<td class="red lasttd center">')[-1]\
                        .split("</td>")[-2])
                linenum += 1
            torrents.append(item)
    return torrents

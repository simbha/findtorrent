# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

def search(keywords):
    import urllib

    keywords = urllib.quote_plus(keywords)
    page = urllib.urlopen("http://isohunt.com/torrents/?ihq=%s" % keywords)
    lines = page.readlines()
    page.close()
    results = []
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
                    i.split('<td class="row3">')[1]\
                    .split("</td>")[0]
                if (item['seed'] == ''):
                    item['seed'] = -1
                else:
                    item['seed'] = int(item['seed'])
                item["leech"] = \
                    i.split('<td class="row3">')[2]\
                    .split("</td>")[0]
                if (item['leech'] == ''):
                    item['leech'] = -1
                else:
                    item['seed'] = int(item['seed'])
                item["files"] = \
                    int(i.split('<td class="row3" title=\'')[1]\
                    .split()[0])
                results.append(item)
    return results

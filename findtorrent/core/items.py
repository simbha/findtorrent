# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from findtorrent.core.helper import *


class Items:
    def search(self, plugin, keywords):
        exec 'from findtorrent.plugins import %s' % plugin

        exec 'Items.results = %s.search(\'%s\')' % (plugin, keywords)

    def sort(self, sort, reverse):
        from operator import itemgetter

        Items.sorted = sorted(Items.results, key=itemgetter(sort), reverse=reverse)

    def print_items(self, max_items):
        import os
        import string
        from findtorrent.core.colors import colors
        from hurry.filesize import size, si

        cols = int(os.popen('stty size', 'r').read().split()[1])
        print colors.HEADER + \
              'No.  Name' + (cols - 33) * ' ' + 'Size  Files  Seed  Leech'
        print cols * '-'
        for index, item in enumerate(Items.sorted):
            if (max_items != -1 and index + 1 > max_items):
                break
            print colors.INDEX + string.ljust(str(index + 1) + '.', 5) + \
                  colors.NAME + string.ljust(item['name'][:cols - 31],
                                             cols - 31) + \
                  colors.SIZE + string.rjust(size(item['size'],
                                                  system=si), 6) + \
                  colors.FILES + string.rjust(str(item['files']) \
                                 .replace('-1', 'N/A'), 7) + \
                  colors.SEED + string.rjust(str(item['seed']) \
                                .replace('-1', 'N/A'), 6) + \
                  colors.LEECH + string.rjust(str(item['leech']) \
                                 .replace('-1', 'N/A'), 7) + \
                  colors.ENDC

    def get_url_list(self):
        Items.urls = []
        url_nums = get_user_input('Enter torrent number:').split(',')
        for url_num in url_nums:
            Items.urls.append(Items.sorted[int(url_num) - 1]['url'])

    def download_urls(self):
        conf = load_settings()
        from findtorrent.core.download import download
        for url in Items.urls:
            download(url, conf["download_dir"] + "/" + url.split('/')[-1])

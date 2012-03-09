# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from findtorrent.core.helper import *


def main():
    from findtorrent.core.items import Items

    conf = load_settings()
    args = parse_args()

    i = Items()
    i.search(args['plugin'], args['keywords'])
    i.sort(args['sort'], args['reverse'])
    i.print_items(args['max_items'])
    i.get_url_list()
    i.download_urls()

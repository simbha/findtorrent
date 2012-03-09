# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from findtorrent import *


def str2bool(v):
    return v.lower() in ("yes", "true")


def get_user_input(message):
    import sys

    try:
        user_input = raw_input(message + ' ')
    except KeyboardInterrupt:
        print ''
        sys.exit()

    return user_input


def load_settings():
    import os
    from configobj import ConfigObj

    global conf

    try:
        conf = ConfigObj(CONFIG_FILE, file_error=True)
    except IOError:
        if not os.path.exists(CONFIG_FILE.replace("/findtorrent.conf", "")):
            os.makedirs(CONFIG_FILE.replace("/findtorrent.conf", ""))
        conf = ConfigObj()
        conf.filename = CONFIG_FILE
        conf["download_dir"] = DOWNLOAD_DIR
        conf["default_plugin"] = DEFAULT_PLUGIN
        conf.write()

    return conf


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description='Find and download torrent \
                                                  files from various torrent \
                                                  sites')
    parser.add_argument('--plugin',
                        metavar='plugin',
                        default=conf['default_plugin'],
                        help='plugin')
    parser.add_argument('--max-items',
                        metavar='max_items',
                        default=-1,
                        help='maximum number of results')
    parser.add_argument('--sort',
                        metavar='sort',
                        default='seed',
                        help='sort results')
    parser.add_argument('--reverse',
                        metavar='reverse',
                        default='True',
                        help='reverse results order')
    parser.add_argument('keywords',
                        metavar='keywords',
                        nargs='?',
                        default='',
                        type=str,
                        help='search')
    args = vars(parser.parse_args())

    args['max_items'] = int(args['max_items'])
    args['reverse'] = str2bool(args['reverse'])

    if (args['keywords'] == ''):
        args['keywords'] = get_user_input('Enter search terms:')

    return args

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import os

CONFIG_FILE = os.environ['XDG_CONFIG_HOME'] + '/findtorrent/findtorrent.conf'
DOWNLOAD_DIR = os.environ['HOME']
DEFAULT_PLUGIN = 'isohunt'

from findtorrent.core.main import main

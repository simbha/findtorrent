# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

class colors:
    INDEX = '\033[90m'
    NAME = '\033[94m'
    SIZE = '\033[92m'
    FILES = '\033[93m'
    SEED = '\033[91m'
    LEECH = '\033[95m'
    HEADER = '\033[90m'
    ENDC = '\033[0m'

    def disable(self):
        self.INDEX = ''
        self.NAME = ''
        self.SIZE = ''
        self.FILES = ''
        self.SEED = ''
        self.LEECH = ''
        self.HEADER = ''
        self.ENDC = ''

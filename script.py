#!/usr/bin/python

import sys
from Instagram import Instagram

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]

    instagram = Instagram(username, password)

    instagram.get_non_followers()
else:
    print "USAGE:\n./script.py username password"
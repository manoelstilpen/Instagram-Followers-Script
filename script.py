#!/usr/bin/python

import argparse
from Instagram import Instagram

parser = argparse.ArgumentParser(description="Return people who dont follow you back on instagram")
parser.add_argument("username", help="Your Instagram user")
parser.add_argument("password", help="Your Instagram password")
args = parser.parse_args()

instagram = Instagram(args.username, args.password)
instagram.get_non_followers()

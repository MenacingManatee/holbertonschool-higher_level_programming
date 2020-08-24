#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status using urllib'''


import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as u:
    print(u.getheader('X-Request-Id'))
    u.close()

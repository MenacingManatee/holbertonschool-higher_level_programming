#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as a parameter'''


import urllib.request, urllib.parse
from sys import argv


data = urllib.parse.urlencode({"email": argv[2]}).encode()
with urllib.request.urlopen(argv[1], data=data) as u:
    print(u.read().decode('utf-8'))
    u.close()

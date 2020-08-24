#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status using urllib'''


import urllib.request


with urllib.request.urlopen("https://intranet.hbtn.io/status") as u:
    print(u.getheader('X-Request-Id'))
    u.close()

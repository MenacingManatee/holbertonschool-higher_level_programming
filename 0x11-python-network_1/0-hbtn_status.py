#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status using urllib'''


import urllib.request


with urllib.request.urlopen("https://intranet.hbtn.io/status") as u:
    tmp = u.read()
    print("Body response:")
    print("\t- type: {}".format(type(tmp)))
    print("\t- content: {}".format(tmp))
    print("\t- utf8 content: {}".format(tmp.decode('utf-8')))
    u.close()

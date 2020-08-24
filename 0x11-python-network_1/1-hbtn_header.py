#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status using urllib'''

if __name__ == "__main__":
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as u:
        print(u.getheader('X-Request-Id'))
        u.close()

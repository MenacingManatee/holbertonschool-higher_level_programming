#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status using requests module'''


if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.head(argv[1])
    print(req.headers.get('X-Request-Id'))

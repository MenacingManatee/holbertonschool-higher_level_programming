#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status using requests module'''


if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.post(argv[1], data={"email": argv[2]})
    print(req.text)

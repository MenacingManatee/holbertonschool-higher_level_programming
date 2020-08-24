#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as a parameter'''


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    data = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], data=data) as u:
        print(u.read().decode('utf-8'))
        u.close()

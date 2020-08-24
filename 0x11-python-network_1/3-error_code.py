#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the body \
of the response'''


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as u:
            print(u.read().decode('utf-8'))
            u.close()
    except error.HTTPError as e:
        print("Error Code: {}".format(e.code))

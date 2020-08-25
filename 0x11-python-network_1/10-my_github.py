#!/usr/bin/python3
'''takes your Github credentials (username and password)
and uses the Github API to display your id'''


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(argv[1], argv[2]))
    print(req.json().get('id'))

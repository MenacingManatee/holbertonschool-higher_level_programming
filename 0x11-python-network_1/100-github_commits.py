#!/usr/bin/python3
'''takes your Github credentials (username and password)
and uses the Github API to display your id'''


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "".join(['https://api.github.com/repos/', argv[2], '/',
                   argv[1], '/commits'])
    req = requests.get(url)
    for item in req.json():
        print(item.get('sha'), item.get('commit').get('author').
              get('name'))

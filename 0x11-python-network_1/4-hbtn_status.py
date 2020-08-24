#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status using requests module'''


if __name__ == "__main__":
    import requests

    body = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t-type: {}\n\t- content: {}".format(
        type(body.text), body.text))

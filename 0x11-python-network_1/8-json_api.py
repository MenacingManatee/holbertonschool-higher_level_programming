#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.'''


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2:
        js = ""
    else:
        js = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data={"q": js})
    try:
        js2 = req.json()
    except Exception:
        print("Not a valid JSON")
        exit
    if js2 == {} or js2 is None:
        print("No result")
    else:
        print("[{}] {}".format(js2.get('id'), js2.get('name')))

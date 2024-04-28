#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        info = r.json()
        if len(info) == 0 or "id" not in info or "name" not in info:
            print("No result")
        else:
            print("[{}] {}".format(info.get("id"), info.get("name")))
    except Exception:
        print("Not a valid JSON")

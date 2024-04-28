#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    basic = requests.auth.HTTPBasicAuth(user, pw)

    r = requests.get(
            "https://api.github.com/users/{}".format(user), auth=basic)
    info = r.json()
    print(info.get('id'))

#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    basic = requests.auth.HTTPBasicAuth(user, pw)

    r = requests.get(
            "https://api.github.com/user", auth=basic)
    print(r.json().info.get('id'))

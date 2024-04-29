#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

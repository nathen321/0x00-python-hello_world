#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(dict(response.headers).get("X-Request-Id"))     

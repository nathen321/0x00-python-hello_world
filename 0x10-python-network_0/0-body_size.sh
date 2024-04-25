#!/usr/bin/python3
curl -I $1 | grep "Content-Length" | cut -d " " -f2

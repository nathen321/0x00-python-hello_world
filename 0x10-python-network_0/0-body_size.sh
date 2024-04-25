#!/usr/bin/python3
curl -sI $1 | grep "Content-Length" | cut -d " " -f2

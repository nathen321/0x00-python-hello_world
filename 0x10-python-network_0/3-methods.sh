#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -i ALLOW $1 -L | grep "Allow" | cut -d " " -f2-

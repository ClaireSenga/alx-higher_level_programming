#!/usr/bin/env python3
# Sends a request to a URL & displays response body using urllib & sys

import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    # Send a GET request to the URL
    with urllib.request.urlopen(url) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')
        print(response_body)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")

#!/usr/bin/env python3
# Sends a POST request with email as parameter & displays response body using urllib & sys

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send a POST request to the URL with the data
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')
        print(response_body)
except urllib.error.URLError as e:
    print(f"Error fetching {url}: {e}")

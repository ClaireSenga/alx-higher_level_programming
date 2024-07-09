#!/usr/bin/env python3
# Sends a request to a URL & displays the value of X-Request-Id using requests & sys

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if X-Request-Id header exists in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(f"X-Request-Id: {x_request_id}")
    else:
        print("X-Request-Id header not found in the response.")
        
except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")

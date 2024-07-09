#!/usr/bin/env python3
# Sends a request to a URL & displays response body using requests & sys

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Display the body of the response
    print(response.text)
    
    # Check for HTTP error status codes
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")

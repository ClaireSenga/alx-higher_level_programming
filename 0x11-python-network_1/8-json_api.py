#!/usr/bin/env python3
# Sends a POST request with letter as parameter & processes response using requests & sys

import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}

try:
    response = requests.post(url, data=data)
    
    # Check if response content is JSON and not empty
    if response.headers.get('content-type') == 'application/json':
        json_response = response.json()
        
        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")

except requests.RequestException as e:
    print(f"Error making POST request to {url}: {e}")

#!/usr/bin/env python3
# Sends a POST request with email as parameter & displays response body using requests & sys

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = {'email': email}

try:
    # Send a POST request to the URL with data
    response = requests.post(url, data=data)
    
    # Display the body of the response
    print(response.text)
    
except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")

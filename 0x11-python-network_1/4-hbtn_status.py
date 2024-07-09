#!/usr/bin/env python3
# Fetches https://alx-intranet.hbtn.io/status using requests.

import requests

url = 'https://alx-intranet.hbtn.io/status'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
    # Display the body of the response in the required format
    print("- Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Error fetching {url}: {e}")

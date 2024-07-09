#!/usr/bin/env python3
# Fetches GitHub user id using GitHub API with Basic Authentication using requests & sys

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = f'https://api.github.com/user'

try:
    # Send GET request to GitHub API with Basic Authentication using token
    response = requests.get(url, auth=(username, token))
    
    # Check if request was successful
    if response.status_code == 200:
        user_info = response.json()
        print(f"User ID: {user_info['id']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")


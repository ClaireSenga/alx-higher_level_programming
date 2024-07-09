#!/usr/bin/env python3
# Fetches 10 most recent commits from a GitHub repository using GitHub API with requests & sys

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]
base_url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'
params = {'per_page': 10}  # Limit to 10 most recent commits messages

try:
    # Send GET request to GitHub API.
    response = requests.get(base_url, params=params, auth=('YOUR_USERNAME', 'YOUR_TOKEN'))
    
    # Check if request was a success.
    if response.status_code == 200:
        commits = response.json()
        
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.RequestException as e:
    print(f"Error fetching {base_url}: {e}")

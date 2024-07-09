#!/usr/bin/env python3
# Fetches https://alx-intranet.hbtn.io/status using urllib.

import urllib.request
import urllib.error

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')
        print("- Body response:")
        print("\t- type:", type(html_content))
        print("\t- content:", html_content)
except urllib.error.URLError as e:
    print(f"Error fetching {url}: {e}")

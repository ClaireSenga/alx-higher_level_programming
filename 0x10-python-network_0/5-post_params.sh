#!/bin/bash
# A script that takes in a URL, sends a POST request to The passed URL, & displays the body of the response.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

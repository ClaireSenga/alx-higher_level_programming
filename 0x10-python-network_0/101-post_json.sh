#!/bin/bash
# Sends a JSON POST request to given URL with a given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

#!/bin/bash
# Sends a request to URL & displays the size of the body of the response
curl -s "$1" | wc -c

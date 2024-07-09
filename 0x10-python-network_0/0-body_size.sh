#!/bin/bash
# Sends a request to URL & displays the size
# Of the body of the response
curl -s "$1" | wc -c

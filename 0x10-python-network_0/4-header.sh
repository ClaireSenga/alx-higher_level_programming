#!/bin/bash
# A script that takes in a URL as an arg, sends a GET request to the URL, & displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"

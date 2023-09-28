#!/bin/bash
# use curl to send a request and displays the size of the response
curl -s -X POST -H "Content-Type: application/json" -d "%(cat "$2")" "$1"

#!/bin/bash
# use curl to send a request and displays the size of the response
curl -s "$1" | wc -c

#!/bin/bash
# use curl to send a request and display all allowed methods
curl -s -I "$1" | grep -i "Allow:" | cut -d " " -f 2-

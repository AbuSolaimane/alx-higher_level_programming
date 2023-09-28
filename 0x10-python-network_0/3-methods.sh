#!/bin/bash
# use curl to send a request and display all allowed methods
curl -sI "$1" | grep -i "Allow:" | awk '{print $2}'

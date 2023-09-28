#!/bin/bash
# use curl to send a request and displays only status
curl -s -w "%{http_code}" "$1"

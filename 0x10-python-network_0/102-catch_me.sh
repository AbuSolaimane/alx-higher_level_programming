#!/bin/bash
# use curl to send a request
curl -o /dev/null -w "You got me!" -s 0.0.0.0:5000/catch_me

#!/bin/bash
# use curl to send a request
curl -so /dev/null -w "You got me!" 0.0.0.0:5000/catch_me

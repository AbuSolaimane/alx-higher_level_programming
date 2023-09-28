#!/bin/bash
# use curl to send a request
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=44" 0.0.0.0:5000/catch_me

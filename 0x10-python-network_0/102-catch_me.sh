#!/bin/bash
# Script to SEND a request to 0.0.0.0:5000/catch_me with the message "You got me!".
curl -sL -X PUT -H "Origin: HB" -d "user_id=98" 0.0.0.0:5000/catch_me

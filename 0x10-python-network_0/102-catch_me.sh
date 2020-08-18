#!/usr/bin/env bash
# causes the server to respond with a message containing You got me!
curl -sX PUT -L --data "user_id=98" =H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me

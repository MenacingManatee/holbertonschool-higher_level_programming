#!/usr/bin/env bash
# sends a POST request an displays response
curl --data "email=hr@holbertonschool.com&subject=I will always be here \
for PLD" "$1"

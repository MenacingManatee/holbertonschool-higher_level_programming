#!/usr/bin/env bash
# sends a JSON POST request to a URL and displays the body of the response.
curl -sX POST "$1" -d @"$2" --header "Content-Type: application/json"

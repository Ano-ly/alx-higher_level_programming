#!/bin/bash
#Connect to a url and print size in bytes of response using curl
curl -s -o /dev/null -w '%{size_download}\n' "$1"

#!/bin/bash
#Connect to a url and print size in bytes of response using curl
curl -sw "%{size_download}\n" "$1" | tail -n 1

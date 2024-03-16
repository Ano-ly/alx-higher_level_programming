#!/bin/bash
#Print allowed http request methods for a u
curl -sI "$1" | grep 'Allow' | awk -v FS=": " '{print $2}'

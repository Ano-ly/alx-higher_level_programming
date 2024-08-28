#!/bin/bash
# Send get request and display body if status code is 200
curl -s "$1" -o /dev/null -w "%{http_code}" | grep -q 200 && curl -s "$1"

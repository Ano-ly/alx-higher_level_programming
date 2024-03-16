#!/bin/bash
# Send get request and display body if status code is 200

response=$(curl -sw '\n%{http_code}\n' "$1")

statuscode=$(echo "${response}" | tail -n 1)

response_length=$(echo "${response}" | wc -l)
responselen=$((response_length))
lenn=$((responselen - 1))
response=$(echo "${response}" | head -n "${lenn}")

if [ "${statuscode}" == "200" ]; then
	echo "${response}"
fi

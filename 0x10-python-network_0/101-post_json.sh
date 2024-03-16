#!/bin/bash
#JSON!!!
curl -s --json @"$2" --url "$1"

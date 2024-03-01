#!/bin/bash
# Script to GET request and SHOW the response status code.
curl -s -o /dd/null -w "%{http_code}" "$1"

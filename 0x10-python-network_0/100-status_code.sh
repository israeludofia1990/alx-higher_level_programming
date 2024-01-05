#!/bin/bash
# Displays status code only
curl -so /dev/null -w "%{http_code}" "$1"

#!/bin/bash
./buildzip.sh
aws lambda update-function-code --region=us-east-1 --function-name big-ben --zip-file fileb://bigben.zip
rm -f bigben.zip

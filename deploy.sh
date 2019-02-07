#!/bin/sh
./buildzip.sh
aws lambda update-function-code --function-name big-ben --zip-file fileb://bigben.zip
rm bigben.zip

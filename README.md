# Big Ben Lambda Function
Powers https://mastodon.org.uk/@bigben

Runs as an AWS Lambda for great serverless justice

## You will need

* One Python 3.9 installation
* One Bash shell
* One virtualenv utility
* One zip utility
* One Mastodon access token
* One AWS account with ready-made IAM Role for Lambda Execution with the AWSLambdaBasicExecutionRole policy attached
* One installed and configured AWS CLI tool with the relevant permissions to create a Lambda

## Environment Varibles

* MASTODON_BASE_URL - The hostname of the mastodon instance e.g. https://mastodon.org.uk
* MASTODON_ACCESS_TOKEN - A valid mastodon access token

## Initial Command To Deploy Lambda
```
./buildzip.sh
aws lambda create-function --function-name big-ben --runtime python3.9 --handler main.handler --timeout 15 --zip-file fileb://bigben.zip --role <my-iam-role-arn>
```

## Updating the code
`./deploy.sh`

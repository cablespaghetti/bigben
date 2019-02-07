# Big Ben Lambda Function
Powers https://mastodon.org.uk/@bigben

Runs as an AWS Lambda for great serverless justice

## Environment Varibles

* MASTODON_BASE_URL - The hostname of the mastodon instance e.g. https://mastodon.org.uk
* MASTODON_ACCESS_TOKEN - A valid mastodon access token

## Initial Command To Deploy Lambda
```
./buildzip.sh
aws lambda create-function --function-name big-ben --runtime python3.6 --handler main.handler --timeout 15 --zip-file fileb://bigben.zip --role <my-iam-role-arn>
```

## Updating the code
`./deploy.sh`

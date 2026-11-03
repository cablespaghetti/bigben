# Big Ben Lambda Function

Powers https://mastodon.org.uk/@bigben

Runs as an AWS Lambda for great serverless justice. On each invocation it posts
a photo of the Great Clock of Westminster and a "BONG" for the current hour in
London to Mastodon, with a special post for New Year.

## Requirements

* [mise](https://mise.jdx.dev/) - installs Python 3.14, Pipenv, the AWS CLI and
  the AWS SAM CLI
* One Mastodon access token
* An AWS account you can deploy to (CI assumes the
  `github-actions-bigben` IAM role via GitHub OIDC)

## Setup

```sh
mise install        # install the pinned tools
mise run check      # sync dependencies, run Black and the tests
```

## Environment Variables

* `MASTODON_BASE_URL` - The hostname of the mastodon instance e.g. `https://mastodon.org.uk`
* `MASTODON_ACCESS_TOKEN` - A valid mastodon access token

## Tasks

| Task | Description |
| --- | --- |
| `mise run install` | Install dependencies from `Pipfile.lock` |
| `mise run lint` | Check formatting with Black |
| `mise run test` | Run the unit tests |
| `mise run check` | Run lint and tests |
| `mise run requirements` | Export production requirements for SAM |
| `mise run build` | Build the Lambda package with SAM |
| `mise run deploy` | Build and deploy the stack with SAM |

## Deployment

Deployment is handled by GitHub Actions in
`.github/workflows/deploy.yml`:

* Pull requests run `mise run check`.
* Pushes to `main` run the checks and then `mise run deploy`.

The workflow authenticates to AWS with GitHub OIDC (no long-lived keys) using
the `arn:aws:iam::033667237508:role/github-actions-bigben` role. The
`MASTODON_ACCESS_TOKEN` and `MASTODON_BASE_URL` secrets live in the `production`
GitHub environment.

The SAM stack is named `big-ben` and deploys to `us-east-1`, writing build
artifacts to the `bigben-sam-artifacts-033667237508` S3 bucket (created on the
first deploy if missing).

### First deploy

The function is managed by CloudFormation with the fixed name `big-ben`. If you
still have a manually-created `big-ben` Lambda, delete it before the first
stack deploy so CloudFormation can create the replacement:

```sh
aws lambda delete-function --function-name big-ben --region us-east-1
```

Then push to `main`, or deploy locally with AWS credentials and the Mastodon
environment variables set:

```sh
export MASTODON_BASE_URL=https://mastodon.org.uk
export MASTODON_ACCESS_TOKEN=...
mise run deploy
```

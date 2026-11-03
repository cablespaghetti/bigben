# Big Ben Lambda Function

Powers https://mastodon.org.uk/@bigben

Runs as an AWS Lambda for great serverless justice.

## Requirements

* [mise](https://mise.jdx.dev/) - installs Python 3.14, uv, the AWS CLI and the AWS SAM CLI
* One Mastodon access token
* An AWS account you can deploy to (CI assumes the `github-actions-bigben` IAM role via GitHub OIDC)

## Setup

```sh
mise install        # install the required tools
mise run check      # sync dependencies, run Black and the tests
```

## Environment Variables

* `MASTODON_BASE_URL` - The hostname of the mastodon instance e.g. `https://mastodon.org.uk`
* `MASTODON_ACCESS_TOKEN` - A valid mastodon access token

## Tasks

| Task | Description |
| --- | --- |
| `mise run install` | Install dependencies from `uv.lock` |
| `mise run lint` | Check formatting with Black |
| `mise run test` | Run the unit tests |
| `mise run check` | Run lint and tests |
| `mise run requirements` | Export production requirements for SAM |
| `mise run build` | Build the Lambda package with SAM |
| `mise run deploy` | Build and deploy the stack with SAM |

## Deployment

Deployment is handled by GitHub Actions in `.github/workflows/deploy.yml`:

* Pull requests run `mise run check`.
* Pushes to `main` run the checks and then `mise run deploy`.

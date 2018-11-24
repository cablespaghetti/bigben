# Big Ben Script
Powers https://mastodon.org.uk/@bigben

Uses v0.19.0 of https://github.com/ihabunek/toot

Not much more to say really. It runs as a cron job, on the hour every hour. Everything is hardcoded. I will at some point make it less shonky but right now it'll do!

## Environment Varibles

The following are used to build `.config/toot/config.json`. The easiest way to get them is to install toot, login to your account and then view that file:
* MASTODON_INSTANCE - The hostname of the mastodon instance
* MASTODON_USERNAME - The username for your user (not including @instance.hostname)
* MASTODON_ACCESS_TOKEN
* MASTODON_CLIENT_ID
* MASTODON_CLIENT_SECRET

## Kubernetes CronJob YAML
```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: bigben
spec:
  schedule: "0 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: bigben
            image: cablespaghetti/bigben
            env:
              MASTODON_INSTANCE: mastodon.org.uk
              MASTODON_USERNAME: bigben
              MASTODON_ACCESS_TOKEN: <my token>
              MASTODON_CLIENT_ID: <my client id>
              MASTODON_CLIENT_SECRET: <my client secret>
          restartPolicy: OnFailure
```

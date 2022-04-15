from mastodon import Mastodon
import datetime
import os
import pytz


def handler(event, context):
    access_token = os.environ.get("MASTODON_ACCESS_TOKEN", "")
    api_base_url = os.environ.get("MASTODON_BASE_URL", "")

    if not access_token or not api_base_url:
        print(
            "You must set both a MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL environment variable"
        )
        exit(1)

    mastodon = Mastodon(access_token=access_token, api_base_url=api_base_url)
    now = datetime.datetime.now(pytz.timezone("Europe/London"))
    hour = now.hour % 12

    if now.month == 1 and now.day == 1 and now.hour == 0:
        filename = "newyear.jpg"
    else:
        filename = f"{hour}.jpg"

    print(filename)

    photo = mastodon.media_post("images/" + filename, "image/jpeg")
    mastodon.status_post(("BONG " * hour).rstrip(), media_ids=photo)


if __name__ == "__main__":
    handler(None, None)

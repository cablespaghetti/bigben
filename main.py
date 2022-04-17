from mastodon import Mastodon
import datetime
import os
import pytz


def get_mastodon():
    access_token = os.environ.get("MASTODON_ACCESS_TOKEN", "")
    api_base_url = os.environ.get("MASTODON_BASE_URL", "")

    if not access_token or not api_base_url:
        print(
            "You must set both a MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL environment variable"
        )
        exit(1)

    return Mastodon(access_token=access_token, api_base_url=api_base_url)


def get_time_in_london():
    now = datetime.datetime.now(pytz.timezone("Europe/London"))
    return now.hour % 12, now.day, now.month


def get_big_ben_image_path(hour, day, month):
    if month == 1 and day == 1 and hour == 0:
        filename = "newyear.jpg"
    else:
        filename = f"{hour}.jpg"

    return "images/" + filename


def post_to_mastodon(image_path, hour):
    mastodon = get_mastodon()
    photo = mastodon.media_post(image_path, "image/jpeg")
    mastodon.status_post(("BONG " * hour).rstrip(), media_ids=photo)


def handler(event, context):
    hour, day, month = get_time_in_london()
    image_path = get_big_ben_image_path(hour, day, month)
    post_to_mastodon(image_path, hour)

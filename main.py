from mastodon import Mastodon
import datetime
import os
import pytz


def get_mastodon() -> Mastodon:
    """Creates an instance of the Mastodon Class

    Returns:
        Mastodon: The instance of the Mastodon Class
    """
    access_token = os.environ.get("MASTODON_ACCESS_TOKEN", "")
    api_base_url = os.environ.get("MASTODON_BASE_URL", "")

    if not access_token or not api_base_url:
        print(
            "You must set both a MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL environment variable"
        )
        exit(1)

    return Mastodon(access_token=access_token, api_base_url=api_base_url)


def get_time_in_london() -> tuple[int, int, int]:
    """Gets the current time in London right now

    Returns:
        tuple[int, int, int]: A tuple with the hour (12 hour clock), day of the month and month of the year
    """
    now = datetime.datetime.now(pytz.timezone("Europe/London"))
    return int(now.strftime("%I")), now.day, now.month


def get_big_ben_image_path(hour: int, day: int, month: int) -> str:
    """Gets an image of Big Ben given the time

    Args:
        hour (int): The hour in London (12 hour clock)
        day (int): The day of the month in London
        month (int): The month of the year in London

    Returns:
        str: The relative path of a JPEG image
    """
    if month == 1 and day == 1 and hour == 12:
        filename = "newyear.jpg"
    else:
        filename = f"{hour}.jpg"

    return "images/" + filename


def post_to_mastodon(image_path: str, hour: int):
    """Post to Mastodon

    Args:
        image_path (str): The path of a JPEG image
        hour (int): The time to bong for
    """
    mastodon = get_mastodon()
    photo = mastodon.media_post(image_path, "image/jpeg")
    mastodon.status_post(("BONG " * hour).rstrip(), media_ids=photo)


def handler(event, context):
    hour, day, month = get_time_in_london()
    image_path = get_big_ben_image_path(hour, day, month)
    post_to_mastodon(image_path, hour)

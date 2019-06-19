from mastodon import Mastodon
import datetime
import os
import pytz


def handler(event, context):
    access_token = os.environ.get('MASTODON_ACCESS_TOKEN', '')
    api_base_url = os.environ.get('MASTODON_BASE_URL', '')

    if not access_token or not api_base_url:
        print('You must set both a MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL environment variable')
        exit(1)

    mastodon = Mastodon(
        access_token=access_token,
        api_base_url=api_base_url
    )

    hour = int(datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%I'))
    print(str(hour))
    photo = mastodon.media_post('images/' + str(hour) + '.jpg')
    sadmsg = '*Sadly and quietly to self: '
    mastodon.status_post(sadmsg + ('BONG ' * hour).rstrip(), media_ids=photo)

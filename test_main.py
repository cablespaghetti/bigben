import os

from freezegun import freeze_time
from unittest import TestCase, mock

from main import handler


class BigBenTestSuite(TestCase):
    def test_errors_without_creds(self):
        with self.assertRaises(SystemExit) as cm:
            handler(None, None)

        self.assertEqual(cm.exception.code, 1)

    @mock.patch.dict(
        os.environ,
        {"MASTODON_ACCESS_TOKEN": "foo", "MASTODON_BASE_URL": "banana.com"},
    )
    @mock.patch("main.Mastodon")
    @freeze_time("2000-01-02 22:02:02")
    def test_happy_case(self, FakeMastodon):
        mastodon = FakeMastodon()
        handler(None, None)
        mastodon.media_post.assert_called_once_with("images/10.jpg", "image/jpeg")
        mastodon.status_post.assert_called_once_with(
            "BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG", media_ids=mock.ANY
        )

    @mock.patch.dict(
        os.environ,
        {"MASTODON_ACCESS_TOKEN": "foo", "MASTODON_BASE_URL": "banana.com"},
    )
    @mock.patch("main.Mastodon")
    @freeze_time("2000-01-02 00:02:02")
    def test_midnight_case(self, FakeMastodon):
        mastodon = FakeMastodon()
        handler(None, None)
        mastodon.media_post.assert_called_once_with("images/12.jpg", "image/jpeg")
        mastodon.status_post.assert_called_once_with(
            "BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG",
            media_ids=mock.ANY,
        )

    @mock.patch.dict(
        os.environ,
        {"MASTODON_ACCESS_TOKEN": "foo", "MASTODON_BASE_URL": "banana.com"},
    )
    @mock.patch("main.Mastodon")
    @freeze_time("2000-01-01 00:02:02")
    def test_happy_new_year_case(self, FakeMastodon):
        mastodon = FakeMastodon()
        handler(None, None)
        mastodon.media_post.assert_called_once_with("images/newyear.jpg", "image/jpeg")
        mastodon.status_post.assert_called_once_with(
            "BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG",
            media_ids=mock.ANY,
        )

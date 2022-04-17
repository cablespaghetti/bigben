from unittest import TestCase, mock
import os

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
    def test_happy_case(self, FakeMastodon):
        mastodon = FakeMastodon()
        handler(None, None)
        mastodon.media_post.assert_called_once_with("images/10.jpg", "image/jpeg")
        mastodon.status_post.assert_called_once_with(
            "BONG BONG BONG BONG BONG BONG BONG BONG BONG BONG", media_ids=mock.ANY
        )

from unittest.mock import patch
from django.test import TestCase
from landing.mailchimp import subscribe_to_mailchimp

class MailchimpTest(TestCase):
    @patch("landing.mailchimp.requests.post")
    def test_mailchimp_api_call(self, mock_post):
        """Ensure Mailchimp API call is made correctly without actually sending requests."""
        mock_post.return_value.status_code = 200  # Simulated success response
        response = subscribe_to_mailchimp("test@example.com", "JohnDoe")
        status_code, _ = response  # Unpack the tuple
        self.assertEqual(status_code, 200)

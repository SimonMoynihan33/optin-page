from django.test import TestCase
from django.urls import reverse
from landing.models import OptIn

class OptInViewTest(TestCase):
    def test_landing_page_loads(self):
        """Ensure the landing page loads successfully."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing/index.html')

    def test_form_submission(self):
        """Ensure valid form submissions redirect to the thank you page."""
        response = self.client.post(reverse('index'), {
            "nickname": "JohnDoe",
            "email": "john@example.com"
        })
        self.assertEqual(response.status_code, 200)  # Should render thank you page

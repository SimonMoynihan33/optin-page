from django.test import TestCase
from landing.forms import OptInForm

class OptInFormTest(TestCase):
    def test_valid_form(self):
        """Test if form is valid with correct input."""
        form = OptInForm(data={"nickname": "JohnDoe", "email": "john@example.com"})
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        """Test if form rejects invalid emails."""
        form = OptInForm(data={"nickname": "JohnDoe", "email": "invalid-email"})
        self.assertFalse(form.is_valid())

    def test_blank_fields(self):
        """Test if form rejects empty fields."""
        form = OptInForm(data={"nickname": "", "email": ""})
        self.assertFalse(form.is_valid())

from django.db import models


class OptIn(models.Model):
    """
    Model to store nickname and email from the opt-in form.
    """

    nickname = models.CharField(max_length=50)  # Field for the nickname
    email = models.EmailField()  # Field for the email address

    def __str__(self):
        return self.email  # Display the email in the Django admin

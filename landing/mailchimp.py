import requests
from django.conf import settings

def subscribe_to_mailchimp(email, nickname):
    url = f"https://us1.api.mailchimp.com/3.0/lists/{settings.MAILCHIMP_AUDIENCE_ID}/members/"
    headers = {
        "Authorization": f"apikey {settings.MAILCHIMP_API_KEY}"
    }
    data = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {
            "FNAME": nickname
        }
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code, response.json()

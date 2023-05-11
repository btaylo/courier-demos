#!/usr/bin/python

from trycourier import Courier

client = Courier(auth_token="API KEY GOES HERE")  # Replace with production API key

resp = client.send_message(
  message={
    "template": "QJAQ20TN9TM90QNRWNE7TN1NHF8J",  # Replace with the actual notification ID
    "to": {
        "email":"someone@example.com"  # Replace with the recipient email address
    },
  }
)

#!/usr/bin/python

from trycourier import Courier

client = Courier(auth_token="API KEY GOES HERE")   # Replace with actual API key

resp = client.send_message(
  message={
    "to": {"email":"someone@example.com"},  # Replace with recipient email address
    "template": "QJAQ20TN9TM90QNRWNE7TN1NHF8J",  # Replace with actual notification ID
    "data": {}
  }
)

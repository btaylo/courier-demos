#!/usr/bin/python

from trycourier import Courier

client = Courier(auth_token="pk_prod_N671XW6PREMS0EMX67XMTPWAYTQW")

resp = client.send_message(
  message={
    "to": {"email":"brandon@wizardondemand.com"},
    "template": "QJAQ20TN9TM90QNRWNE7TN1NHF8J",
    "data": {}
  }
)

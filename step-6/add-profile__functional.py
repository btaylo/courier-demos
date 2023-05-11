#!/usr/bin/python


from trycourier import Courier


client = Courier(auth_token="pk_prod_N671XW6PREMS0EMX67XMTPWAYTQW")

resp = client.profiles.add(
  "BRANDON", # Add an ID that can be used to uniquely identify the recipient
  {
    "email": "brandon@wizardondemand.com", # Replace with the email address of the recipient
    "name": "Brandon Taylor" # Replace with the name of the recipient
  }
)





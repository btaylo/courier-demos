#!/usr/bin/python


from trycourier import Courier


client = Courier(auth_token="API KEY GOES HERE")  # Replace with production API key

resp = client.profiles.add(
  "PROFILE_ID", # Add an ID that can be used to uniquely identify the recipient
  {
    "email": "someone@example.com", # Replace with the email address of the recipient
    "name": "Someone Name" # Replace with the name of the recipient
  }
)





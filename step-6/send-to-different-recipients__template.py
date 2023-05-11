#!/usr/bin/python


from trycourier import Courier


client = Courier(auth_token="API KEY GOES HERE")  # Replace with production API key


resp = client.automations.invoke(
    automation={
      'steps': [
        {
          # This notification sends to the email address of "PROFILE_ID_1"
          "action": "send",
          "template": "QJAQ20TN9TM90QNRWNE7TN1NHF8J", # Replace with your 1st actual notification ID
          "recipient": "PROFILE_ID_1", # Replace with your actual PROFILE_ID
        },
        {
          "action": "delay",
          "duration": "1 minutes",
        },
        {
          # This notification sends to the email address of "PROFILE_ID_2"
          "action": "send",
          "template": "X0G40J35NP4MS0GRWD67Q0CTBJA0", # Replace with your 2nd actual notification ID
          "recipient": "PROFILE_ID_2", # Replace with your actual PROFILE_ID
        },
      ],
    },
)




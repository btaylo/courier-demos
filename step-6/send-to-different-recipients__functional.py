#!/usr/bin/python


from trycourier import Courier


client = Courier(auth_token="pk_prod_N671XW6PREMS0EMX67XMTPWAYTQW")


resp = client.automations.invoke(
    automation={
      'steps': [
        {
          'action': 'send',
          "template": "QJAQ20TN9TM90QNRWNE7TN1NHF8J", # Replace with your 1st actual notification ID
          "recipient": "BRANDON", # This notification sends to the email address of "PROFILE_ID_1"
        },
        {
          "action": "delay",
          "duration": "1 minutes",
        },
        {
          'action': 'send',
          "template": "X0G40J35NP4MS0GRWD67Q0CTBJA0", # Replace with your 2nd actual notification ID
          "recipient": "BRANDON_STEM", # This notification sends to the email address of "PROFILE_ID_2" },
        },
      ],
    },
)




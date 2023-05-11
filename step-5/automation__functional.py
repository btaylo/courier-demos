#!/usr/bin/python


from trycourier import Courier
import sched
import time



def schedule_notification(interval, s):
  send_notification()
  s.enter(interval, 1, schedule_notification)


def send_notification():
  client = Courier(auth_token="pk_prod_N671XW6PREMS0EMX67XMTPWAYTQW")

  resp = client.automations.invoke(
    automation={
      'steps': [
        {
          'action': 'send',
           "template": "QJAQ20TN9TM90QNRWNE7TN1NHF8J" # Replace with your actual notification ID
        },
        {
          "action": "delay",
          "duration": "1 minutes"
        },
        {
          'action': 'send',
          "template": "5VGC2H0P28M1G1KFJ6JRNTJEG361" # Replace with your actual notification ID
        },
      ],
    },
    recipient="SAMPLE_RECIPIENT_ID", # Unique identifier of the recipient
    profile={
      "email": "someone@example.com" # Replace with the email address of the recipient
    },
  )


# start
s = sched.scheduler(time.time, time.sleep)
interval = 3600 * 24

schedule_notification(s)
s.run()



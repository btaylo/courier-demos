#!/usr/bin/python


from trycourier import Courier
import sched
import time



def schedule_notification(interval, s):
  send_notification()

  # delay (in seconds), priority, function to call, command line args (as tuple)
  s.enter(interval, 1, schedule_notification, (interval, s, ))


def send_notification():
  print("Execute automation: ", time.time())

  client = Courier(auth_token="API KEY GOES HERE")  # Replace with production API key

  # Automation to send one notification, with a delay, and then another
  resp = client.automations.invoke(
    automation={
      'steps': [
        {
          "action": "send",
          "template": "QJAQ20TN9TM90QNRWNE7TN1NHF8J" # Replace with your 1st actual notification ID
        },
        {
          "action": "delay",
          "duration": "1 minutes"
        },
        {
          "action": "send",
          "template": "X0G40J35NP4MS0GRWD67Q0CTBJA0" # Replace with your 2nd actual notification ID
        },
      ],
    },
    recipient="SAMPLE_RECIPIENT_ID", # Unique identifier of the recipient (optional to change, but line must be there in the request)
    profile={
      "email": "someone@example.com" # Replace with the email address of the recipient
    },
  )



# setup scheduler
s         = sched.scheduler(time.time, time.sleep)
interval  = 60 * 60 * 24  # execute automation once per day (interval must be in seconds)
schedule_notification(interval, s)

# run scheduler and execute automation once per day
print ("Hit Ctrl-C to stop")
s.run()


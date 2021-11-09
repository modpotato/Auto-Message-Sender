import requests
import time
from time import sleep

days = int(input('Days already passed: '))
webhook = input('Webhook URL: ')
usernameinput = input('Webhook username: ')

dayspassed = days

data = {
    "content" : dayspassed,
    "username" : usernameinput
}

while True:
  requests.post(webhook, json=data)
  time.sleep(86400)
  dayspassed = (dayspassed + 1)
  data = {
    "content" : dayspassed,
    "username" : usernameinput
  }

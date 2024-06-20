# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1xxxxxxxxxx',
    body='Hello ji',
    to='+91xxxxxxxxxx',
    media_url="https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif"
)

# MM6ca9bc56417cd9d52dcb8636cbf6e9fa
print(message.sid)

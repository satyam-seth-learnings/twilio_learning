# https://www.twilio.com/docs/voice/quickstart/python#make-a-phone-call-using-twilio

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to=os.environ['TO_NUMBER'],
    from_=os.environ['FROM_NUMBER']
)

print(call.sid)

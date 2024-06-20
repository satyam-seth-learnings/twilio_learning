# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
    url='https://handler.twilio.com/twiml/EHa7fbbb1c9ba18fe1a43598bde4376a92',
    to='+917235973436',
    from_='+17175368041'
)

# CAc4f14780f35d23a522625b2314a6cce2
print(call.sid)

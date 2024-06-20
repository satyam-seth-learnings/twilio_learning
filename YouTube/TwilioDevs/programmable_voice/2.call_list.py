# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

calls = client.calls.list(limit=20)

for record in calls:
    print(record.sid)

# CA8ec5aced94409d0c0010a68b08a4366e
# CAc4f14780f35d23a522625b2314a6cce2
# CAe5971abbcc1c48b467df07b09f95d4d2
# CAf083587505c7bd5aa9680f5f68c0016f
# CAe26b40cca1c87760392c0e446c5adfdc
# CAe9c3ec833587a7357f798bf58cf6879b
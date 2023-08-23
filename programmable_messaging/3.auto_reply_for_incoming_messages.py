# https://www.twilio.com/docs/messaging/twiml/message
# We can generate dynamic TwiMl response

from twilio.twiml.messaging_response import MessagingResponse

response = MessagingResponse()
response.message('Store Location: 123 Easy St.')

print(response)
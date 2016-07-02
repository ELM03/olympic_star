# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC3812d37fd9f78cf4f9fcf8327c13eb96"
auth_token = "8eed43c4a82bcca4d8575b81eae96af2"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+818041324020", from_="+12513335896",
                                     body="Hello Yoshiki")

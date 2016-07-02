# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC36907006a673700389534d987442aaec"
auth_token = "cb59e51a87837a3ab111a519bf7a4da7"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+12513335896", from_="+12513336112",
                                     body="35.633998,139.715828")

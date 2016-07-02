from flask import Flask, request, redirect
import twilio.twiml
from datetime import *

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

app = Flask(__name__)

# Try adding the user list

callers = {
  "+818041324020":"Yoshiki Kanda", 
  "+12513336613":"Tetsuya 2"
}

# Find these values at https://twilio.com/user/account


@app.route("/", methods=['GET','POST'])
def hello_monkey():
  """Respond to incoming calls with a simple text message."""
  from_number = request.values.get('From',None)
  from_body = request.values.get('Body',None)

  if from_number in callers:
    message = callers[from_number] + ", thanks Tetsuya2 " + str(from_body)
  else:
    message = "Thanks unknown user for your message!" + str(from_body)


  resp = twilio.twiml.Response()
  resp.message(message)

  account_sid = "AC3812d37fd9f78cf4f9fcf8327c13eb96"
  auth_token = "8eed43c4a82bcca4d8575b81eae96af2"
  client = TwilioRestClient(account_sid, auth_token)
  message = client.messages.create(to="+819087101147", from_="+12513335896", body = "OK"+":"+str(from_body))
  return str(resp)


if __name__ == "__main__":
  app.run(debug=True,host='47.88.192.79')

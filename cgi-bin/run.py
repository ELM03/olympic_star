from flask import Flask, request, redirect
import twilio.twiml
from datetime import *
import MySQLdb
import math
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

app = Flask(__name__)

# Try adding the user list

callers = {
  "+1(251)3336613":"Tetsuya"
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

  # Get the geographic info. of Drone
  l = str(from_body).split(",")


  connector = MySQLdb.connect(host="localhost",db="db1",user="yoshiki",charset="utf8")
  cursor = connector.cursor()

  
  cursor.execute("select * from drones");
  
  records= cursor.fetchall()
  distance = []
  i = 0
  for record in records:
    distance.append(math.sqrt( math.pow(float(l[0]) - record[1], 2) + math.pow(float(l[1]) - record[2],2)))
    print distance[i]
    i = i + 1

  min_dist = distance[0]  
  i = 0
  k = 0

  for dist in distance:
    k = 0
    if min_dist > dist:
      k = i
    min_dist = dist
    i = i + 1

  cursor.close()
  connector.close()

 
  print k 
  message = client.messages.create(to="+819087101147", from_="+12513335896", body = "Drone is coming in 30 sec. Drone ID:"+str(k))
  return str(resp)


if __name__ == "__main__":
  app.run(debug=True,host='47.88.192.79')

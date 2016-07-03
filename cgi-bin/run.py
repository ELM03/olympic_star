from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
from datetime import *
import MySQLdb
import math
import time

# Crate the Flask web application
app = Flask(__name__)

# Find these values at https://twilio.com/user/account

@app.route("/", methods=['GET','POST'])
def responseSms():
  """Respond to incoming calls with a simple text message."""
  from_number = request.values.get('From',None)
  from_body = request.values.get('Body',None)
  

  #Return OK if recieved the SMS
  message = "OK"
  resp = twilio.twiml.Response()
  resp.message(message)


  # Get the geographic info. of Drone
  l = str(from_body).split(",")
  connector = MySQLdb.connect(host="localhost",db="db1",user="yoshiki",charset="utf8")
  cursor = connector.cursor()
  
  cursor.execute("select * from drones");
  records= cursor.fetchall()
  distance = []
  i = 0
  #Calculate the distance from the current location and the nearest drone
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

  #Print the nearest drone's number 
  print k 

  
  # Get the Access key and Authentication token
  account_sid = "AC3812d37fd9f78cf4f9fcf8327c13eb96"
  auth_token = "8eed43c4a82bcca4d8575b81eae96af2"
  client = TwilioRestClient(account_sid, auth_token)

  # Send message with the nearest drone's information 
  message = client.messages.create(to="+819087101147", from_="+12513335896", body = "Drone is coming in 15 sec. Drone ID:"+str(k))
  time.sleep(15)

  print "15 sec. has finished"
  message = client.messages.create(to="+819087101147", from_="+12513335896", body = "Drone got arrived. Drone ID:"+str(k))

  
  connector = MySQLdb.connect(host="localhost",db="db1",user="yoshiki",charset="utf8")
  cursor = connector.cursor()
  r = cursor.execute("update drones set longtitude=35.633998, latitude=139.715828 where drone_id=4")
  connector.commit()
  cursor.close()
  connector.close()

  connector = MySQLdb.connect(host="localhost",db="db1",user="yoshiki",charset="utf8")
  cursor = connector.cursor()
  
  cursor.execute("select * from drones");
  records= cursor.fetchall()
  # Check if the selected query is correct
  for record in records:
    print record

  cursor.close()
  connector.close()

  time.sleep(10)

  connector = MySQLdb.connect(host="localhost",db="db1",user="yoshiki",charset="utf8")
  cursor = connector.cursor()
  r = cursor.execute("update drones set longtitude=35.6581, latitude=139.701742 where drone_id=4")
  connector.commit()
  cursor.close()
  connector.close()

  connector = MySQLdb.connect(host="localhost",db="db1",user="yoshiki",charset="utf8")
  cursor = connector.cursor()
  
  cursor.execute("select * from drones");
  records= cursor.fetchall()
  for record in records:
    print record


  cursor.close()
  connector.close()


  print "Drone said good bye to you!"

  return str(resp)


if __name__ == "__main__":
  app.run(debug=True,host='47.88.192.79')

from firebase import Firebase
import requests
from time import sleep 

# JSOn URL : https://attendance-53e75-default-rtdb.firebaseio.com/.json
# https://stackoverflow.com/questions/36528079/how-to-retrieve-data-from-firebase-using-python

config = {
  "apiKey" : "AIzaSyDO3JR1-ZiNadGKOLUe0hRXbcdSgfvcMIE",
  "authDomain" : "attendance-53e75.firebaseapp.com",
  "databaseURL" : "https://attendance-53e75-default-rtdb.firebaseio.com",
  "projectId" : "attendance-53e75",
  "storageBucket" : "attendance-53e75.appspot.com",
  "messagingSenderId" : "380525800546",
  "appId": "1:380525800546:web:d080cfcc66f08c14e6353b",
  "measurementId": "G-EQ2B54C9HX"
}

API_ENDPOINT = 'http://127.0.0.1:8000/attendance/rfid/'

firebase = Firebase(config)
db = firebase.database()
"21iojiqejio12ejoi2ejio12"
while True:
    today_attendance = db.get()

    if today_attendance.val():
          for key, value in today_attendance.val().items():
            data = {'rfid' : value} 
            print("Attendance Added")
            requests.post(url = API_ENDPOINT, data = data)
            db.child(key).remove()
    print("Next Iteration")
    sleep(60)
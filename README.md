# Attendence

 - [x] **Profile Model Details** 
 - username
 - profile pic
 - roll number
 - Dept
 - Bus number
 - Location (place of attendance taken)
 - Email 
 - RF's UUid (HEX - max=16)
 - is_fees_Paid (Bool)

 

**Admin** 
 - [x] Admin panel 
 - [x] Register (Single Register page)
 - [x] Attendance Status  (Table only one day) 
 - [x] Attendance Status  (Sheet CSV download manually) 
 - [x] Profile (single user details)

**User** 
- [x] login  (using roll number)
- [x] RF id writing page  (using RF UUid)
        curl -X POST -d "rfid=21iojiqejio12ejoi2ejio12" http://127.0.0.1:8000/attendance/rfid/

- [x] mail users while attendance taken  

 
**About us page**

 


#### Send post request 
**sample**

curl -d '{"rfid" : "21iojiqejio12ejoi2ejio12"}'  --header "Content-Type: application/json" --request POST http://127.0.0.1:8000/attendance/rfid/


# Changes
        - Datetime in http://127.0.0.1:8000/attendance-today/
        - Format CSV : username, Roll Number, Department, Bus Number, email, Attendance Status, Date Time, Fees Paid Status
        - Date time format DD/MMM, YYYY HH:MM:SS

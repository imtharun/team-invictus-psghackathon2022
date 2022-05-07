import db
import time 

print ("Welcome to student attendance system")
db.checktoday()
curr_staff = 0
while 1:
    print("Enter tag id:")
    tag = input()
    if(curr_staff==0):
        curr_staff = db.scanstaff(tag)
    else:
        db.addattendance(tag,curr_staff)


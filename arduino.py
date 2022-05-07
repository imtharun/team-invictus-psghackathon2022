import db
import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print (arduino.readline()) #read the serial data and print it as line
print ("Enter 1 to get LED ON & 0 to get OFF")

curr_staff = 0
 
while 1:      #Do this in loop

    var = input() #get input from user

    tag = arduino.readline()
    db.addattendance(tag,curr_staff)
#Use this after connecting the arduino to RFID reader
from curses import baudrate
import db
import serial
import time 
com = 'COM3' 
baudrate = 9600


arduino = serial.Serial(com,baudrate)

time.sleep(2) 

print ("Welcome to student attendance system")

curr_staff = 0
while 1:
    tag = arduino.readline()      #read input from arduino serial
    if(curr_staff==0):
        curr_staff = db.scanstaff(tag)    
    db.addattendance(tag,curr_staff)
from base64 import encode, encodebytes
import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print (arduino.readline()) #read the serial data and print it as line
print ("Enter 1 to get LED ON & 0 to get OFF")

 
while 1:      #Do this in loop

    var = input() #get input from user
   
    
    if (var == '1'): #if the value is 1
        hi = '1'
        arduino.write(hi.encode()) #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == '0'): #if the value is 0
        hi = '0'
        arduino.write(hi.encode()) #send 0
        print ("LED turned OFF")
        time.sleep(1)

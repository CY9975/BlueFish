#Imports

Required imports
import RPi.GPIO as GPIO
import time
import os
import serial

#GPIO Pins
Fish = 18
count=0



GPIO.setmode(GPIO.BOARD)
GPIO.setup(Fish, GPIO.IN)

def line():

	if (GPIO.input(Fish)==1):
		x=1
		currFish=GPIO.input(Fish)
		time.sleep(3)
		lastFish=GPIO.input(Fish)
		if (currFish==lastFish):
			AT_COMMANDS=["AT+CMSS=6\r"]
			
			for i in AT_COMMANDS:
				msg = (i).encode()#Convert str to bytes
				ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)#Establish com port
				ser.write(msg)#Write AT command to serial port
				ser.close()#Closes serial port.
			
			print("Message Sent")
			
			
	if (GPIO.input(Fish)==0):
		x=0
		time.sleep(.1)
		print(x)
	
	return x
	
	
		
def BlueFish():
    
    while count==0:
		y=line()
		if (y==1):
			break

BlueFish()

		

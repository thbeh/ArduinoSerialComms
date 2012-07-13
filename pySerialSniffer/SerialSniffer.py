#requires pyserial (pip install pyserial) to work
#by Dan Reed 7/13/12

import serial
from time import sleep

def loop():
	buttonPressed = ser.read()
	###############uncomment for a debug stream
	#print buttonPressed
	if(buttonPressed=='1'):
		print 'About to do some magic, stand back... this could be dangerous.'
		doSomeMagic()
	#remove comments to debug the serial stream
	#elif(buttonPressed != '0'):
	#	print 'echoing status->' + '#' +buttonPressed +'#'

def doSomeMagic():
	print 'beginning magic'
	ser.write('2') #denotes event received
	sleep(3)
	print 'uhhhh, we made progress or something'
	ser.write('3') #denotes progress made
	sleep(3)
	print 'work complete!'
	ser.write('4') #denotes process finished
	sleep(3)
	print 'done with the magic'

#this is pretty fragile, set it to whatever comms port your 'duino is hooked up to until I find a better solution
ser = serial.Serial('/dev/tty.usbmodem1421', 9600, timeout=1)
while(True):
	loop()





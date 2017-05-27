#code for comms for UOSTAR

import serial
import Adafruit_BBIO.UART as UART
  
UART.setup("UART1")

ser = serial.Serial(port = '/dev/ttyO1', baudrate=9600)
while(1):
	while ser.inWaiting()==0:
		pass
	output = ser.readline()
	print output

 
# Eventually, you'll want to clean up, but leave this commented for now, 
# as it doesn't work yet
#UART.cleanup()

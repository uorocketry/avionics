#code for comms for UOSTAR

import Adafruit_BBIO.UART as UART
import serial
  
UART.setup("UART2")

ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
	print "Port Open"
    ser.write("Test Transmission")
ser.close()
 
# Eventually, you'll want to clean up, but leave this commented for now, 
# as it doesn't work yet
#UART.cleanup()

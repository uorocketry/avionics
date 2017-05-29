import serial
import Adafruit_BBIO.UART as UART

UART.setup("UART1")

ser = serial.Serial(port = '/dev/ttyO1', baudrate=9600)
while(1):
	while ser.inWaiting()==0:
		pass
	output = ser.readline()
	print output

 

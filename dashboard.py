import serial
import tk
#this module runs on the computer that receives telemetry to receive the rocket data

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
ser.open()
while True:
    if ser.isOpen():
        data = ser.read(ser.inWaiting())
        print data

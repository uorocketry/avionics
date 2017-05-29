import serial
#this module runs on the computer that receives telemetry to receive the rocket data

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
ser.open()
while True:
    print(ser.readline())

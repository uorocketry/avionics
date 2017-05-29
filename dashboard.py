import serial
import Tkinter
#this module runs on the computer that receives telemetry to receive the rocket data


begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)


ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
ser.open()
#while True:
#    if ser.isOpen():
#        data = ser.read(ser.inWaiting())
#        print data
while True:
    print(ser.readline())

from collections import namedtuple
from threading import Thread
from Adafruit_I2C import Adafruit_I2C
import rocket_state
import Adafruit_BBIO.UART as UART
import serial
import uostar
import datetime
from Observer import Observer, Observable

class SensorProducer(Thread, Observable):
    def __init__(self):
        self.current_state = uostar.RocketState()

    def run():
        record_state()

    def record_state():



class Sensor(object):
    def __init__(self):
        Object.__init__(self)
    def get_data():
        return None



class GPSSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        UART.setup("UART1")
        ser = serial.Serial(port = '/dev/ttyO1', baudrate=9600)

    def get_data():
        return # a gps object defined in uostar.py

class AccelerationSensor(Sensor):
    def __init__(self):
        self.i2c = Adafruit_I2C(0x53,2) #accelerometer is i2c address 53 in ic2-2
        i2c.write8(45, 8) #powering on the accelerometer

    def get_data():
        #z-acceleration = i2c.readS8(54)




    #transmit data asynchronously to application after putting it in standard format
def poll_sensors():
    accel=get_accel() #get accelerometer data
    gps=get_gps()   #get gps data
    baro=get_baro()  #get pressure data
    prev_rocket_state =
    return uostar.RocketState(accel,gps,datetime.datetime.now())

def get_gps():
    return 1#poll gps and return gps data

def get_accel():
    #i2c.write8(45, 8) #powering on the accelerometer
    #return i2c.readS8(54)#return
    return 2
    #poll accelerometer and return acceleration value




if __name__ == '__main__':
        print SensorProducer.run()

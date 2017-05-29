from threading import Thread
from Adafruit_I2C import Adafruit_I2C
import rocket_state
import Adafruit_BBIO.UART as UART
import serial
import rocket
import datetime
from sensor_observer import publisher as Observable

class SensorProducer2(Thread, Observable):
    def __init__(self):
        Thread.__init__(self,group=None, target=None, name=None, args=(), kwargs={})
        #super(SensorProducer,self).__init__()
        self.current_state = rocket.State(None,datetime.datetime.now(),0,None)
        self.gps_sensor = GPSSensor()
        self.accelerometer = AccelerationSensor()

    #def record_state(r):
    #    self.current_state = r

    def run(self):
        print"ran"
        if self.current_state.previous_state == None:
                a = rocket.Acceleration()
                g = rocket.GPS()
                r = rocket.State(None, datetime.datetime.now(), a, g)
        else:
                a = accelerometer.read()
                g = gps_sensor.read()
                r = rocket.State(self.current_state.previous_state, datetime.datetime.now(), a, g)

        #callback with
        #record_state(r)

        self.current_state = r


class SensorProducer(object):
    def __init__(self):
        super(SensorProducer,self).__init__()
        self.current_state = rocket.State(None,datetime.datetime.now(),0,None)
        self.gps_sensor = GPSSensor()
        self.accelerometer = AccelerationSensor()

    def record_state(r):
        self.current_state = r

    def __str__(self):
        "rocket"

    def produce(self):
        #print"produced"
        if self.current_state.previous_state == None:
                a = rocket.Acceleration()
                g = rocket.GPS()
                r = rocket.State(None, datetime.datetime.now(), a, g)
        else:
                a = accelerometer.read()
                g = gps_sensor.read()
                r = rocket.State(self.current_state.previous_state, datetime.datetime.now(), a, g)
        #callback with
        #record_state(r)
        return r



class Sensor(object):
    def __init__(self):
        object.__init__(self)
    def read():
        return None



class GPSSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        #UART.setup("UART1")
        #self.ser = serial.Serial(port = '/dev/ttyO1', baudrate=9600)

    def read():
        return rocket.GPS()# a gps object defined in uostar.py

class AccelerationSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        #self.i2c = Adafruit_I2C(0x53,2) #accelerometer is i2c address 53 in ic2-2
        #i2c.write8(45, 8) #powering on the accelerometer

    def read():
        #z-acceleration = i2c.readS8(54)
        return rocket.Acceleration()



    #transmit data asynchronously to application after putting it in standard format
#def poll_sensors():
#    accel=get_accel() #get accelerometer data
#    gps=get_gps()   #get gps data
#    baro=get_baro()  #get pressure data
#    prev_rocket_state =
#    return uostar.RocketState(accel,gps,datetime.datetime.now())

#def get_gps():
#    return 1#poll gps and return gps data

#def get_accel():
    #i2c.write8(45, 8) #powering on the accelerometer
    #return i2c.readS8(54)#return
#    return 2
    #poll accelerometer and return acceleration value




if __name__ == '__main__':
        print SensorProducer.run()

from threading import Thread
import rocket_state
import serial
import rocket
import datetime
from sensor_observer import publisher as Observable
from time import sleep

class SensorProducer(object):
    def __init__(self):
        super(SensorProducer,self).__init__()
        self.current_state = rocket.State(None,None,0,None)
        self.gps_sensor = GPSSensor()
        self.accelerometer = AccelerationSensor()

    def record_state(self,r):
        self.current_state.previous_state = r

    def produce(self):
        if self.current_state.previous_state == None:
            a = rocket.Acceleration()
            g = rocket.GPS()
            r = rocket.State(None, str(datetime.datetime.now()), a, g)
        else:
            a = self.accelerometer.read()
            g = self.gps_sensor.read()
            r = rocket.State(self.current_state.previous_state, str(datetime.datetime.now()), a, g)
        self.record_state(r)
        return r



class Sensor(object):
    def __init__(self):
        object.__init__(self)
    def read():
        return None



class GPSSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    def read(self):
        return rocket.GPS(45.3607600,-75.7284500)# a gps object defined in uostar.py

class AccelerationSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    def read(self):
        return rocket.Acceleration(0,0,-9.8)


if __name__ == '__main__':
        print SensorProducer.run()

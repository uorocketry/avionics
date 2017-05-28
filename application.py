from threading import Thread
import time
import sensor_producer
import sensor_observer
from Queue import Queue
import serial
import json

sensorObservers= []
sensorConsumers= []
queue = Queue(1)

app_data = sensor_observer.publisher()
#app_data.


#highest level class
#it is the subject in the observer pattern
#has a list of all observers

#store the current rocket_state and the previous rocket_state
#use them to integrate acceleration over the time interval to find velocity
#i.e (accel(current state)+accel(previous state))*(time2-time1)/2


#producer Thread
class publisher_thread(Thread):
    def run(self):
        global queue
        while True:
            queue.put(sensor_producer.poll_sensors())
            #print "Produced", string
            time.sleep(0.2)

#thread that receives data from sensor_producer via data_thread
class consumer_thread(Thread):
    def run(self):
        while True:
            data = json.loads(queue.get())
            gps_data = str(data['GPS'] )
            time_data = str(data["Time"])
            #data = queue.get()
            print "Consumed", data
            if ser.isOpen():
                ser.write(str(time_data+"\r\n"))
                #response = ser.read(ser.inWaiting())
            time.sleep(0.2)


#opening the serial port on the beaglebone usb port
ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
ser.open()


publisher_thread().start()
consumer_thread().start()

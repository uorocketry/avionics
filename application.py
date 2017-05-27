from threading import Thread
import time
import sensor_producer
from Queue import Queue

sensorObservers= []
sensorConsumers= []
queue = Queue(1)

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
            queue.put(get_sensor_data())
            #print "Produced", string
            time.sleep(0.2)

#thread that receives data from sensor_producer via data_thread
class consumer_thread(Thread):
    def run(self):
        while True:
            string = queue.get()
            print "Consumed", string
            time.sleep(0.2)

def get_sensor_data():
    sensor_producer.poll_sensors()



publisher_thread().start()
consumer_thread().start()

from threading import Thread, Condition
import time
import sensor_producer
import random


condition = Condition()

#highest level class
#it is the subject in the observer pattern
#has a list of all observers

#store the current rocket_state and the previous rocket_state
#use them to integrate acceleration over the time interval to find velocity

class data_thread(Thread):
    def run(self):
      print "Starting Thread:"
      sensor_producer.poll_sensors()
      print "Exiting Thread"

d_thread = data_thread()

sensorObservers= []
sensorConsumers= []


d_thread.start()

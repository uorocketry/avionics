from threading import Thread, Timer
import time
import dummy_sensor_producer as sensor_producer
import sensor_observer
from Queue import Queue
import serial
import json
import rocket

#global queue
#Queue.Queue has an implentation of publisher/subscriber pattern built into it
#queue = Queue(1)


#highest level class
#it is the subject in the observer pattern, has a list of all observers

#store the current rocket_state and the previous rocket_state
#use them to integrate acceleration over the time interval to find velocity


#producer Thread

class consumer_thread(Thread):
    def run(self):
        print "consumer_thread"
        #while True:
        #    print "hello"
	#main thread deserializes data
            #data = json.loads(queue.get())
            #print "received sensor data at: ", str(data["Time"])
            #app_data.dispatch(data)
            #time.sleep(0.15)

def publisher_data(rocket):
    app_data.dispatch(rocket)


def publish(callback):
    Timer(1, publish, args = (callback,)).start()
    rocket = producer.produce()
    callback(rocket)


class serial_telemetry_subscriber(sensor_observer.subscriber):
    def __init__(self, name, port, baudrate):
        sensor_observer.subscriber.__init__(self,name)
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial()
        self.ser.port = self.port
        self.ser.baudrate = self.baudrate
        self.ser.open()

    def update(self,data):
        if self.ser.isOpen():
            self.ser.write(json.dumps(data.to_dict()))
            self.ser.write("\r\n")


class flight_control_subscriber(sensor_observer.subscriber):
    def __init__(self,name):
        sensor_observer.subscriber.__init__(self,name)
    # TODO: define the update function for flight controller

#create subject
app_data = sensor_observer.publisher()

serial_telemetry_subscriber = serial_telemetry_subscriber("serial","/dev/ttyUSB0",9600)
flight_control_subscriber = flight_control_subscriber("flight control")

app_data.register(serial_telemetry_subscriber)
app_data.register(flight_control_subscriber)

producer = sensor_producer.SensorProducer()

publisher_thread = Thread(target=publish, args=(publisher_data,)).start()
consumer_thread().start()

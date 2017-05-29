from threading import Thread, Timer
import dummy_sensor_producer as sensor_producer
import observer
import serial
import json
import rocket

#main thread, has a callback for the thread running the publish function
# it is the subject in the observer pattern, has a list of all observers

def publisher_data(rocket):
    app_data_subject.dispatch(rocket)


def publish(callback):
    Timer(1, publish, args = (callback,)).start()
    rocket = producer.produce()
    callback(rocket)


class SerialTelemetryObserver(observer.Observer):
    def __init__(self, name, port, baudrate):
        observer.Observer.__init__(self,name)
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


class FlightControlObserver(observer.Observer):
    def __init__(self,name):
        observer.Observer.__init__(self,name)
    # TODO: override the update function for flight controller

app_data_subject = observer.Subject()

serial_telemetry_observer = SerialTelemetryObserver("serial","/dev/ttyUSB0",9600)
flight_control_observer = FlightControlObserver("flight control")

app_data_subject.register(serial_telemetry_observer)
app_data_subject.register(flight_control_observer)

producer = sensor_producer.SensorProducer()

publisher_thread = Thread(target=publish, args=(publisher_data,)).start()
#consumer_thread().start()

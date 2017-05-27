#an implementation of the Observer pattern for rocket data
import serial


ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
ser.open()

class subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, data):
        print('{} got data "{}"'.format(self.name, data))
        if ser.isOpen():
            ser.write(str(data+"\r\n"))
        #opening the serial port on the beaglebone usb port


class publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)

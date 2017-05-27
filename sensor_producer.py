from collections import namedtuple
import threading
import rocket_state
import sensor_observer
#import Adafruit_BBIO.UART as UART
import serial

print "start"

#set up sensor pins to be read
#UART.setup("UART1") #gps
#UART.setup("UART2") #accelerometer
#UART.setup("UART4") #pressure data
#def init(subscriber):
#    publisher = sensor_observer.publisher()
#    publisher.register(subscriber)
#publisher = sensor_observer.publisher()
#publisher.register(subscriber)


    #transmit data asynchronously to application after putting it in standard format
def poll_sensors():
    #threading.Timer(1.0, poll_sensors).start()
    accel=get_accel() #get accelerometer data
    gps=get_gps()   #get gps data
    baro=get_baro()  #get pressure data

    state= rocket_state.parse(accel,gps,baro)

    #print state
    #publisher.dispatch(state)
    return state


def get_gps():
    return 1#poll gps and return gps data

def get_accel():
    return 2#return
    #poll accelerometer and return acceleration value

def get_baro():
    return 4    #poll barometer and return pressure data



if __name__ == '__main__':
    poll_sensors()

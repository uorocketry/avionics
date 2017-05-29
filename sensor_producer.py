from threading import Thread
from Adafruit_I2C import Adafruit_I2C
import rocket_state
import Adafruit_BBIO.UART as UART
import serial
import rocket
import datetime
from sensor_observer import publisher as Observable

class SensorProducerThread(Thread, Observable):
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

    def record_state(self,r):
        self.current_state.previous_state = r



    def produce(self):
        #print"produced"
        if self.current_state.previous_state == None:
                a = rocket.Acceleration()
                g = rocket.GPS()
                r = rocket.State(None, datetime.datetime.now(), a, g)
        else:
                a = self.accelerometer.read()
                g = self.gps_sensor.read()
                r = rocket.State(self.current_state.previous_state, datetime.datetime.now(), a, g)
        #callback with
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
        UART.setup("UART1")
        self.ser = serial.Serial(port = '/dev/ttyO1', baudrate=9600)
        #This sets up variables for useful commands.
        #This set is used to set the rate the GPS reports
        UPDATE_10_sec=  "$PMTK220,10000*2F\r\n" #Update Every 10 Seconds
        UPDATE_5_sec=  "$PMTK220,5000*1B\r\n"   #Update Every 5 Seconds
        UPDATE_1_sec=  "$PMTK220,1000*1F\r\n"   #Update Every One Second
        UPDATE_200_msec=  "$PMTK220,200*2C\r\n" #Update Every 200 Milliseconds
        #This set is used to set the rate the GPS takes measurements
        MEAS_10_sec = "$PMTK300,10000,0,0,0,0*2C\r\n" #Measure every 10 seconds
        MEAS_5_sec = "$PMTK300,5000,0,0,0,0*18\r\n"   #Measure every 5 seconds
        MEAS_1_sec = "$PMTK300,1000,0,0,0,0*1C\r\n"   #Measure once a second
        MEAS_200_msec= "$PMTK300,200,0,0,0,0*2F\r\n"  #Meaure 5 times a second
        #Set the Baud Rate of GPS
        BAUD_57600 = "$PMTK251,57600*2C\r\n"          #Set Baud Rate at 57600
        BAUD_9600 ="$PMTK251,9600*17\r\n"             #Set 9600 Baud Rate
        #Commands for which NMEA Sentences are sent
        ser.write(BAUD_57600)
        sleep(1)
        ser.baudrate=57600
        GPRMC_ONLY= "$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n" #Send only the GPRMC Sentence
        GPRMC_GPGGA="$PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*28\r\n"#Send GPRMC AND GPGGA Sentences
        SEND_ALL ="$PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0*28\r\n" #Send All Sentences
        SEND_NOTHING="$PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*28\r\n" #Send Nothing
        ser.write(UPDATE_200_msec)
        sleep(1)
        ser.write(MEAS_200_msec)
        sleep(1)
        ser.write(GPRMC_GPGGA)
        sleep(1)
        ser.flushInput()
        ser.flushInput()
        print "GPS Initialized"
    def read(self):
        ser.flushInput()
        ser.flushInput()
        while ser.inWaiting()==0:
                pass
        self.NMEA1=ser.readline()
        while ser.inWaiting()==0:
                pass
        self.NMEA2=ser.readline()
        NMEA1_array=self.NMEA1.split(',')
        NMEA2_array=self.NMEA2.split(',')
        if NMEA1_array[0]=='$GPRMC':
                self.timeUTC=NMEA1_array[1][:-8]+':'+NMEA1_array[1][-8:-6]+':'+NMEA1_array[1][-6:-4]
                self.latDeg=NMEA1_array[3][:-7]
                self.latMin=NMEA1_array[3][-7:]
                self.latHem=NMEA1_array[4]
                self.lonDeg=NMEA1_array[5][:-7]
                self.lonMin=NMEA1_array[5][-7:]
                self.lonHem=NMEA1_array[6]
                self.knots=NMEA1_array[7]
        if NMEA1_array[0]=='$GPGGA':
                self.fix=NMEA1_array[6]
                self.altitude=NMEA1_array[9]
                self.sats=NMEA1_array[7]
        if NMEA2_array[0]=='$GPRMC':
                self.timeUTC=NMEA2_array[1][:-8]+':'+NMEA1_array[1][-8:-6]+':'+NMEA1_array[1][-6:-4]
                self.latDeg=NMEA2_array[3][:-7]
                self.latMin=NMEA2_array[3][-7:]
                self.latHem=NMEA2_array[4]
                self.lonDeg=NMEA2_array[5][:-7]
                self.lonMin=NMEA2_array[5][-7:]
                self.lonHem=NMEA2_array[6]
                self.knots=NMEA2_array[7]

        if NMEA2_array[0]=='$GPGGA':
                self.fix=NMEA2_array[6]
                self.altitude=NMEA2_array[9]
                self.sats=NMEA2_array[7]
        return rocket.GPS(self.lonDeg, self.latDeg)

    #def read(self):
    #    return rocket.GPS()# a gps object defined in uostar.py

class AccelerationSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        #self.i2c = Adafruit_I2C(0x53,2) #accelerometer is i2c address 53 in ic2-2
        #i2c.write8(45, 8) #powering on the accelerometer

    def read(self):
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

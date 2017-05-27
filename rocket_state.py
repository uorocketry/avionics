import uostar
from datetime import datetime
def parse(accel, gps, baro):
    x = uostar.Coords(3,4)
    #x.to_string()
    #temporarily just returns a string for testing
    return "altitude: "+accel

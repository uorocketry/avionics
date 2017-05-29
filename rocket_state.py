import rocket
import json

import pprint
from datetime import datetime

def pack(accel, gps, baro):
    x = rocket.Coords(3,4)
    data = {
    "Acceleration":accel,
    "GPS":gps,
    "pressure":baro,
    "Time": str(datetime.now())
    }
    output = json.dumps(data)
    return output

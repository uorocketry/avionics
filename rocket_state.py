import uostar
import json

import pprint
from datetime import datetime

def parse(accel, gps, baro):
    x = uostar.Coords(3,4)

    output = json.dumps({"Acceleration":accel,"GPS":gps,"pressure":baro,"Time": str(datetime.now())})
    #x.to_string()
    #temporarily just returns a string for testing
    return output

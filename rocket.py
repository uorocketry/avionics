import math

class State(object):
    def __init__(self, previous_state, time, acceleration, gps):
        self.previous_state = previous_state
        self.time = time
        self.acceleration = acceleration
        self.gps = gps

        if previous_state == None:
            self.velocity = Velocity(0,0,0)
            self.postion = Position(0,0,0)
        else:
            #time_diff_state = self.time - previous_state.time
            self.velocity = Velocity(0,0,0)
            self.postion = Position(0,0,0)
#            self.velocity = acceleration.apply_to(previous_state.velocity, time_diff_state)
#            self.position = Velocity.apply_to(previous_state.Position, time_diff_state)
    def __str__(self):
        return "rocket"

    def to_dict(self):
        return{
        "time":self.time,
        "acceleration":self.acceleration.to_dict(),
        "gps":self.gps.to_dict(),
        "velocity" :self.velocity.to_dict(),
        #"position" :self.position.to_dict(),
        }


class GPS(object):
    #TODO implement proper version
    def __init__(self, longi=0, lati=0):
        self.longi = longi
        self.lati = lati
    def to_dict(self):
        return{
        "longitude":self.longi,
        "latitude":self.lati
        }



class Vector(object):
    def __init__(self, x, y, z):
        object.__init__(self)
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = other.x + self.x
        y = other.y + self.y
        z = other.z + self.z
        return Vector(x,y,z)
    def to_dict(self):
        return{
        "x":self.x,
        "y":self.y,
        "z":self.z}


class Velocity(Vector):
    def __init__(self, x=0, y=0, z=0):
        Vector.__init__(self, x, y, z)

    def apply_to(self, postion, time):
        x = position.x + self.x * time
        y = position.y + self.y * time
        z = position.z + self.z * time
        return Position(x, y, z)

class Acceleration(Vector):
    def __init__(self, x=0, y=0, z=-9.81):
        Vector.__init__(self, x, y, z)

    def apply_to(self, velocity, time):
        x = velocity.x + self.x * time
        y = velocity.y + self.y * time
        z = velocity.z + self.z * time
        return Velocity(0,0,0)

class Position(Vector):
    def __init__(self, x=0, y=0, z=0):
        Vector.__init__(self, x, y, z)



#TODO implement this

#if __name__ == "__main__"
#do something

#if __name__ == "__main__"

def integrate(t1,t2,y1,y2):
    return (y2+y1)*(t2-t1)/2

class RocketState(Object)
    def __init(accel, gps,rocket_state,time):
        self.previous_state = rocket_state
        self.accel = accel
        self.gps = gps
        self.time = time
        get_velocity()


    def get_velocity():
        if self.velocity == None:
            delta_v = integrate(self.previous_state.time, self.time, self.previous_state.acceleration, self.acceleration )
            self.velocity = self.previous_state.velocity + delta_v
        return self.velocity

    def get_position():



#TODO burn this
class Coords:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def to_string():
        print "("+x+","+y+")"

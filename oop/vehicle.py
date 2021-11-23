class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        Vehicle.__init__(self, max_speed, mileage)
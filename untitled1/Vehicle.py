import math

class Vehicle:

    def __init__(self, name, vehicleType, speed, fuel, powerCapacity, position):
        self.name = name
        self.vehicleType = vehicleType
        self.speed = speed
        self.fuel = fuel
        self.powerCapacity = powerCapacity
        self.position = position
        self.task = None

    def isItDrone(self):
        if self.vehicleType == "Drone":
            return True
        else:
            return False

    def setTask(self,task):
        if self.isItFree():
            self.task = task
    def setFree(self):
        self.task = None

    def isItFree(self):
        if self.task == None:
            return True
        else:
            return False

    # findDistance method finds the distance from current position of the vehicle to the target point
    def findDistance(self, targetPoint):

        x = self.position[0]
        y = self.position[1]

        # x and y are current position of the vehicle

        x1 = targetPoint[0]
        y1 = targetPoint[1]

        # x1 and y1 are position of the target point

        distance = (x1-x)**2 + (y1-y)**2
        distance = math.sqrt(distance)

        return distance

    def setPosition(self, newPosition):
        self.position = newPosition

    def setFuel(self, fuel):
        self.fuel = fuel

    def setSpeed(self,speed):
        self.speed = speed
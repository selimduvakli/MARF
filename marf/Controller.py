#!/usr/bin/env python

######################################################


Vehicles = set()
ControlPoints = set()
Tasks = set()
Map = None


def addToTaskList(task):
    Tasks.add(task)


def remFromTaskList(task):
    Tasks.remove(task)


def remFromVehicleList(vehicle):
    Vehicles.remove(vehicle)


# def remFromTaskList(name):
#     for t in Tasks:
#         if t.name == name:
#             Tasks.remove(t)
#     #maybe raise an error later

def returnPointByName(name):
    for p in ControlPoints:
        if name == p.name:
            return p
    raise Exception('There is no control point that has the given name.')


# def isItUnique(name):
#     if {name}.issubset(Vehicles):
#         return False
#     else:
#         Vehicles.add(name)
#         return True

def NumberOfAsphaltPaver():
    sayac = 0
    for v in Vehicles:
        if v.type == "Asphalt Paver":
            sayac += 1
    return sayac


def NumberOfBulldozer():
    sayac = 0
    for v in Vehicles:
        if v.type == "Bulldozer":
            sayac += 1
    return sayac


def NumberOfCompactor():
    sayac = 0
    for v in Vehicles:
        if v.type == "Compactor":
            sayac += 1
    return sayac


def NumberOfExcavator():
    sayac = 0
    for v in Vehicles:
        if v.type == "Excavator":
            sayac += 1
    return sayac


def NumberOfTruck():
    sayac = 0
    for v in Vehicles:
        if v.type == "Truck":
            sayac += 1
    return sayac


class DummyMap:
    def __init__(self, n, m):
        if (n < 10 or n > 30) or (m < 10 or m > 30):
            raise Exception('Map sizes must be between 10 and 30!')
        self.sizeX = m
        self.sizeY = n
        self.Obstacles = []

    def addObstacle(self, point):
        for obs in self.Obstacles:
            if obs.positionX == point.positionX and obs.positionY == point.positionY:
                return
        for cp in ControlPoints:
            if cp.positionX == point.positionX and cp.positionY == point.positionY:
                raise Exception('There is a Control Point at given position')
        for v in Vehicles:
            if v.startPoint.positionX == point.positionX and v.startPoint.positionY == point.positionY:
                raise Exception('There is a Vehicle at given position')
        self.Obstacles.append(point)

    def deleteObstacle(self, point):
        for obs in self.Obstacles:
            if obs.positionX == point.positionX and obs.positionY == point.positionY:
                self.Obstacles.remove(obs)

    def toJSON(self):
        map = []
        row = []
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                row.append(0)
            map.append(row)
            row = []
        for obs in self.Obstacles:
            map[obs.positionY][obs.positionX] = 1
        return map

    def yaz(self):
        for i in range(self.sizeY):
            print(self.toJSON()[i])
        print()


class NonRepeatableTaskVisitCP:
    def __init__(self, name, priority, controlPoint, startTime, finishTime):
        for t in Tasks:
            if name == t.name:
                raise Exception("This name given to another task.")
        self.name = name
        self.type = "Visiting Control Point"
        self.priority = priority
        self.controlPoint = controlPoint
        self.startTime = startTime
        self.finishTime = finishTime

    def addVehiclesToTask(self, vehicle_list):
        self.vehicles = vehicle_list

    def isRemoveable(self):
        # todo here where we do the check
        return True

    def toJSON(self):
        vehicles = []
        # for v in Vehicles:
        #     if v.type == 'Drone':
        #         vehicles.append(v.toJSON())
        jsn = {
            'name': self.name,
            'type': self.type,
            'priority': self.priority,
            # 'controlPoint' : self.controlPoint.toJSON(),
            'controlPoint': self.controlPoint.name,
            'startTime': self.startTime.__str__(),
            'finishTime': self.finishTime.__str__(),
            # 'vehicles' : self.vehicles
        }
        return jsn


class RepeatableTaskVisitCP(NonRepeatableTaskVisitCP):
    def __init__(self, name, priority, controlPoint, startTime, finishTime, deadline):
        super().__init__(name, priority, controlPoint, startTime, finishTime)
        self.deadline = deadline

    def toJSON(self):
        vehicles = []
        # for v in Vehicles:
        #     if v.type == 'Drone':
        #         vehicles.append(v.toJSON())
        jsn = {
            'name': self.name,
            'type': self.type,
            'priority': self.priority,
            # 'controlPoint' : self.controlPoint.toJSON(),
            'controlPoint': self.controlPoint.name,
            'startTime': self.startTime.__str__(),
            'finishTime': self.finishTime.__str__(),
            'deadline': self.deadline.__str__(),
            # 'vehicles' : self.vehicles
        }
        return jsn


class NonRepeatableTask(NonRepeatableTaskVisitCP):
    def __init__(self, name, type, priority, targetPoint, controlPoint, startTime, finishTime):
        super().__init__(name, priority, controlPoint, startTime, finishTime)
        self.type = type
        self.targetPoint = targetPoint

    def toJSON(self):
        vehicles = []
        # for v in self.vehicles:
        #     vehicles.append(v.toJSON())
        jsn = {
            'name': self.name,
            'type': self.type,
            'priority': self.priority,
            # 'controlPoint' : self.controlPoint.toJSON(),
            'controlPoint': self.controlPoint.name,
            'targetPoint': self.targetPoint.toJSON(),
            'startTime': self.startTime.__str__(),
            'finishTime': self.finishTime.__str__(),
            'vehicles': self.vehicles
        }
        return jsn


class RepeatableTask(RepeatableTaskVisitCP):
    def __init__(self, name, type, priority, targetPoint, controlPoint, startTime, finishTime, deadline):
        super().__init__(name, priority, controlPoint, startTime, finishTime, deadline)
        self.type = type
        self.targetPoint = targetPoint

    def toJSON(self):
        vehicles = []
        # for v in self.vehicles:
        #     vehicles.append(v.toJSON())
        jsn = {
            'name': self.name,
            'type': self.type,
            'priority': self.priority,
            # 'controlPoint' : self.controlPoint.toJSON(),
            'controlPoint': self.controlPoint.name,
            'targetPoint': self.targetPoint.toJSON(),
            'startTime': self.startTime.__str__(),
            'finishTime': self.finishTime.__str__(),
            'deadline': self.deadline.__str__(),
            'vehicles': self.vehicles
        }
        return jsn


class Point:
    def __init__(self, map, posX, posY):
        # change axis names later
        if (posX < 0 or posX >= map.sizeX) or (posY < 0 or posY >= map.sizeY):
            raise Exception('This is not a valid point')
        self.positionX = posX
        self.positionY = posY

    def toJSON(self):
        return [self.positionX, self.positionY]


class ControlPoint(Point):
    def __init__(self, map, posX, posY, name):
        super().__init__(map, posX, posY)
        self.name = name
        if name == '':
            raise Exception("Please enter a name.")
        for cp in ControlPoints:
            if cp.name == name:
                raise Exception("Names must be unique")
            elif cp.positionX == posX and cp.positionY == posY:
                raise Exception("This Control point already exists")
        for obs in map.Obstacles:
            if posX == obs.positionX and posY == obs.positionY:
                raise Exception("There is an obstacle on this point.")
        ControlPoints.add(self)

    def toJSON(self):
        jsn = {
            'name': self.name,
            'coordinates': [self.positionX, self.positionY]
        }
        return jsn


class Vehicle:
    def __init__(self, map, name, type, startPoint, fuelPercentage, speed, powerCapacity):
        for vec in Vehicles:
            if name == vec.name:
                raise Exception('Names must be unique!')
            elif vec.startPoint.positionX == startPoint.positionX and vec.startPoint.positionY == startPoint.positionY:
                raise Exception("There is already an agent on this start point.")
        for obs in map.Obstacles:
            if obs.positionX == startPoint.positionX and obs.positionY == startPoint.positionY:
                raise Exception("There is an obstacle on starting point!")
        self.name = name
        self.type = type
        self.startPoint = startPoint
        self.fuelPercentage = fuelPercentage
        self.speed = speed
        self.powerCapacity = powerCapacity
        Vehicles.add(self)

    def isRemoveable(self):
        if self.type == "Asphalt Paver":
            for t in Tasks:
                if NumberOfAsphaltPaver() - 1 < t.vehicles['Asphalt Paver']:
                    return False
            return True
        elif self.type == "Bulldozer":
            for t in Tasks:
                if NumberOfBulldozer() - 1 < t.vehicles['Bulldozer']:
                    return False
            return True
        elif self.type == "Compactor":
            for t in Tasks:
                if NumberOfCompactor() - 1 < t.vehicles['Compactor']:
                    return False
            return True
        elif self.type == "Excavator":
            for t in Tasks:
                if NumberOfExcavator() - 1 < t.vehicles['Excavator']:
                    return False
            return True
        elif self.type == "Truck":
            for t in Tasks:
                if NumberOfTruck() - 1 < t.vehicles['Truck']:
                    return False
            return True
        else:
            return True

    def toJSON(self):
        jsn = {
            'name': self.name,
            'type': self.type,
            'startPoint': self.startPoint.toJSON(),
            'fuelPercentage': self.fuelPercentage,
            'speed': self.speed,
            'powerCapacity': self.powerCapacity
        }
        return jsn


class Drone:
    def __init__(self, map, name, startPoint, runtmCap, alg):
        for vec in Vehicles:
            if name == vec.name:
                raise Exception('Names must be unique!')
            elif vec.startPoint == startPoint:
                raise Exception("There is already a vehicle on this start point.")
        for obs in map.Obstacles:
            if obs.positionX == startPoint.positionX and obs.positionY == startPoint.positionY:
                raise Exception("There is an obstacle on starting point!")
        self.name = name
        self.type = "Drone"
        self.startPoint = startPoint
        self.runtimeCapacity = runtmCap
        self.algorithm = alg
        Vehicles.add(self)

    def isRemoveable(self):
        if len(Tasks) > 0:
            return False
        else:
            return True

    def toJSON(self):
        jsn = {
            'name': self.name,
            'type': self.type,
            'startPoint': self.startPoint.toJSON(),
            'runtimeCapacity': self.runtimeCapacity,
            'algorithm': self.algorithm
        }
        return jsn

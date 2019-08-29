from datetime import datetime
import random
from random import shuffle
import sys
import math
import time as TIME
import requests
import json

from ControlPoint import ControlPoint
from TaskType import TaskType
from Vehicle import Vehicle
from Task import Task


class System:

    def __init__(self):
        self.mapSizes = [0, 0, 0, 0]  # first element : x lowest, second : y lowest, third : x highest, fourth : y highest
        self.vehicles = []
        self.controlPoints = []
        self.tasks = []
        self.map = [[]]
        self.vehicleTypes = {"Excavator": 0, "Drone": 0, "Truck": 0, "Bulldozer": 0, "Asphalt Paver": 0,
                             "Compactor": 0}
        self.tasksForDrone = []
        self.completedTasks = []
        self.startingTimes = []
        self.visitedControlPoint = []
        self.URL = "http://127.0.0.1:5000/"
        self.ID = "0"

    def register(self):
        url = self.URL + "publisher"
        data = {"name": "task_manager", "topics": ["visiting", "MAS", "Task2UI"]}
        r1 = requests.post(url, json=data)
        print(r1.text)

        data = {"name": "task_manager", "topics": ["visitingResponse", "MAR", "UI2Task"]}
        url = self.URL + "subscriber"
        r2 = requests.post(url, json=data)
        print(r2.text)

    def send(self,topicName, message):
        data = {"topic_name": topicName, "data": {"taskDetails": message}}
        url = self.URL + "publish"
        r3 = requests.post(url, json=data)
        print(r3.text)

    def receive(self,topicName):
        url = self.URL + "publish/" + self.ID
        r4 = requests.get(url)
        x = r4.text
        y = json.loads(x)
        if len(y.values()) == 0:
            return "no data"
        y = y[topicName]["data"]["taskDetails"]
        return y

    # ---------------------------------------------------------------------------#
    # ---------------------------------------------------------------------------#
    def getDatafromUI(self):
        url = self.URL + "publish/" + self.ID
        r5 = requests.get(url)
        #       print(r4.text)
        a = r5.text
        b = json.loads(a)
        if len(b.values()) == 0:
            return "no data"
        Data = b['UI2Task']["data"]
        return Data
    #---------------------------------------------------------------------------#
    # ---------------------------------------------------------------------------#
    def setMap(self, mapSizes, map):
        # mapSizes list is consist of 4 elements, [x lowest, y lowest, x highest, y highest]
        # x : horizontal axis, y: vertical axis
        self.mapSizes = mapSizes
        self.map = map

    # this method controls the uniuqe name for the given list( list can be control points, vehicles and tasks)
    def isNameUnique(self, name, list):
        i = 0
        size = len(list)

        while i < size and name != list[i].name:
            i += 1

        if i < size:
            return False
        else:
            return True

    # this method controls the coordinate values for control points
    def isCoordinateValidForControlPoint(self, x, y):

        if x >= self.mapSizes[0] and y >= self.mapSizes[1]:  # map[0] = lowest x, map[1] =lowest y
            if x <= self.mapSizes[2] and y <= self.mapSizes[3]:  # map[2] = highest x, highest y
                if self.map[x][y] != 1:  # if there is not obstacle at this point
                    i = 0
                    size = len(self.controlPoints)
                    # we have to check, is there any control point at this coordinate
                    while i < size and (
                            self.controlPoints[i].coordinates[0] != x or self.controlPoints[i].coordinates[1] != y):
                        i += 1
                    if i >= size:
                        return True
                    else:
                        print("There is another control point with the same coordinate")
                else:
                    print("There is an obstacle in this coordinates")
        else:
            print("invalid coordinate")
        return False

    # This method add new control point to the system
    def addControlPoint(self, controlPoint):
        if self.isNameUnique(controlPoint.name, self.controlPoints):  # Control Point name shall be unique at the system
            if self.isCoordinateValidForControlPoint(controlPoint.coordinates[0], controlPoint.coordinates[1]):
                self.controlPoints.append(controlPoint)
                print(controlPoint.name, " : The new Control point is added")
                return True
        else:
            print(controlPoint.name, " : There is already a control point with the same name")
        return False

    def showControlPoints(self):
        for i in self.controlPoints:
            print(i.name, i.coordinates)

    # This method controls the coordinate values for the vehicle
    def isCoordinateValidForVehicle(self, x, y):

        if x >= self.mapSizes[0] and y >= self.mapSizes[1]:  # map[0] = lowest x, map[1] =lowest y
            if x <= self.mapSizes[2] and y <= self.mapSizes[3]:  # map[2] = highest x, highest y
                if self.map[x][y] != 1:  # is there obstacle at this point
                    i = 0
                    size = len(self.vehicles)
                    while i < size and (
                            self.vehicles[i].position[0] != x or self.vehicles[i].position[1] != y):
                        i += 1
                    if i >= size:
                        return True
                    else:
                        print("There is another vehicle at this coordinate")
                else:
                    print("There is an obstacle in this coordinate")
        else:
            print("Invalid Coordinate")
        return False

    # This method adds new vehicle to the system
    # The vehicle parameter is the vehicle Object
    def addVehicle(self, vehicle):  #
        if self.isNameUnique(vehicle.name, self.vehicles):  # Every vehicle shall have the unique name at the system
            if self.isCoordinateValidForVehicle(vehicle.position[0], vehicle.position[1]):
                if vehicle.isItDrone():
                    # The system shall have only one drone
                    if self.vehicleTypes["Drone"] == 0:
                        self.vehicles.append(vehicle)
                        self.vehicleTypes[vehicle.vehicleType] += 1
                        print(vehicle.name, " : The new vehicle is added")
                    else:
                        print("The system shall have only one drone")
                else:
                    self.vehicles.append(vehicle)
                    self.vehicleTypes[vehicle.vehicleType] += 1
                    print(vehicle.name, " : The new vehicle is added")
                return True
        else:
            print("There is already a vehicle with the same name")
        return False

    def showVehicles(self):
        for i in self.vehicles:
            print(i.name)

    # This method returns the index of element from the list
    # List can be tasks, vehicles and control points
    def searchWithName(self, name, list):

        i = 0
        size = len(list)

        while i < size and name != list[i].name:
            i += 1

        if i >= size:  # if the list doesn't include this element, the function returns -1
            return -1
        else:
            return i

    # This method deletes the vehicles according to vehicleName
    def deleteVehicle(self, vehicleName):
        index = self.searchWithName(vehicleName, self.vehicles)
        if index != False:
            # If this vehicle has a task, firstly we have to wait until task will be completed
            while self.vehicles[index].task != None:
                pass
            self.vehicles.remove(self.vehicles[index])
            print(vehicleName, " is deleted")
        return

    # This method adds new task to the system
    def addTask(self, task):
        x = task.targetPosition[0]  # horizontal axis
        y = task.targetPosition[1]  # vertical axis
        # Each task shall an unique name at the system
        if self.isNameUnique(task.name, self.tasks):
            if x >= self.mapSizes[0] and y >= self.mapSizes[1]:  # map[0] = lowest x, map[1] =lowest y
                if x <= self.mapSizes[2] and y <= self.mapSizes[3]:  # map[2] = highest x, highest y
                    if task.taskType.name == "Visit The Control Point":
                        # The system shall have only one drone at the same time
                        self.tasksForDrone.append(task)
                    else:
                        # the number of necessary vehicles for this task can't be bigger than the number of vehicles at the system
                        k = 0
                        flag = 0
                        for key in self.vehicleTypes.keys():
                            if (self.vehicleTypes[key] < task.numberOfNecessaryVehicle[k]):
                                flag = 1
                            k += 1
                        if flag == 0:
                            self.tasks.append(task)
                            task.plan = self.createPlan(task)
                            print(task.name, " : Task is added")
                            return True
                        else:
                            print("There is not enough vehicle for this task")
                else:
                    print("Invalid coordinate")
            else:
                print("Invalid coordinate")
        else:
            print("There is already task with the same name")
        return False

    # This method deletes the task according to given task name
    def deleteTask(self, taskName):

        index = self.searchWithName(taskName, self.tasks)

        if index == -1:  # the task is not on the tasks list
            # it may be drone task
            index = self.searchWithName(taskName, self.tasksForDrone)
            if index == -1:  # there is not task with this name
                return
            task = self.tasksForDrone[index]
            isItForDrone = True
        else:
            task = self.tasks[index]
            isItForDrone = False

        while task.situation == "in Progress":
            pass
        # we should release the vehicles
        self.releaseVehicle(task)

        if isItForDrone == True:
            self.tasksForDrone.remove(task)
        else:
            self.tasks.remove(task)

    # This methods release the vehicles which allocated to the given task
    def releaseVehicle(self, task):

        vehicles = self.returnVehiclesForThisTask(task)

        if vehicles != None:
            for i in vehicles:
                if i.task.situation == "completed" or i.task.situation == "not completed":
                    self.vehicleTypes[i.vehicleType] += 1
                    i.setFree()
            print(task.name + " bittikten sonraki arac durumu:---> ")
            print("--------")
            for i in self.vehicleTypes.keys():
                print(i, self.vehicleTypes[i])
            print("---------")

    # This method shows the task details
    def listTasks(self):
        print("Name priority situation type")
        for i in self.tasksForDrone:
            print(i.name + " : " + i.priority + " -" + i.situation + " - " + i.taskType.name)
        for i in self.tasks:
            print(i.name + " : " + i.priority + " -" + i.situation + " - " + i.taskType.name)

    # This method creates a plan for the given task considering by task type
    def createPlan(self, task):
        plan = []
        step1 = " It is plan for " + task.name
        step2 = " Go to " + str(task.targetPosition[0]) + " " + str(task.targetPosition[1])
        step3 = " "
        for i in task.taskType.stepOfPlan:
            step3 += i
        plan.append(step1)
        plan.append(step2)
        plan.append(step3)
        task.plan = plan

        return plan

    def preprocessData(self, name,isForScheduling):
        if isForScheduling == True:
            preprocessing = {"High": 7, "Medium": 5, "Low": 3}
        else:
            preprocessing = {"Weak": 1, "Medium": 3, "Strong": 5}

        return preprocessing[name]

    # This method returns the task list considering by given features
    def takeTask(self, time, isItForDrone, ControlPoint=None):
        # Time format is the hour and minute
        # Type of isItForDrone parameter is the boolean
        # ControlPoint can be list of the Control Points
        resultList = []
        if isItForDrone == True and ControlPoint == None:
            taskList = self.tasksForDrone
        else:
            taskList = []
            for i in ControlPoint:
                for j in self.tasks:
                    if j.controlPoint == i:
                        taskList.append(j)

        for i in taskList:
            if i.timePeriod[0] == time:
                resultList.append(i)

        if (len(resultList) == 0):
            return False
        return resultList

    # This method schedules tasks according to their features
    # In this method, genetic algorithm is used when scheduling
    def scheduleTasks(self, time, isItForDrone, ControlPoint=None):

        taskList = self.takeTask(time, isItForDrone, ControlPoint)

        if taskList == False:
            return -1, -1

        population = []
        populationSize = 100

        max = sys.maxsize
        minPoint = max

        # We create the initial population
        for i in range(populationSize):
            shuffle(taskList)
            point = self.fitnessOfScheduling(taskList)
            newPerson = [list(taskList), int(point)]

            population.append(newPerson)
            if minPoint > newPerson[1]:
                minPoint = newPerson[1]
                result = newPerson[0].copy()

        # We create the new generations from the old population
        k = 0
        while k < 200:
            k += 1
            m = 0
            newPopulation = []
            # We create 80 children from the old population
            while m < 80:
                m += 1
                parent1 = self.selection(population, True)
                parent2 = self.selection(population, True)
                child = self.crossOver(parent1, parent2)
                # Mutation is important to provide the diversity
                probability = random.randint(0, 100)
                if probability < 15:
                    child = self.mutation(child)
                child[1] = self.fitnessOfScheduling(child[0])
                newPopulation.append(child)
                # We append new child to the population
                if minPoint > child[1]:
                    minPoint = child[1]
                    result = child[0].copy()
            # May be the best solution of the problem is belong to the old population
            # We take 20 members of the old population to add new population
            oldBest = self.findOldBestState(population)
            population = newPopulation.copy()
            # we append 20 indivuals  which have better points than other, from old population, to the new population
            for i in oldBest:
                population.append(i)
        # Result is list of tasks, minPoint is the fitness point of this result
        return result, minPoint

    # this method finds the individuals which have better points, returns the list of them
    def findOldBestState(self, population1):
        population = population1.copy()
        resultlist = []

        for i in range(20):
            individual = self.findMinPoint(population)
            resultlist.append(individual)
            population.remove(individual)

        return resultlist

    # this method finds the element of the population which has the best point
    def findMinPoint(self, population):
        i = 1
        resultIndex = 0
        min = population[0][1]
        while i < len(population):
            if min > population[i][1]:
                min = population[i][1]
                resultIndex = i
            i += 1
        return population[resultIndex]

    # this method calculates the required time for the task to be started
    def calculateWaitingTime(self, task, taskList):

        time = 0
        i = 0
        while task.name != taskList[i].name:
            # Each task should wait to upper task which has the same task type
            if taskList[i].taskType.name == task.taskType.name:
                time = time + int(taskList[i].calculateTimeToBeDone())
            i = i + 1

        return time

    # this method calculates the fitness point for the scheduling
    def fitnessOfScheduling(self, personOfPopulation):

        taskList = personOfPopulation.copy()

        numberOfWaitingTasks = 0
        flag = {"Visit The Control Point": 0, "Excavation": 0, "Pit Filling": 0, "Pouring Asphalt": 0}
        point = 0
        vehicleNumberForEachType = list(self.vehicleTypes.values()).copy()
        for i in range(len(taskList)):
            k = 0
            numberOfVehicleForThisTask = taskList[i].numberOfNecessaryVehicle.copy()
            # there are six vehicle types at the system
            while k < 6:
                vehicleNumberForEachType[k] = vehicleNumberForEachType[k] - numberOfVehicleForThisTask[k]
                if vehicleNumberForEachType[k] < 0:
                    vehicleNumberForEachType[k] = 0
                    flag[taskList[
                        i].taskType.name] = 1  # The tasks which have this task type, shall wait until upper task will be completed
                k += 1
            if flag[taskList[i].taskType.name] == 1:
                point += self.preprocessData(taskList[i].priority,True) * self.calculateWaitingTime(taskList[i], taskList)
                numberOfWaitingTasks += 1
        point = point + numberOfWaitingTasks * 100
        return point

    # This method choices a person from the population considering by fitness points and probability
    def selection(self, population, isForScheduling):

        if isForScheduling == True:
            k = 5000
        else:
            k = 50

        sum = 0
        for i in population:
            sum += (k - i[1])
        rel = []
        for i in population:
            relative_fitness = float(i[1] / sum)
            rel.append(relative_fitness)
        probs = []
        sumRel = 0
        for i in rel:
            sumRel = sumRel + i
            pr = sumRel
            probs.append(pr)
        r = random.uniform(0, 1)
        flag = 0
        i = 0
        parent = 0
        while i < len(probs) and flag == 0:
            if (r <= probs[i]):
                flag = 1
                parent = i
            i += 1
        return population[parent]

    # this method produce a child from his parents
    def crossOver(self, parent1, parent2):
        size = len(parent1[0])
        number = random.randint(1,size)
        randomList = []
        for i in range(size):
            randomList.append(-1)

        i = 0
        # Firstly, we add random number of elements from parent1 to the child
        while i < number:
            randomElementFromParent1 = random.randint(0, (size - 1))
            if randomList[randomElementFromParent1] == -1:
                if self.searchInTheList(parent1[0][randomElementFromParent1], randomList) != True:
                    randomList[randomElementFromParent1] = parent1[0][randomElementFromParent1]
                    i += 1
        # Then we take number of necessary elements from parent2, and add them to the child
        for i in parent2[0]:
            j = 0
            if self.searchInTheList(i, randomList) != True:
                while j < size and randomList[j] != -1:
                    j += 1
                if j < size:
                    randomList[j] = i
        child = [randomList.copy(), 0]

        return child

    # it swaps position of the two elements at the person
    def mutation(self, person):
        size = len(person[0])

        x = random.randint(0, (size - 1))
        y = random.randint(0, (size - 1))

        tmp = person[0][x]
        person[0][x] = person[0][y]
        person[0][y] = tmp

        return person

    # This method search value in the list and return type is the boolean
    def searchInTheList(self, value, list):
        i = 0
        while i < len(list) and list[i] != value:
            i += 1
        if i < len(list):
            return True
        else:
            return False

    # This method returns list of suitable vehicles according to the given vehicle type
    def takeVehiclesAccordingToVehicleType(self, vehicleType):
        vehicles = []
        for i in self.vehicles:
            if i.vehicleType == vehicleType and i.task == None:
                vehicles.append(i)
        return vehicles

    def indexOfVehicleType(self, vehicleName):
        index = 0
        vehicleListOfTheSystem = list(self.vehicleTypes.keys()).copy()
        while index < 6 and vehicleListOfTheSystem[index] != vehicleName:
            index += 1
        return index

    # This method allocates the given tasks to the suitable vehicles
    # The genetic algorithm is used when allocation of the task
    def allocateTask(self, taskList):
        flags = {"Excavator": 0, "Drone": 0, "Truck": 0, "Bulldozer": 0, "Asphalt Paver": 0, "Compactor": 0}
        p = 0

        while p < len(taskList):
            vehiclesTypesForThisTaskType = taskList[p].taskType.necessaryVehicleTypes.copy()
            p += 1

            for i in vehiclesTypesForThisTaskType:
                if flags[i] == 0:
                    flags[i] = 1

                    max = sys.maxsize
                    minPoint = max

                    vehicles = self.takeVehiclesAccordingToVehicleType(i)
                    sum = 0
                    index = self.indexOfVehicleType(i)
                    for j in taskList:
                        sum += j.numberOfNecessaryVehicle[index]

                    population = []
                    populationSize = 100

                    # let's create the initial population
                    for k in range(populationSize):
                        vehicleList = random.sample(vehicles, sum)
                        individual = [vehicleList, 0]
                        individual[1] = self.fitnessForAllocation(taskList, individual, index)
                        population.append(individual)
                        if minPoint > individual[1]:
                            minPoint = individual[1]
                            result = individual[0].copy()

                    # we created the initial population
                    for m in range(100):
                        newPopulation = []
                        k = 0
                        while k < 80:
                            parent1 = self.selection(population, False)
                            parent2 = self.selection(population, False)
                            child = self.crossOver(parent1, parent2)
                            # Mutation is important for population diversity
                            probability = random.randint(0, 100)
                            if probability < 5:
                                child = self.mutation(child)
                            child[1] = self.fitnessForAllocation(taskList, child, index)
                            newPopulation.append(child)

                            if minPoint > child[1]:
                                minPoint = child[1]
                                result = child[0].copy()

                            k += 1
                        # May be the best solution of the problem is belong to the old population
                        oldBest = self.findOldBestState(population)
                        population = newPopulation.copy()
                        for k in oldBest:
                            population.append(k)
                    l = 0
                    for k in taskList:
                        t = 0
                        print(k.name + " adli goreve arac tahsis edelim")
                        print("-----------")
                        k.setSituation("in Progress")
                        while l < len(result) and t < k.numberOfNecessaryVehicle[index]:
                            t += 1
                            result[l].setTask(k)
                            print("bu goreve " + result[l].name + " araci tahsis edildi")
                            l += 1

    # This method calculates the fitness point for the given individual
    def fitnessForAllocation(self, taskList, individual, index):
        vehicles = individual[0].copy()
        k = 0
        point = 0
        for task in taskList:
            toFinal = task.numberOfNecessaryVehicle[index]
            timeForJob = (self.preprocessData("Medium",False) * toFinal)
            while k < toFinal:
                x = (vehicles[k].position[0] - task.targetPosition[0]) ** 2
                y = (vehicles[k].position[1] - task.targetPosition[1]) ** 2
                distance = x + y
                distance = math.sqrt(distance)
                time = timeForJob / self.preprocessData(vehicles[k].powerCapacity,False)
                point += distance / vehicles[k].speed + time
                k += 1
        return point

    # This method trig the task allocation method
    def trigTheAllocationOfTask(self, res):
        # res parameter is the result of the scheduling
        allocatedTasks = self.listTheTasksToBeDoneAtNow(res)
        print("allocate edilen tasklar:")
        print("-----------")
        if len(allocatedTasks) > 0:
            for i in allocatedTasks:
                print(i.name)
            self.allocateTask(allocatedTasks)  # in here we started to allocation of task
            for i in allocatedTasks:
                j = 0
                for key in self.vehicleTypes.keys():
                    self.vehicleTypes[key] -= i.numberOfNecessaryVehicle[j]
                    j += 1
            print("------------")
            print("atamalar sonucu sistemdeki arac sayilari:")
            for key in self.vehicleTypes.keys():
                print(key, self.vehicleTypes[key])

            print("-----------")

            for i in self.vehicles:
                if i.task != None:
                    print(i.name + " adli araca " + i.task.name + " gorevi atanmistir")
            print("-----------")

    # this method returns the list of vehicles which will accomplish this task
    def returnVehiclesForThisTask(self, task):
        myVehicles = []
        print(self.vehicles)
        for i in self.vehicles:

            if i.task ==task:
                myVehicles.append(i)
                print(myVehicles)
        return myVehicles

    # this method returns the list of tasks according to result of the task scheduling
    def listTheTasksToBeDoneAtNow(self, res):
        # res parameter is the result of the scheduling
        taskList = res.copy()
        allocatedTasks = []
        vehicleNumberForEachType = list(self.vehicleTypes.values()).copy()
        flag = {"Visit The Control Point": 0, "Excavation": 0, "Pit Filling": 0, "Pouring Asphalt": 0}
        for i in range(len(taskList)):
            k = 0
            if taskList[i].situation == "not started":
                numberOfVehicleForThisTask = taskList[i].numberOfNecessaryVehicle.copy()
                # there are six vehicle types at the system
                while k < 6:
                    vehicleNumberForEachType[k] = vehicleNumberForEachType[k] - numberOfVehicleForThisTask[k]
                    if vehicleNumberForEachType[k] < 0:
                        vehicleNumberForEachType[k] = 0
                        flag[taskList[i].taskType.name] = 1
                    k += 1
                if flag[taskList[i].taskType.name] == 0:
                    allocatedTasks.append(taskList[i])
        return allocatedTasks

    # It provides to take starting time of all tasks without duplication
    def createStartingTimeList(self):
        for i in self.tasksForDrone:
            if self.searchInTheList(i.timePeriod[0], self.startingTimes) == False:
                self.startingTimes.append(i.timePeriod[0])
        for i in self.tasks:
            if self.searchInTheList(i.timePeriod[0], self.startingTimes) == False:
                self.startingTimes.append(i.timePeriod[0])
        self.startingTimes.sort()
        return

    # This method clean the given list
    def cleanTheList(self, list):
        list.clear()
        return

    # This method make visited when drone went the given control point
    def doVisitedControlPoint(self, controlPoint):
        if self.searchInTheList(controlPoint, self.visitedControlPoint) == False:
            self.visitedControlPoint.append(controlPoint)
        return

    # When the start signal came from UI, the this method should run
    def run(self):
        # Firstly we have to run this method !!!

        self.createStartingTimeList()

        for time in self.startingTimes:
            resForDrone, point = self.scheduleTasks(time, isItForDrone=True)
            time1 = time.strftime("%H %M")
            if resForDrone != -1:
                print("--------------------------")
                print("Result of Scheduling For Drone At " + str(time1) + ":")
                print("--------------------------")

                for i in resForDrone:
                    print(i.name, i.priority, i.numberOfNecessaryVehicle, i.calculateTimeToBeDone())

                print("Point = ", point)

                self.trigTheAllocationOfTask(resForDrone)  # lets start the allocation

                taskList = resForDrone.copy()
                i = 0
                flag = 0
                # to Run the tasks
                while i < len(taskList):
                    # send this task to the drone path planner by MultiAgent Communication
                    situation = taskList[i].situation
                    necessaryVehicles = self.returnVehiclesForThisTask(taskList[i])
                    print(len(necessaryVehicles))
                    print(taskList[i].name)
                    print(necessaryVehicles)
                    data = [necessaryVehicles[0].position, taskList[i].targetPosition]
                    self.send("visiting", data)
                    while situation == "in Progress" or situation == "no data":
                        situation = self.receive("visitingResponse")
                        print(situation)
                    taskList[i].situation = situation
                    if taskList[i].situation == "completed":
                        self.doVisitedControlPoint(taskList[i].controlPoint)
                        self.completedTasks.append(taskList[i])
                        for j in necessaryVehicles:
                            j.position = taskList[i].targetPosition
                        for j in taskList[i].taskType.stepOfPlan:
                            print(" ---"+j+"is completed")
                            self.send("Task2UI", " ---"+j+" is completed")
                    self.releaseVehicle(taskList[i])
                    print(taskList[i].name, taskList[i].situation)
                    if type(taskList[i].name) == str:
                        print(taskList[i].name + " is " + taskList[i].situation)
                    # if taskList[i].isItRepeatable() == False:
                    # self.deleteTask(taskList[i].name)
                    # elif taskList[i].deadline < NOW:
                    # self.deleteTask(taskList[i].name)
                    i = (i + 1)
                    self.trigTheAllocationOfTask(taskList.copy())

            # let s schedule the agent's task
            res, point = self.scheduleTasks(time, isItForDrone=False, ControlPoint=self.visitedControlPoint)
            if res != -1:
                print("--------------------------")
                print("Result of Scheduling For Agents At " + str(time1) + ":")
                print("--------------------------")

                for i in res:
                    print(i.name, i.priority, i.numberOfNecessaryVehicle, i.calculateTimeToBeDone(),
                          i.controlPoint.name)

                print("Point = ", point)

                self.trigTheAllocationOfTask(res)

                # to Run the tasks
                taskList = res.copy()
                i = 0
                flag = 0
                while i < len(taskList):
                    # send this data to AI path planner with MultiAgent Communication
                    necessaryVehicles = self.returnVehiclesForThisTask(taskList[i])
                    startPositions = []
                    for j in necessaryVehicles:
                        startPositions.append(j.position)
                    data = []
                    data.append(startPositions)
                    data.append(taskList[i].targetPosition)
                    self.send("MAS", data)
                    situation = taskList[i].situation
                    counter = 0
                    while situation == "in Progress" or situation == "no data":
                        situation = self.receive("MAR")
                        if counter % 100 == 0:
                            print(situation)
                        counter = counter + 1
                    taskList[i].situation = situation
                    if taskList[i].situation == "completed":
                        self.completedTasks.append(taskList[i])
                        for j in necessaryVehicles:
                            j.position = taskList[i].targetPosition
                        for j in taskList[i].taskType.stepOfPlan:
                            print(" ---"+j+"is completed")
                            self.send("Task2UI", " ---"+j+" is completed")
                    self.releaseVehicle(taskList[i])
                    if type(taskList[i].name) == str:
                        print(taskList[i].name + " is " + taskList[i].situation)
                    # if taskList[i].isItRepeatable() == False:
                    #   self.deleteTask(taskList[i].name)
                    # elif taskList[i].deadline < NOW:
                    #   self.deleteTask(taskList[i].name)
                    i = (i + 1)
                    self.trigTheAllocationOfTask(taskList.copy())

        # We have to clean the starting times when all task will be completed!!!
        self.cleanTheList(self.startingTimes)

system = System()

# We should register to communication system
system.register()

#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
result="no data"
#result={'Map': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 'Tasks': [{'controlPoint': 'A', 'deadline': '2019-01-01', 'finishTime': '02:00:00', 'name': 'ER', 'priority': 'Medium', 'startTime': '01:00:00', 'targetPoint': [2, 7], 'type': 'Excavation', 'vehicles': {'Asphalt Paver': 0, 'Bulldozer': 0, 'Compactor': 0, 'Excavator': 1, 'Truck': 0}}, {'controlPoint': 'A', 'deadline': '2019-01-01', 'finishTime': '04:00:00', 'name': 'V', 'priority': 'Medium', 'startTime': '00:03:00', 'type': 'Visiting Control Point'}], 'Vehicles': [{'fuelPercentage': 25, 'name': 'E', 'powerCapacity': 'weak', 'speed': 4, 'startPoint': [3, 3], 'type': 'Excavator'}, {'algorithm': 'A*', 'name': 'D', 'runtimeCapacity': 100, 'startPoint': [4, 5], 'type': 'Drone'}], 'controlPoints': [{'coordinates': [1, 2], 'name': 'A'}]}
#result={'Map': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 'Vehicles': [{'name': 'llklk', 'type': 'Drone', 'startPoint': [1, 1], 'runtimeCapacity': 6, 'algorithm': 'A*'}, {'name': 'ppp', 'type': 'Excavator', 'startPoint': [2, 2], 'fuelPercentage': 25, 'speed': 1, 'powerCapacity': 'medium'}], 'Tasks': [{'name': 'Visit the Control POint', 'type': 'Visiting Control Point', 'priority': 'Low', 'controlPoint': 'lkllkkk', 'startTime': '01:00:00', 'finishTime': '03:00:00', 'deadline': '2019-01-01'}], 'controlPoints': [{'name': 'lkllkkk', 'coordinates': [6, 6]}]}
while result == "no data":
    result = system.getDatafromUI()
print(result)

Map=result['Map']

Mapsize=[0,0,len(Map[0]),len(Map)]

system.setMap(Mapsize,Map)
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

"""  
#We should take the map by Communication System
#  result = [[0,0,30,30],[0,1,1,1,1,...]]
result = system.receive("visitingResponse")
result = system.receive("visitingResponse")

while result == "no data":
    result = system.receive("visitingResponse")

print(result[0])
print(result[1])
system.setMap(result[0], result[1])
"""


# EMBEDDED-->
#---------------------------------------------------------------------------#
taskType1 = TaskType("Visit The Control Point", ["Drone"], ["Take task information"])
taskType2 = TaskType("Excavation", ["Excavator"], ["Excavate"])
taskType3 = TaskType("Pit Filling", ["Truck", "Bulldozer"],
                     ["Bulldozer load the soil to truck", "Truck pours the soil to pit"])
taskType4 = TaskType("Pouring Asphalt", ["Asphalt Paver", "Compactor"],
                     ["Asphalt pavers pours asphalt", "Compactor compact the asphalt"])
#--------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
def createControlPoint(ControlPoints):
   for x in ControlPoints:
        y=ControlPoint(x['name'], x['coordinates'])
        system.addControlPoint(y)

def returnPointbyName(pointName):
    for x in system.controlPoints:
        if(x.name==pointName):
            return x
    return None
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
''' 
 controlPoint1 = ControlPoint("ControlPoint1", [2, 1])
controlPoint2 = ControlPoint("ControlPoint2", [1, 1])
controlPoint3 = ControlPoint("ControlPoint3", [15, 15])
#CONTROLPOINTS= system.receive("UI2Task")
#for each CONTROLPOINTS:
#    system.addControlPoint(each)


system.addControlPoint(controlPoint1)
system.addControlPoint(controlPoint2)
system.addControlPoint(controlPoint3)

 '''
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
def createVehicles(Vehicles):
    Vhcls=[]
    for x in Vehicles:
        if x["type"] != "Drone":
            y=Vehicle(x['name'],x['type'],x['speed'],x['fuelPercentage'],x['powerCapacity'],x['startPoint'])
        else:
            y=Vehicle(x['name'], "Drone", 3, x['runtimeCapacity'], "Strong", x['startPoint'])
        Vhcls.append(y)
        system.addVehicle(y)
    return Vhcls
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
''' 
vehicle = Vehicle("excavator1", "Excavator", 3, 100, "Weak", [1, 1])
vehicle1 = Vehicle("excavator2", "Excavator", 3, 100, "Strong", [1, 2])
vehicle2 = Vehicle("excavator3", "Excavator", 3, 100, "Strong", [1, 3])
vehicle3 = Vehicle("excavator4", "Excavator", 3, 100, "Medium", [2, 1])
vehicle4 = Vehicle("truck1", "Truck", 3, 100, "Strong", [2, 0])
vehicle5 = Vehicle("truck2", "Truck", 3, 100, "Weak", [7, 7])
vehicle6 = Vehicle("Drone", "Drone", 3, 100, "Strong", [2, 4])
vehicle7 = Vehicle("Bulldozer1", "Bulldozer", 3, 100, "Strong", [4, 2])
vehicle8 = Vehicle("Asphalt Pavers1", "Asphalt Paver", 3, 100, "Strong", [5, 2])
vehicle9 = Vehicle("Compactor1", "Compactor", 3, 100, "Strong", [7, 2])
vehicle10 = Vehicle("excavator5", "Excavator", 3, 100, "Weak", [7, 1])
vehicle11 = Vehicle("excavator6", "Excavator", 3, 100, "Strong", [2, 6])
vehicle12 = Vehicle("excavator7", "Excavator", 3, 100, "Weak", [2, 5])
vehicle13 = Vehicle("Bulldozer2", "Bulldozer", 3, 100, "Strong", [5, 3])
vehicle14 = Vehicle("Truck3", "Truck", 3, 100, "Weak", [7, 4])


system.addVehicle(vehicle)
system.addVehicle(vehicle1)
system.addVehicle(vehicle2)
system.addVehicle(vehicle3)
system.addVehicle(vehicle4)
system.addVehicle(vehicle5)
system.addVehicle(vehicle6)
system.addVehicle(vehicle7)
system.addVehicle(vehicle8)
system.addVehicle(vehicle9)
system.addVehicle(vehicle10)
system.addVehicle(vehicle11)
system.addVehicle(vehicle12)
system.addVehicle(vehicle13)
system.addVehicle(vehicle14)

'''

system.showControlPoints()
system.showVehicles()

date_format = "%H:%M"
start_time = datetime.strptime("11:00", date_format)
end_time = datetime.strptime("11:30", date_format)

start_time1 = datetime.strptime("11:00", date_format)
end_time1 = datetime.strptime("11:40", date_format)

start_time8 = datetime.strptime("11:00", date_format)
end_time8 = datetime.strptime("11:01", date_format)

start_time2 = datetime.strptime("13:00", date_format)
end_time2 = datetime.strptime("13:15", date_format)

start_time3 = datetime.strptime("12:00", date_format)
end_time3 = datetime.strptime("12:20", date_format)

# ["Excavator","Drone","Truck","Bulldozer","Asphalt Pavers","Compactor"]
numOfVehicleForEachType1 = [2, 0, 0, 0, 0, 0]  # task type 2

numOfVehicleForEachType2 = [0, 0, 1, 1, 0, 0]  # task type 3

numOfVehicleForEachType3 = [3, 0, 0, 0, 0, 0]  # task type 2

numOfVehicleForEachType4 = [0, 0, 0, 0, 1, 1]  # task type 4

numOfVehicleForEachType5 = [0, 1, 0, 0, 0, 0]  # task type 1

numOfVehicleForEachType6 = [0, 1, 0, 0, 0, 0]  # task type 1
numOfVehicleForEachType7 = [0, 1, 0, 0, 0, 0]  # task type 1

#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
def createTask(Tasks):
    for x in Tasks:
        try:
            if(x['type']=='Visiting Control Point'):
                deadline = x["deadline"]
                controlPoint = returnPointbyName(x['controlPoint'])
                numberOfNecessaryVehicle = [0, 1, 0, 0, 0, 0]
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                numberOfNecessaryVehicle = [0, 1, 0, 0, 0, 0]
                print(controlPoint)
                y=Task(x['name'], x['priority'], taskType1, True, controlPoint.coordinates, deadline,
                       controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            elif x['type']=="Excavation":
                deadline = x["deadline"]
                controlPoint = returnPointbyName(x['controlPoint'])
                numberOfNecessaryVehicle = []
                # ["Excavator","Drone","Truck","Bulldozer","Asphalt Pavers","Compactor"]
                numberOfNecessaryVehicle = [0, 0, 0, 0, 0, 0]
                numberOfNecessaryVehicle[0] = x["vehicles"]['Excavator']
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                y = Task(x['name'], x['priority'], taskType2, True, x['targetPoint'], deadline,
                         controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            elif x['type']=="Pit Filling":
                deadline = x["deadline"]
                controlPoint = returnPointbyName(x['controlPoint'])
                numberOfNecessaryVehicle = [0, 0, 0, 0, 0, 0]
                numberOfNecessaryVehicle[2] = x["vehicles"]['Truck']
                numberOfNecessaryVehicle[3] = x["vehicles"]['Bulldozer']
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                y = Task(x['name'], x['priority'], taskType3, True, x['targetPoint'], deadline,
                         controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            elif x['type']=="Pouring Asphalt":
                deadline = x["deadline"]
                controlPoint = returnPointbyName(x['controlPoint'])
                numberOfNecessaryVehicle = [0, 0, 0, 0, 0, 0]
                numberOfNecessaryVehicle[4] = x["vehicles"]['Asphalt Paver']
                numberOfNecessaryVehicle[5] = x["vehicles"]['Compactor']
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                y = Task(x['name'], x['priority'], taskType4, True, x['targetPoint'], deadline,
                         controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            else: return None
        except KeyError:
            if (x['type'] == 'Visiting Control Point'):
                controlPoint = returnPointbyName(x['controlPoint'])
                numberOfNecessaryVehicle = [0, 1, 0, 0, 0, 0]
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                y = Task(x['name'], x['priority'], taskType1, False, controlPoint.coordinates, 5,
                         controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            elif x['type'] == "Excavation":
                controlPoint = returnPointbyName(x['controlPoint'])
                # ["Excavator","Drone","Truck","Bulldozer","Asphalt Pavers","Compactor"]
                numberOfNecessaryVehicle = [0, 0, 0, 0, 0, 0]
                numberOfNecessaryVehicle[0] = x["vehicles"]['Excavator']
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                y = Task(x['name'], x['priority'], taskType2, False, x['targetPoint'], 5,
                         controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            elif x['type'] == "Pit Filling":
                controlPoint = returnPointbyName(x['controlPoint'])
                numberOfNecessaryVehicle = [0, 0, 0, 0, 0, 0]
                numberOfNecessaryVehicle[2] = x["vehicles"]['Truck']
                numberOfNecessaryVehicle[3] = x["vehicles"]['Bulldozer']
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                y = Task(x['name'], x['priority'], taskType3, False, x['targetPoint'], 5,
                         controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            elif x['type'] == "Pouring Asphalt":
                controlPoint = returnPointbyName(x['controlPoint'])
                numberOfNecessaryVehicle = [0, 0, 0, 0, 0, 0]
                numberOfNecessaryVehicle[4] = x["vehicles"]['Asphalt Paver']
                numberOfNecessaryVehicle[5] = x["vehicles"]['Compactor']
                start_time = datetime.strptime(x['startTime'][0:5], date_format)
                end_time = datetime.strptime(x['finishTime'][0:5], date_format)
                timePeriod = [start_time, end_time]
                y = Task(x['name'], x['priority'], taskType4, False, x['targetPoint'], 5,
                         controlPoint, timePeriod, numberOfNecessaryVehicle)
                system.addTask(y)
            else:
                return None
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
'''  
task1 = Task("A", "High", taskType2, False, [3, 4], 5, controlPoint1, [start_time, end_time], numOfVehicleForEachType1)
task2 = Task("B", "Low", taskType2, False, [3, 4], 5, controlPoint2, [start_time, end_time], numOfVehicleForEachType1)
task3 = Task("C", "Medium", taskType3, False, [1, 2], 5, controlPoint2, [start_time2, end_time2],
             numOfVehicleForEachType2)
task4 = Task("D", "High", taskType2, False, [3, 4], 5, controlPoint2, [start_time, end_time], numOfVehicleForEachType3)
task5 = Task("E", "Low", taskType1, False, controlPoint2.coordinates, 5, controlPoint2, [start_time3, end_time3], numOfVehicleForEachType5)
task6 = Task("F", "High", taskType2, False, [3, 7], 5, controlPoint2, [start_time, end_time], numOfVehicleForEachType3)
task7 = Task("G", "Medium", taskType3, False, [3, 4], 5, controlPoint2, [start_time1, end_time1],
             numOfVehicleForEachType2)
task8 = Task("H", "Low", taskType2, False, [10, 12], 5, controlPoint2, [start_time1, end_time1], numOfVehicleForEachType3)
task9 = Task("I", "Low", taskType2, False, [1, 4], 5, controlPoint2, [start_time2, end_time2], numOfVehicleForEachType1)
task10 = Task("J", "High", taskType1, False, controlPoint3.coordinates, 6, controlPoint1, [start_time1, end_time1],
              numOfVehicleForEachType6)
task11 = Task("K", "Low", taskType1, False, controlPoint2.coordinates, 6, controlPoint2, [start_time8 , end_time8],
              numOfVehicleForEachType7)

task12 = Task("L","Medium",taskType4,False,[4,6],6,controlPoint1,[start_time1, end_time1],numOfVehicleForEachType4)
task13 = Task("M","High",taskType4,False,[4,4],6,controlPoint2,[start_time3,end_time3],numOfVehicleForEachType4)
task14 = Task("N","Low",taskType4,False,[15,15],6,controlPoint1,[start_time3,end_time3],numOfVehicleForEachType4)
task15 = Task("T","High",taskType1,False, controlPoint1.coordinates,6,controlPoint1,[start_time1,end_time1],numOfVehicleForEachType5)

system.addTask(task1)
system.addTask(task2)
system.addTask(task3)
system.addTask(task4)
system.addTask(task5)
system.addTask(task6)
system.addTask(task7)
system.addTask(task8)
system.addTask(task9)
system.addTask(task10)
system.addTask(task11)
system.addTask(task12)
system.addTask(task13)
system.addTask(task14)
system.addTask(task15)

'''
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
createControlPoint(result['controlPoints'])
createVehicles(result['Vehicles'])
createTask(result['Tasks'])
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
system.listTasks()
system.run()
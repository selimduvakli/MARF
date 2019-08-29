import datetime
import json
import threading
import requests
import Controller
import Mapper2
import time
MY_ID = 3
MY_NAME = "user_interface"
TOPICS_SUBSCRIBED = ["Task2UI", "Drone2UI", "MA2UI"]
TOPICS_PUBLISHED = ["UI2Task", "UI2Drone", "UI2MA"]
Ip = "127.0.0.1"
Port = 5000
URL = ("http://%s:%d" % (Ip, Port))

#when we are choosing the two vehicles require tasks the system gives the one path control it

def check(liste):
    i = 0
    while i<len(liste):
        j = 0
        while j<len(liste[i]):
            if liste[i][j][0]<0 or liste[i][j][1]<0:
                liste[i].remove(liste[i][j])
                j=j-1
#after deleting the index list range is decresing so control this situation with decreasing j value
            j=j+1
        i=i+1



def json2Time(tm):
    time = datetime.time()
    time.__setattr__('hour', int(tm.split(':')[0]))
    time.__setattr__('minute', int(tm.split(':')[1].split(':')[0]))
    time.__setattr__('second', 0)
    return time


def json2Date(dt):
    date = datetime.date()
    date.__setattr__('year', int(dt.split('-')[0]))
    date.__setattr__('month', int(dt.split('-')[1].split('-')[0]))
    date.__setattr__('day', int(dt.split('-')[1].split('-')[1]))
    return date


def json2Vehicle(jsn, map):
    name = jsn['name']
    type = jsn['type']
    startPoint = jsn['startPoint']
    try:
        runtmCap = jsn['runtimeCapacity']
        alg = jsn['algorithm']
        vehicle = Controller.Drone(map, name, startPoint, runtmCap, alg)
    except KeyError:
        fuelPercentage = jsn['fuelPercentage']
        speed = jsn['speed']
        powerCapacity = jsn['powerCapacity']
        vehicle = Controller.Vehicle(map, name, type, startPoint, fuelPercentage, speed, powerCapacity)
    return vehicle


def json2Task(jsn):
    name = jsn['name']
    type = jsn['type']
    priority = jsn['priority']
    controlPoint = jsn['controlPoint']
    startTime = json2Time(jsn['startTime'])
    finishTime = json2Time(jsn['finishTime'])
    vehicles = []
    if type == "Visiting Control Point":
        for drn in Controller.Vehicles:
            if drn.type == "Drone":
                vehicles.append(drn)
        try:
            deadline = json2Date(jsn['deadline'])
            task = Controller.RepeatableTaskVisitCP(name, priority, controlPoint, startTime, finishTime, deadline)
        except KeyError:
            task = Controller.NonRepeatableTaskVisitCP(name, priority, controlPoint, startTime, finishTime)
    else:
        targetPoint = jsn['targetPoint']
        try:
            deadline = json2Date(jsn['deadline'])
            task = Controller.RepeatableTask(name, type, priority, targetPoint, controlPoint, startTime, finishTime,
                                             deadline)
        except KeyError:
            task = Controller.NonRepeatableTask(name, type, priority, targetPoint, controlPoint, startTime, finishTime)
        for v in jsn['vehicles']:
            vehicles.append(json2Vehicle(json.loads(v)))
    task.addVehiclesToTask(vehicles)
    return task


class Topic(threading.Thread):
    def __init__(self):
        super().__init__()
        # todo connect to webservice via id
        #self.register_as_subscriber()
        #self.register_as_publisher()

    def register_as_subscriber(self):
        url = URL + "/subscriber"
        data = {"name": MY_NAME, "topics": TOPICS_SUBSCRIBED}
        r2 = requests.post(url, json=data)
        print("Registered to", TOPICS_SUBSCRIBED, "as Subscriber", r2.text)

    def register_as_publisher(self):
        url = URL + "/publisher"
        # todo change here
        data = {"name": MY_NAME, "topics": TOPICS_PUBLISHED}
        r1 = requests.post(url, json=data)
        print("Registered to", TOPICS_PUBLISHED, "as Publisher", r1.text)

    # def Publish(self):
    #     #todo here we connect to topic
    #     #todo send information in form of json
    #
    #
    # def Subsbcribe(self):
    #     #todo here we connect to topic
    #     #todo get information in form of json

    def receive(self, topicName):
        url = URL + "/publish/" + str(MY_ID)
        r4 = requests.get(url)
        x = r4.text
        y = json.loads(x)
        if len(y.values()) == 0:
            return "no data"
        y = y[topicName]["data"]
        return y

    def send(self, topicName, msg):
        try:
            data = {"topic_name": topicName, 'data': msg}  # {"taskDetails": msg}}
            url = URL + "/publish"
            r3 = requests.post(url, json=data)
        except Exception as e:
            print(e)
        print(r3.text)


class UI2Task(Topic):
    def __init__(self):
        pass

    def Publish(self, map, vehicles, tasks, controlPoints):
        vec = []
        tsk = []
        cpont = []
        for v in vehicles:
            vec.append(v.toJSON())
        for t in tasks:
            tsk.append(t.toJSON())
        for cp in controlPoints:
            cpont.append(cp.toJSON())
        jsn = {
            'Map': map.toJSON(),
            'Vehicles': vec,
            'Tasks': tsk,
            'controlPoints': cpont
        }
        self.send("UI2Task", jsn)
        print("Message sent to Task Planner")


class Task2UI(Topic):
    def __init__(self, textBrowser):
        super().__init__()
        self.__stop = False
        self.logScreen = textBrowser

    def Listen(self):
        data = "no data"
        while not self.__stop:
            data = self.receive("Task2UI")
            if data != "no data":
                #data = json.loads(data)
                print(data['taskDetails'])
                time.sleep(4)
                self.logScreen.append(data['taskDetails'])

    def run(self):
        self.Listen()

    def stop(self):
        self.__stop = True

class UI2Drone(Topic):
    def __init__(self):
        pass

    def Publish(self, map, drone):
        data = {
            'Map': map.toJSON(),
            # 'RuntimeCapacity' : runtimeCapacity
            'Drone': drone.toJSON()
        }
        self.send("UI2Drone", data)
        print("Message sent to Drone")


class Drone2UI(Topic):
    def __init__(self, textBrowser):
        super().__init__()
        self.logScreen = textBrowser
        self.__stop = False

    def Listen(self):
        while not self.__stop:
            data = self.receive("Drone2UI")
            if data != "no data":
                # data = json.loads(data)
                print(data)
                #print(data['taskDetails'])
                #self.logScreen.append(data['taskDetails'])

    def stop(self):
        self.__stop = True

    def run(self):
        self.Listen()

class UI2MA(Topic):
    def __init__(self):
        pass

    def Publish(self, map):
        data = {'Map': map.toJSON()}
        self.send('UI2MA', data)
        print("Message sent to M.A.")


class MA2UI(Topic):
    def __init__(self, textBrowser):
        super().__init__()
        self.__stop = False
        self.logScreen = textBrowser

    def Listen(self):
        while not self.__stop:
            data = self.receive("MA2UI")
            if data != "no data":
                # data = json.loads(data)
                print(data)

    def stop(self):
        self.__stop = True

    def run(self):
        self.Listen()


class Listener(Topic):
    def __init__(self, textBrowser, Mapper):
        super().__init__()
        self.logScreen = textBrowser
        self.Mapper = Mapper
        self.__stop = False

    def receive(self):
        url = URL + "/publish/" + str(MY_ID)
        r4 = requests.get(url)
        x = r4.text
        y = json.loads(x)
        if len(y.values()) == 0:
            return "no data"
        return y

    def Listen(self):
        while not self.__stop:
            data = self.receive()
            if data != "no data":
                #print(data)
                if "Task2UI" in data:
                    self.logScreen.append("Task_manager: "+data["Task2UI"]['data']['taskDetails'])
                if "Drone2UI" in data:
                    if "path" in data["Drone2UI"]['data']:
                        print(data["Drone2UI"]['data']['path'])
                        self.Mapper.addAgnt(data["Drone2UI"]['data']['path'])
                    if "taskDetails" in data["Drone2UI"]['data']:
                        self.logScreen.append("Drone_path_planner: "+data["Drone2UI"]['data']['taskDetails'])
                if "MA2UI" in data:
                    if "info" in data["MA2UI"]['data']:
                        self.logScreen.append("Muliagent_sys: "+data["MA2UI"]['data']['info'])
                    if "paths" in data["MA2UI"]['data']:
                     #   print(data["MA2UI"]['data']['paths'])
                     # There was  (-)minus values in the list so we made check method for erase them
                        check(data["MA2UI"]['data']['paths'])
                        print(data["MA2UI"]['data']['paths'])
                        for i in data["MA2UI"]['data']['paths']:
                            self.Mapper.addAgnt(i)

    def stop(self):
        self.__stop = True

    def run(self):
        self.Listen()

from Environment import Environment
from GeneticAlgorithm import GeneticAlgorithm
import copy
import random
import requests
import json


class Main:

    def __init__(self):  # initializing the attribute for use
        self.__genAl = []  # all the agents are kept in a list

    # =============================================================================
    #   Sets the agent list
    #   @param agent list to set
    # =============================================================================
    def setGenAl(self, genAl):
        self.__genAl = genAl

    # =============================================================================
    #   @return the point of the state variable fitness point and found boolean tag
    # =============================================================================
    def getGenAl(self):

        return self.__genAl

    # =============================================================================
    #   adding the GenAlg. objects for ai based multi-agent path planning list
    # =============================================================================

    def addGenAl(self, genAlgtoAdd):
        self.__genAl.append(genAlgtoAdd)

    # =============================================================================
    #   discharging the objects for ai based multi-agent path planning list
    # =============================================================================
    def freeGenAlgs(self):
        self.__genAl = []

    # =============================================================================
    #   Checks the elements in the list if found 2 sames return their indexes
    #   if it hasn't returns the flag
    #   @param List for check
    #   @return same values of indexes or true flag
    # =============================================================================
    def dup(self, L):
        i = 0
        j = 0
        flag = True
        while i < len(L) and flag:
            j = i + 1
            while j < len(L) and flag:
                if L[i] == L[j]:  # if we find the equality, we set the flag
                    flag = False
                j += 1
            i += 1
        if not flag:  # if flag is false means that we found a duplication
            if random.randint(1, 2) < 2:  # indexes return randomly with probability of %50 respectively
                return [i - 1, j - 1]
            else:
                return [j - 1, i - 1]
        return flag  # if no indexes are returned, means that we couldn't find any duplication

    # =============================================================================
    #   Controls the whole paths and find the Max length
    #   @param List for finding the max length
    #   @return max len of the elements of the list
    # =============================================================================
    def findMax(self, paths):
        Max = 0
        for i in paths:
            if len(i) > Max:
                Max = len(i)
        return Max

    # =============================================================================
    #   Figure outs the content that needs to change
    #   @param List of paths
    #   @return flag value or dup indexes
    # =============================================================================
    def indexControl(self, paths):
        indexes = []
        j = 1  # start index doesn't count! Collision free movement comes after first move.
        highest = self.findMax(paths)
        result = True
        result2 = []
        while j < highest and result:
            i = 0
            while i < len(paths):
                indexes.append(paths[i][j])
                i += 1
            result2 = self.dup(indexes)
            indexes = []
            if type(result2) == bool:  # if the method returns correct we don't change path
                result = True
            else:
                result = False  # if indexes are returned we shall change paths
            j += 1
        if result:

            return result
        else:

            return [result2[0], result2[1]]  # changePath method will know the routes to change

    # =============================================================================
    #   Add the first elements in the list to new indexes list and returned it
    #   @param List to get the first elements
    #   @return first element list
    # =============================================================================
    def addIndexes(self, List):
        indexes = []
        i = 0
        while i < len(List):
            indexes.append(List[i][0])  # indexes list only takes first elements of the parameter list
            i += 1

        return indexes

    # =============================================================================
    #   Checks the elements in the list and creates an unique list
    #   @param List for check
    #   @return unique list
    # =============================================================================
    def duplicate(self, items):
        unique = []
        for item in items:
            if item not in unique:  # if it has the same value don't add them to the list
                unique.append(item)

        return unique

    # =============================================================================
    #   This method creates path for every agent in the system
    #   @return path list
    # =============================================================================
    def changePath(self):
        maxLen = 0  # max route length int path list
        multiAgentPath = []  # path list for every agent with alternative ones
        for i in self.__genAl:
            agent = []  # one agent paths with alternatives
            for j in i.getTruePaths():  # for every path in agent i
                withOutStart = j.getCoord()  # first calculate the coordinates
                agent.append(withOutStart)  # after append them to agent path
                a = i.getStart()  # after that construct the same coordinates with 1 movement delay
                withStart = withOutStart[::-1]
                withStart.append(a)
                withStart.reverse()
                agent.append(withStart)  # lastly add the delayed path
                withOutStart = j.getCoord()
                agent.append(withOutStart)
                if len(withStart) > maxLen:
                    maxLen = len(withStart)  # if max route length is less than this route we'll change the maxLen
            agent = self.duplicate(agent)  # duplicate paths are removed
            multiAgentPath.append(agent)  # add them to agents path list

        counter = [-1, -1]  # some routes may have less steps than maxLen
        for i in multiAgentPath:
            for j in i:
                while len(j) < maxLen:  # in that case we add them with counter coordinates
                    j.append(copy.deepcopy(counter))  # and make number of list elements to maxLen
                    counter[0] -= 1  # for every adding we change the counter coordinates because
                    counter[1] -= 1  # we don't want to disturb the unique

        result = False
        flag = True
        indexes = []
        while flag and not result:  # flag takes the road length control and result takes the index control
            indexes = self.addIndexes(multiAgentPath)  # first indexes (which are agent paths) are added
            result = self.indexControl(indexes)  # result value comes from control the path index control
            if type(result) == list:  # if the returned value is list means that there is a collision and we need to fix
                indexes.pop(result[1])  # first are useless now we change it from our alternative paths
                multiAgentPath[result[1]].pop(0)  # of course it is popped from multiAgentPath, too.
                if len(multiAgentPath[result[1]]) > 0:  # if there is still available road
                    indexes.insert(result[1], multiAgentPath[result[1]][0])  # we try another alternative
                    result = self.indexControl(indexes)  # and take the index control of the new agent roads
                else:
                    flag = False  # if there is nothing we exit the loop
            if type(result) == bool:  # if we find an exit we exit also with no collision roads
                result = True
            else:
                result = False  # if we couldn't, we'll continue 'till we find exit

        return indexes

    # =============================================================================
    #   This method checks the mutants for every agent in the system and if it finds
    #   at least one true it continues
    #   @return flag
    # =============================================================================
    def check(self):
        flag = True
        i = 0
        while flag and i < len(self.getGenAl()):  # every agent controlled with their point
            if not self.__genAl[i].bestMutant().getPoint()[1]:  # if it is not true we exit
                flag = False
            i += 1  # if it isn't we continue with other agent

        return flag

    # =============================================================================
    #   This method gets the whole alternative roads for every agent it can be used for
    #   testing the genetic algorithm and finding the routes for agents
    #   @return whole true roads for agents
    # =============================================================================
    # def paths(self):
    #     multiAgentPath = []
    #     for i in self.__genAl:
    #         agent = []
    #         for j in i.getTruePaths():                # THIS METHOD USED FOR
    #             withOutStart = j.getCoord()           # SHOWING ALTERNATIVE
    #             agent.append(withOutStart)            # ROADS FOR EVERY AGENT
    #             a = i.getStart()
    #             withStart = withOutStart[::-1]
    #             withStart.append(a)
    #             withStart.reverse()
    #             agent.append(withStart)
    #             withOutStart = j.getCoord()
    #             agent.append(withOutStart)
    #         agent = self.duplicate(agent)
    #         multiAgentPath.append(agent)
    #
    #     return multiAgentPath
    # =============================================================================

    # =============================================================================
    #   To connect the WebServer first we need to register ourselves one by one
    #   In next steps of the application random access registration can be implemented
    # =============================================================================
    def register(self):
        url = URL + "publisher"
        data = {"name": "Multi-Agent", "topics": ["MAR"]}
        r1 = requests.post(url, json=data)
        print(r1.text)

        data = {"name": "Multi-Agent", "topics": ["MAS"]}
        url = URL + "subscriber"
        r2 = requests.post(url, json=data)
        print(r2.text)

    # =============================================================================
    #   After registration we can send messages to topics. Sending uses JSON objects, too.
    # =============================================================================
    def send(self, topicName, message):
        data = {"topic_name": topicName, "data": {"taskDetails": message}}
        url = URL + "publish"  # # In future studies MA2UI and UI2MA will be added.
        r3 = requests.post(url, json=data)
        print(r3.text)

    # =============================================================================
    #   We can listen the topic which we are connected. From now on, we just speak with task manager
    #   after the UI completed we can speak with UI, too. Our id is static which is 2 now.
    #   Dynamic id assigning may be implemented in next studies.
    # =============================================================================
    def receive(self, topicName):  # gets value from MAS to communicate with task manager
        url = URL + "publish/2"    # MAPP uses id of 2
        r4 = requests.get(url)     # In future studies MA2UI and UI2MA will be added.
        x = r4.text
        y = json.loads(x)
        if len(y.values()) == 0:
            return "no data", "no data"
        y = y[topicName]["data"]["taskDetails"]

        return y[0], y[1]


if __name__ == '__main__':
    URL = "http://10.40.4.33:5000/"

    main = Main()  # initialization the main program
    main.register()  # singing up to WebServer
    # UI is not finished yet, so we use static map which is given below
    temp_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    env = Environment(30, 30)  # env initiation
    env.setMap(temp_map)  # setting the map for test

    while True:  # after connection is completed, system works permanently
        main.freeGenAlgs()  # first we remove the agents that we had
        points = main.receive("MAS")  # after that we wait for locations from Task Manager
        j = 0
        while points[0] == 'no data':  # if there is no signal, we'll wait for it
            if j % 100 == 0:
                print("data is waiting")
            j += 1
            points = main.receive("MAS")
        print(points)

        i = 0
        lenPoint = len(points[0])
        for i in range(lenPoint):  # for every agent we have one start and same end point.
            print("Starting Point: " + str(points[0][i]) + " End Point: " + str(points[1]))
            start = points[0][i]  # for example starts will be (3, 2) and (4, 5) but ends must same, such as (9, 6)
            end = points[1]  # end point always comes with last index of the receiving list
            genAl = GeneticAlgorithm(env, start, end)  # we have start and end point we initiate our agent
            genAl.geneticAlgorithm()  # we run genetic algorithm
            genAl.getTruePaths()  # we find the true paths it gives us the alternative paths, too.
            main.addGenAl(copy.deepcopy(genAl))  # we append them to agent list
        print("Agent Number: " + str(len(main.getGenAl())))  # writing the agent number for verification

        i = 0
        if main.check():  # if all the agent have true paths we enter
            agentPaths = main.changePath()  # we try to find no collision path for every one of them
            # agentRoads = main.paths()
            while i < 20 and (len(agentPaths) != len(main.getGenAl()) or not agentPaths):
                agentPaths = main.changePath()  # path indexes change randomly so we can try for many times such as 20
                # agentRoads = main.paths()
                i += 1

            if len(agentPaths) != len(main.getGenAl()) or not agentPaths:  # if we can't we send negative message
                result = "not completed"                                   # to Task Manager
                print("Collision Happened. Road Couldn't Find.")
                main.send("MAR", result)
            else:  # if we can we send positive message to Task Manager
                result = "completed"
                env.showMap3(agentPaths) #it can be used for illustration
                main.send("MAR", result)
        else: # if all the agent have not true paths we enter the else branch and send negative message to Task Manager
            result = "not completed"
            print("One or more agent couldn't find their road.")
            main.send("MAR", result)
        print("Number Of Trials: " + str(i))  # lastly we write trial number for confirmation

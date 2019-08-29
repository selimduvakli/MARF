import matplotlib.pyplot as plt
import copy
from random import randint
from State import State


class GeneticAlgorithm:

    def __init__(self, environment, start, end):  # this class for fittest individuals are selected for reproduction
        self.__environment = environment  # our map and its attributes
        self.__truePaths = []  # founded paths are collected here
        self.__start = start  # agent starting point kept here
        self.__end = end  # agent arrival point kept here
        self.__population = self.initializePopulation(200)  # it will be our path for finding route for every agents

    # =============================================================================
    #   Sets the population which has 200 individuals in it.
    #   @param population to set
    # =============================================================================
    def setPopulation(self, population):
        self.__population = population

    # =============================================================================
    #   @return current population of the agent
    # =============================================================================
    def getPopulation(self):
        return self.__population

    # =============================================================================
    #   Sets the starting point of the agent.
    #   @param start point to set
    # =============================================================================
    def setStart(self, start):
        self.__start = start

    # =============================================================================
    #   @return starting coordinate
    # =============================================================================
    def getStart(self):
        return self.__start

    # =============================================================================
    #   Sets the end point of the agent.
    #   @param end point to set
    # =============================================================================
    def setEnd(self, end):
        self.__end = end

    # =============================================================================
    #   @return end coordinate
    # =============================================================================
    def getEnd(self):
        return self.__end

    # =============================================================================
    #   Sets the environment which has the map for the agent.
    #   @param environment to set
    # =============================================================================
    def setEnvironment(self, environment):
        self.__environment = environment

    # =============================================================================
    #   @return current environment
    # =============================================================================
    def getEnvironment(self):
        return self.__environment

    # =============================================================================
    #   Calculates point and determines the found value for given path
    #   @param path for the agent which is an state position
    #   @return cost of the path and found boolean value
    # =============================================================================
    def fitness(self, path):  # finding a point for every path which is created
        mapCost = 0  # agent can not exit the map
        obsCost = 0  # agent can not hit the obstacle
        cost = 0  # total cost for path
        i = 0  # loop variable
        tempMap = copy.deepcopy(self.getEnvironment().getMap())  # we take a copy the original map for manipulating
        current = copy.deepcopy(self.__start)  # taking the places we are passing
        flag = True  # loop variable for exceptional exit
        found = False  # did we find the exit, if we did, variable would have turn true
        while i < len(path) and flag:
            if path[i] == 1:  # for moving left
                current[0] -= 1  # x variable decreases 1
            elif path[i] == 2:  # for moving right
                current[0] += 1  # x variable increases 1
            elif path[i] == 3:  # for moving down
                current[1] -= 1  # y variable decreases 1
            else:  # other condition means moving up
                current[1] += 1  # y variable increases 1
            i += 1
            if current[0] < 0 or current[1] < 0 or current[0] >= self.getEnvironment().getSizeX() or \
                    current[1] >= self.getEnvironment().getSizeY():
                flag = False  # if it is out of map it dies
                rand = randint(1, 4)
                while rand + path[i - 1] == 3 or rand + path[i - 1] == 7:
                    rand = randint(1, 4)
                path[i - 1] = rand
                mapCost = 60
            elif tempMap[current[0]][current[1]] == 1:
                flag = False  # if there is an obstacle it won't move and dies
                rand = randint(1, 4)
                while rand + path[i - 1] == 3 or rand + path[i - 1] == 7:
                    rand = randint(1, 4)
                path[i - 1] = rand
                obsCost = 50
            elif current == self.__end:
                flag = False  # if it finds the exit, means that we found the road :)
                found = True
            else:
                tempMap[current[0]][current[1]] = 3  # we will follow the road
        distanceCost = abs(current[0] - self.__end[0]) + abs(current[1] - self.__end[1])
        # for distance we take manhattan distance
        roadCost = int(i / 2)
        cost = mapCost + roadCost + distanceCost + obsCost  # our total cost

        return [cost, found]

    # =============================================================================
    #   This method demonstrates the map for visualization
    # =============================================================================
    def showMap(self):  # for illustrating the map
        plt.imshow(self.__environment.getMap())
        plt.show()

    # =============================================================================
    #   Method that returns best fitness pointed individual in the population
    #   @return best individual in the population
    # =============================================================================
    def bestMutant(self):
        minimum = self.getPopulation().__getitem__(0).getPoint()[0]
        best = self.getPopulation()[0]
        for i in self.getPopulation():
            if minimum > i.getPoint()[0]:  # comparision for every element in the population
                minimum = i.getPoint()[0]
                best = i  # if found one best would change

        return best

    # =============================================================================
    #   Method that returns worst fitness pointed individual in the population
    #   @return worst individual in the population
    # =============================================================================
    def worstMutant(self):
        maxState = self.getPopulation().__getitem__(0).getPoint()[0]
        worst = self.getPopulation()[0]
        for i in self.getPopulation():
            if maxState < i.getPoint()[0]:  # comparision for every element in the population
                maxState = i.getPoint()[0]
                worst = i  # if found one worst would change

        return worst

    # =============================================================================
    #   Method that returns the individual according to probability. It uses
    #   Roulette Wheel Selection for choosing the individual
    #   @return worst individual in the population
    # =============================================================================
    def selection(self):
        sumOfFitness = 0  # total fitness point in population
        select = []  # our container for sumOffitness values
        index = 0  # for array accesing
        for i in self.getPopulation():
            sumOfFitness += (200 - i.getPoint()[0])  # calculating the values min in better
            select.append(sumOfFitness)  # adding the value to list
        pr = randint(1, sumOfFitness)  # roulette wheel selections random value
        while select[index] < pr:
            index += 1  # while we couldn't reach the pr index will increase

        return self.getPopulation()[index]

    # =============================================================================
    #   Genetic algorithms population starts here with random values.
    #   @return initialized population
    # =============================================================================
    def initializePopulation(self, popSize):
        pop = []
        for j in range(0, popSize):
            path = []
            tmp = State()
            path.append(randint(1, 4))
            for i in range(1, 75):  # starting movements are all random
                rand = randint(1, 4)  # 1: left 2: right 3: down 4: up
                while rand + path[i - 1] == 3 or rand + path[i - 1] == 7:
                    # if any one of the subpath is repeating, we'll change it like 1 after 2 or 3 after 4
                    rand = randint(1, 4)
                path.append(rand)
            tmp.setPosition(path)
            tmp.setPoint(self.fitness(tmp.getPosition()))
            pop.append(tmp)

        return pop

    # =============================================================================
    #   Takes the parents and generates the child. All individuals are state
    #   @param parents for produce child
    #   @return initialized population
    # =============================================================================
    def reproduce(self, parent1, parent2):
        i = 0
        rand = randint(1, len(parent1.getPosition()) - 1)  # which genes comes from father
        child = State()
        path = []
        for i in range(rand):  # crossover point 
            path.append(parent1.getPosition()[i])  # new path formed from fathers and mothers genes
        while i < len(parent1.getPosition()) - 1:  # which genes comes from mother
            path.append(parent2.getPosition()[i])
            i += 1

        child.setPosition(path)  # after chromosome is took its shape we gave them to child
        child.setPoint(self.fitness(path))  # chromosomes fitness point is calculated

        return child

    # =============================================================================
    #   Takes the child and generates a new mutant child.
    #   @param  child
    #   @return mutant child
    # =============================================================================
    def mutation(self, child):
        rand = randint(1, len(child.getPosition()) - 1)  # index will be mutate
        rand2 = randint(1, 4)
        while child.getPositionValue(rand - 1) + rand2 == 3 or \
                child.getPositionValue(rand - 1) + rand2 == 7 or \
                child.getPositionValue(rand) == rand2:  # if any one of the subpath is repeating we change
            rand2 = randint(1, 4)  # if it is the same before change

        child.setPositionValue(rand, rand2)  # after changing its values position also changed
        child.setPoint(self.fitness(child.getPosition()))  # and childs fitness point recalculated

        return child

    # =============================================================================
    #   Method that returns founded path list
    #   @return sorted by score path list
    # =============================================================================
    def getTruePaths(self):
        for i in self.__truePaths:
            if not i.getPoint()[1]:  # after mutations if it changes we remove it
                self.__truePaths.remove(i)
        a = []
        for i in self.__truePaths:
            if i not in a and i.getPoint()[1]:  # no duplicates are allowed
                i.calculateCoordinates(self.__start, self.__end)
                a.append(i)
        # returning sorted by fitness score so that we can get
        # less movement for every agent respectively
        return sorted(a, key=lambda x: x.getPoint()[0])

    # =============================================================================
    #   Calculates the number of iteration.
    #   @return number of iteration
    # =============================================================================
    def iterationOfWhile(self):

        return self.getEnvironment().getSizeX() * self.getEnvironment().getSizeY()

    # =============================================================================
    #   Main method for genetic algorithm. This method changes the individuals in
    #   the population and creates better ones.
    #   @return changed population
    # =============================================================================
    def geneticAlgorithm(self):
        k = 0  # loop variable
        foundTemp = []  # found point is true ones
        newPop = []  # new population kept for new arrived individuals
        while k < 2 * self.iterationOfWhile() / 3:
            # =============================================================================
            if k % 100 == 0:
               print(str(k) + " " + "Best Score " + str(self.bestMutant().getPoint()[0]) + " " + str(
                   self.bestMutant().getPoint()[1]))
            #   for following the genetic algorithm this code can be used.
            # =============================================================================

            newPop = []  # new population kept here every new iteration
            k += 1
            p = 0
            j = 0
            foundTemp = self.getFound()  # founded ones are decomposed
            lenFound = len(foundTemp) - 1  # number of founded ones

            for i in range(10):
                worst = self.worstMutant()
                self.removeFromPopulation(worst)

            # Creating new 10 length population and add them to new population
            randPop = self.initializePopulation(10)
            for t in randPop:
                newPop.append(t)

            while j < lenFound:
                newPop.append(foundTemp[j])  # new population use the founded ones
                self.__truePaths.append(foundTemp[j])  # true paths also collect this
                j += 1
            lenPop = len(newPop)

            for i in range(0, 200 - lenPop):
                parent1 = self.selection()  # parents are selected 
                parent2 = self.selection()
                m = 0  # iteration variable

                while parent1 == parent2 or m < 5:  # if parents are same change it
                    parent2 = self.selection()
                    m += 1
                child = self.reproduce(parent1, parent2)  # child generation
                if randint(1, 100) < 85:  # mutation ratio
                    child = self.mutation(child)  # child mutation
                newPop.append(child)  # adding new child to population

            for p in range(50 - lenPop):
                best = self.bestMutant()  # good individual are selected
                self.removeFromPopulation(best)  # deleted from previous population
                if not best.getPoint()[1] and randint(1, 10) < 7:
                    best = self.mutation(best)  # if we don't reach the end we change 
                    # best ones and change their genes
                newPop.append(best)
            self.setPopulation(newPop)  # new population are setted

        return newPop

    # =============================================================================
    #   Method that finds true paths with duplicates
    #   @return founded individuals
    # =============================================================================
    def getFound(self):
        foundParents = []
        for i in self.getPopulation():
            if i.getPoint()[1]:  # if it has true value in point we append it to list
                foundParents.append(i)

        return foundParents

    # =============================================================================
    #   Deletes the element from the population.
    # =============================================================================
    def removeFromPopulation(self, best):
        self.getPopulation().remove(best)

    # =============================================================================
    #   Method that finds true paths without duplicates
    #   @return founded individuals
    # =============================================================================
    def getFound2(self):
        foundParents = []
        for i in self.getPopulation():
            if i not in foundParents and i.getPoint()[1]:
                foundParents.append(i.getPoint())

        return foundParents

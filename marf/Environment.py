import numpy as np
from random import randint
import matplotlib.pyplot as plt
import copy


class Environment:

    def __init__(self, sizeX, sizeY):  # initializing the environment

        if (30 >= sizeX >= 10 and 30 >= sizeY >= 10):
            # if user don't enter valid length, we don't create environment
            self.__sizeX = sizeX  # dimension x size of map
            self.__sizeY = sizeY  # dimension y size of map
            self.__map = np.zeros((sizeX, sizeY))  # starting with empty map
        else:
            raise Exception('Map Dimension shall between 10 and 30 but entered X:'+ str(sizeX) + ' and Y:'
                            + str(sizeY))

    # =============================================================================
    #   Sets the x dimension of map
    #   @param sizeX to set
    # =============================================================================
    def setSizeX(self, sizeX):
        self.__sizeX = sizeX

    # =============================================================================
    #   @return dimension X size
    # =============================================================================
    def getSizeX(self):

        return self.__sizeX

    # =============================================================================
    #   Sets the y dimension of map
    #   @param sizeY to set
    # =============================================================================
    def setSizeY(self, sizeY):
        self.__sizeX = sizeY

    # =============================================================================
    #   @return dimension X size
    # =============================================================================
    def getSizeY(self):

        return self.__sizeY

    # =============================================================================
    #   Sets the environment Map
    #   @param newMap to set
    # =============================================================================
    def setMap(self, newMap):
        self.__map = newMap

    # =============================================================================
    #   @return the Map
    # =============================================================================
    def getMap(self):

        return self.__map

    # =============================================================================
    #   This method adds obstacle to map
    #   @param x and y axis to add obstacle
    #   @return boolean
    # =============================================================================
    def addObstacle(self, x, y):
        if self.__sizeX >= x >= 0 and self.__sizeY >= y >= 0:
            self.__map[x][y] = 1  # obstacle will be added if user enters

            return 1  # correct information
        else:

            return 0

    # =============================================================================
    #   This method deletes obstacle to map
    #   @param x and y axis to delete obstacle
    #   @return boolean
    # =============================================================================
    def deleteObstacle(self, x, y):
        if self.__sizeX >= x >= 0 and self.__sizeY >= y >= 0:
            self.__map[x][y] = 0  # obstacle will be deleted if user enters

            return 1  # correct information
        else:

            return 0

    # =============================================================================
    #   This method construct a map with obsRatio value
    #   @param obsRatio to add obstacle
    # =============================================================================
    def randomMap(self, obsRatio):  # if user wants random map, this method will work
        map = []
        for i in range(self.__sizeX):
            tmp = []
            for j in range(self.__sizeY):
                r = randint(1, 100)
                if r < obsRatio:  # system takes the ratio for adding blocks/obstacles
                    tmp.append(1)
                else:
                    tmp.append(0)
            map.append(tmp)
        self.__map = map

    # =============================================================================
    #   Method that demonstrates the map
    # =============================================================================
    def showMap(self):  # for illustration
        plt.imshow(self.__map)
        plt.show()

    # =============================================================================
    #   Method that demonstrates the map with given state
    #   @param state, start and end coordinates
    # =============================================================================
    def showMap2(self, mutant, start, end):  # for testing simulating the map
        tempMap = copy.deepcopy(self.getMap())
        current = start.copy()
        i = 0
        while current != end and i < 75 and (0 <= current[0] < self.getSizeX()) \
                and (0 <= current[1] < self.getSizeY()) and \
                tempMap[current[0]][current[1]] != 1:
            tempMap[current[0]][current[1]] = 2
            if mutant.getPositionValue(i) == 1:
                current[0] -= 1

            elif mutant.getPositionValue(i) == 2:
                current[0] += 1

            elif mutant.getPositionValue(i) == 3:
                current[1] -= 1
            else:
                current[1] += 1
            i += 1
        tempMap[current[0]][current[1]] = 2
        plt.imshow(tempMap)
        plt.show()

    # =============================================================================
    #   Method that demonstrates the map with given coordinates
    #   @param agent coordinates
    # =============================================================================
    def showMap3(self, agentCoord):
        for i in agentCoord:
            tempMap = copy.deepcopy(self.getMap())
            k = 3
            for j in i:
                if j[0] >= 0:
                    tempMap[j[0]][j[1]] = k
            k += 1
            plt.imshow(tempMap)
            plt.show()

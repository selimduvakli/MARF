class State:

    def __init__(self):  # state holds the status of one agent
        self.__position = []  # movements are keept here left ->1 right->2 down ->3 up->4
        self.__point = []  # variable that fitness score and found boolean are in it.
        self.__coordinates = []  # x and y coordinates for the path state

    # =============================================================================
    #   Sets the position.
    #   @param position to set
    # =============================================================================
    def setPosition(self, position):
        self.__position = position

    # =============================================================================
    #   @return current position array of the agent
    # =============================================================================
    def getPosition(self):

        return self.__position

    # =============================================================================
    #   Sets coordinate array.
    #   @param coordinate to set
    # =============================================================================
    def setCoord(self, coord):
        self.__coordinates = coord

    # =============================================================================
    #   @return current coordinates of the agent
    # =============================================================================
    def getCoord(self):

        return self.__coordinates

    # =============================================================================
    #   Sets the position value by given index.
    #   @param value to set
    # =============================================================================
    def setPositionValue(self, index, value):
        self.__position[index] = value

    # =============================================================================
    #   @return current position of the given index
    # =============================================================================
    def getPositionValue(self, index):

        return self.__position[index]

    # =============================================================================
    #   Sets the point. Point has two elements -> fitness point and found boolean tag
    #   @param point to set
    # =============================================================================
    def setPoint(self, point):
        self.__point = point

    # =============================================================================
    #   @return the point of the state variable fitness point and found boolean tag
    # =============================================================================
    def getPoint(self):

        return self.__point

    # =============================================================================
    #   Sets the coordinate values of given index.
    #   @param index and value
    # =============================================================================
    def setCoordinates(self, index, value):
        self.__coordinates[index] = value

    # =============================================================================
    #   @return coordinate of the given index
    # =============================================================================
    def getCoordinates(self, index):

        return self.__coordinates[index]

    # =============================================================================
    #   This method takes the parameters and calculates the coordinates using position
    #   array
    #   @param start and end coordinates
    #   @return the point of the state variable fitness point and found boolean tag
    # =============================================================================
    def calculateCoordinates(self, start, end):
        current = start.copy()  # first take the starting point to memory
        i = 0  # loop variable
        self.__coordinates = []  # path coordinates are taken from a list

        while i < 75 and current != end:  # until we reach the end or reach the limit of position
            if self.getPositionValue(i) == 1:  # move left
                current[0] -= 1

            elif self.getPositionValue(i) == 2:  # move right
                current[0] += 1

            elif self.getPositionValue(i) == 3:  # move down
                current[1] -= 1
            else:
                current[1] += 1  # move up
            i += 1
            j = current.copy()  # copy the coordinate
            self.__coordinates.append(j)  # add the coordinate to list

        return self.__coordinates  # send the calculated coordinates

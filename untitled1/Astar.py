# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:33:22 2019

@author: toprak.kesgin
"""

from State import State
import matplotlib.pyplot as plt
import copy

class Astar():

    # Constructor For A* Algorithm
    # Start: Start Point Coordinates
    # End: End Point Coordinates
    # Environment: Grid map that algorithms work


    def __init__(self,start,end,environment,runtime):
        self.start = start
        self.end = end
        self.maze = environment
        self.runtime = runtime


    def astar(self):

        self.maze.Map[self.start[0]][self.start[1]] = 0
        self.maze.Map[self.end[0]][self.end[1]] = 0

        # Creates the start State

        start_state = State(None, self.start)
        start_state.g = start_state.h = start_state.f = 0

        # Creates the end state

        end_state = State(None, self.end)
        end_state.g = end_state.h = end_state.f = 0

        # initialites the open and closed list

        open_list = []
        closed_list = []

        open_list.append(start_state)
        i = 0

        found = False

        path = [[0,0,0,0,0],[0,0,0,0,0]]

        while len(open_list) > 0 and not(found):
            i += 1

            # Finds the lowest f value state from the open list

            current_state = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_state.f:
                    current_state = item
                    current_index = index

            # Removes lowest f value state from the open_list and adds to closed list

            open_list.pop(current_index)
            closed_list.append(current_state)

            # If the path is found

            if current_state == end_state:

                found = True

                path = []
                current = current_state

                # Creates found path's coordinates

                while current is not None:
                    path.append(current.location)
                    current = current.parent


            # variable for holding walkable states from the current state

            neighbors = []

            for new_location in [[0, -1], [0, 1], [-1, 0], [1, 0]]:

                walkAble = True

                # Get Current state's coordinates

                state_location = [current_state.location[0] + new_location[0], current_state.location[1] + new_location[1]]

                # if Exceeds the map

                if state_location[0] > (self.maze.n - 1) or state_location[0] < 0 or state_location[1] > self.maze.m - 1 or state_location[1] < 0:
                    walkAble = False

                # If there is a obsacle

                elif self.maze.Map[state_location[0]][state_location[1]] != 0:
                    walkAble = False

                if(walkAble):


                    # Creates new State

                    new_state = State(current_state, state_location)

                    # Adds for control

                    neighbors.append(new_state)

                    # loops for these states


                    # If state is already closed list
                    for child in neighbors:
                        isClose = 0
                        isOpen = 0
                        for closed in closed_list:
                            if child.location == closed.location:
                                isClose = 1


                        # If state is not in closed list

                        if isClose == 0:

                            # Calculate g,h,f values for state

                            child.g = current_state.g + 1
                            child.h = abs(child.location[0] - end_state.location[0]) + abs(child.location[1] - end_state.location[1])
                            child.f = child.g + child.h

                            # If state is open list and it is better g value from open list

                            for open_state in open_list:
                                if open_state.location == child.location:
                                    if child.g < open_state.g:
                                        open_state.parent = current_state
                                        open_state.g = current_state.g + 1
                                        open_state.f = open_state.g + open_state.h
                                        isClose = 1

                            # If state is open list

                        if not(isClose == 1):
                            for opn in open_list:
                                if child.location == opn.location:
                                    isOpen = 1
                            if isOpen == 0:
                                open_list.append(child)


        if len(open_list) <= 0:
            print("Path not Exist")
            return 0
        elif len(path) >= self.runtime:
            print("Not enough runtime")
            return -1

        return path[::-1]

    # Shows the png's of map and path

    def ShowMap(self,path):
        tmpMap = copy.deepcopy(self.maze.Map.copy())
        if(path == -1 or path == 0):
            return
        for i in path:
            a = i[0]
            b = i[1]
            tmpMap[a][b] = 2
        print("Path that found by A* ")
        plt.imshow(tmpMap)
        plt.show()

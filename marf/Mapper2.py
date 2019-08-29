import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time


def animate(mat, current_position, ag_path, ag_id):
    for agnum in range(len(current_position)):
        ''' ag_path[agnum] -> [[1,1], [1,2],[1,3], [2,3], [3,3], [4,3], [4,2], [5,2], [6,2], [6,3], [6,4]]
            [current_position[agnum]] -> 0; [1,1]
            [0] -> 1'''
        ''' ag_path[agnum] -> [[1,1]],[>i][23
        
        '''
        if current_position[agnum] < (len(ag_path[agnum]) - 1):
            x = ag_path[agnum][current_position[agnum]][0]
            y = ag_path[agnum][current_position[agnum]][1]
            mat[x][y] = 0
            current_position[agnum] += 1
            '''position <- next_position'''
            x = ag_path[agnum][current_position[agnum]][0]
            y = ag_path[agnum][current_position[agnum]][1]
            mat[x][y] = ag_id[agnum]
        else:
            '''loops back to the start of animation'''
            x = ag_path[agnum][current_position[agnum]][0]
            y = ag_path[agnum][current_position[agnum]][1]
            mat[x][y] = 0
            current_position[agnum] = 0
            x = ag_path[agnum][current_position[agnum]][0]
            y = ag_path[agnum][current_position[agnum]][1]
            mat[x][y] = ag_id[agnum]

class Mapper2(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.ag_id = []
        self.ag_path = []
        self.current_position = []
        # her agent için bir sıfır daha eklenecek
        self.agntCount = 0
        # a figure instance to plot on
        self.figure = plt.figure()

        #canvaas widget
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.my_timer = QtCore.QTimer()
        self.my_timer.timeout.connect(self.plot)

    def plot(self):
        ''' plot some stuff '''

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        # cmap = ListedColormap(['k', 'w', 'r', "#FFA500"])
        ax.matshow(self.map)  # , cmap=cmap)
        animate(self.map, self.current_position, self.ag_path, self.ag_id)
        # refresh canvas
        self.canvas.draw()

    def addMap(self, map):
        self.map = map

        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 1:
                    # map[i][j] = max(self.ag_id) + 1
                    self.map[i][j] = 1

        '''Fixes the color problem by always making sure that maximum id is same'''
        self.my_timer.start(500)

    def addAgnt(self, agentPath):
        self.ag_path.append(agentPath)
        self.ag_id.append(self.agntCount+1)
        self.current_position.append(0)
        x = self.ag_path[self.agntCount][self.current_position[self.agntCount]][0]
        y = self.ag_path[self.agntCount][self.current_position[self.agntCount]][1]
        self.map[x][y] = self.ag_id[self.agntCount]
        '''This is for initial agent position setup'''
        self.agntCount += 1
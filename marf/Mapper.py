import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import Controller


def samplemat(dims):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = np.zeros(dims)
    # for i in range(min(dims)):
    #     aa[i, i] = i
    aa[0, 0] = 1
    return aa


def animate(aa, i):
    if Controller.Map != None:
        aa = Controller.Map.toJSON()
    else:
        aa[i, i] = 0
        aa[(i + 1) % 15, (i + 1) % 15] = 1
    return aa


class Mapper(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.aa = samplemat((15, 15))
        self.my_timer = QtCore.QTimer()
        self.my_timer.timeout.connect(self.plot)
        self.i = 0

    def plot(self):
        ''' plot some stuff '''

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.matshow(self.aa)
        self.aa = animate(self.aa, self.i)
        self.i = (self.i + 1) % 15
        # refresh canvas
        self.canvas.draw()

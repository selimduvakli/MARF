# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:32:51 2019

@author: toprak.kesgin
"""

class State():

    def __init__(self, parent=None, location=None):
        self.g = 0
        self.h = 0
        self.parent = parent
        self.location = location
        self.f = 0


    def __eq__(self, other):
        return self.location == other.location

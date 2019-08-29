class ControlPoint:

    def __init__(self,name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.tasks = []

    # The control point can't have task name with same name
    def isTaskNameUnique(self,name):
        i = 0
        size = len(self.tasks)

        while(i < size and name != self.tasks[i]):
            i+=1

        if i < size:
            return False
        else:
            return True

    def addTaskToControlPoint(self,task):

        if self.isTaskNameUnique(task.name):
            self.tasks.append(task)


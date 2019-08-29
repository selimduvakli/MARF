class TaskType:

    def __init__(self, name, necessaryVehicleTypes, stepOfPlan):
        self.name = name
        self.necessaryVehicleTypes = necessaryVehicleTypes
        self.stepOfPlan = stepOfPlan

    def addNewSteps(self,newStep):
        self.stepOfPlan.append(newStep)

    def writeStepsOfPlan(self):
        for i in range(len(self.stepOfPlan)):
            print(str(i)+"-) "+self.stepOfPlan[i])

    def completeStep(self,i):
        if i < len(self.stepOfPlan):
            print(self.stepOfPlan[i]+" is completed")
        else:
            print("Invalid parameter")
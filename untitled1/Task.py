class Task:

    def __init__(self, name, priority, taskType, isRepeatable, targetPosition, deadline, controlPoint, timePeriod,
                 numberOfNecessaryVehicle):
        self.name = name
        self.priority = priority
        self.targetPosition = targetPosition
        self.deadline = deadline
        self.controlPoint = controlPoint
        self.timePeriod = timePeriod
        self.numberOfNecessaryVehicle = numberOfNecessaryVehicle
        self.situation = "not started"
        self.taskType = taskType
        self.isRepeatable = isRepeatable
        self.plan = []

    def isItCompleted(self):
        if self.isRepeatable == "completed":
            return True
        else:
            return False

    def isItRepeatable(self):
        return self.isRepeatable

    def setSituation(self, newSituation):
        self.situation = newSituation

    def calculateTimeToBeDone(self):
        startTimeHours = int(self.timePeriod[0].strftime("%H")) * 60  # We convert hours to minutes
        endTimeHours = int(self.timePeriod[1].strftime("%H")) * 60  # We conver hours to minutes

        startTimeMinutes = int(self.timePeriod[0].strftime("%M"))
        endTimeMinutes = int(self.timePeriod[1].strftime("%M"))

        startTime = startTimeHours + startTimeMinutes
        endTime = endTimeHours + endTimeMinutes

        return (endTime - startTime)
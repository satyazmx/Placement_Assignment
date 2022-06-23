from AbstractEmployeeClass import *

class HourlyBasedEmployee(AbstractEmployeeClass):
    def __init__(self, firstName, lastName, department, workingHour, perHourRate):
        super().__init__(firstName, lastName, department)
        self.workingHour = workingHour
        self.perHourRate = perHourRate

    def getSalary(self):
        return self.workingHour * self.perHourRate
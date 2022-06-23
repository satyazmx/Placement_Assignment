from AbstractEmployeeClass import *

class FullTimeEmployee(AbstractEmployeeClass):
    def __init__(self, firstName, lastName, department, salary):
        super().__init__(firstName, lastName, department)
        self.salary = salary

    def getSalary(self):
        return self.salary
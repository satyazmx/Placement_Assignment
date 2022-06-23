from abc import ABC, abstractmethod

class AbstractEmployeeClass(ABC):
    def __init__(self, firstName, lastName, department):
        self.firstName = firstName
        self.lastName = lastName
        self.department = department

    @property
    def getFullName(self):
        return f"{self.firstName} {self.lastName}"

    @property
    def getDepartment(self):
        return self.department

    @abstractmethod
    def getSalary(self):
        pass
class EmployeePayRollClass:
    def __init__(self):
        self.employeeList = []

    def addEmployee(self, employee):
        self.employeeList.append(employee)

    def printEmployee(self):
        for employee in self.employeeList:
            fullName = f"{employee.getFullName}"
            salary = employee.getSalary()
            print(f"{fullName} \t ${salary}")

            #print(f"{employee.getFullName} \t ${employee.getSalary()}")
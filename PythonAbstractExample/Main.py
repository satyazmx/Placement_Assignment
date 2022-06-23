#from FullTimeEmployee import *
import FullTimeEmployee as fte
from HourlyBasedEmployee import *
from ContractBasedEmployee import *
from EmployeePayRollClass import *

payroll = EmployeePayRollClass()

payroll.addEmployee(fte.FullTimeEmployee('Satya', 'Thakur', 'Production', 60000))
payroll.addEmployee(fte.FullTimeEmployee('Diwakar', 'Kumar', 'HR', 65000))

payroll.addEmployee(HourlyBasedEmployee('Umesh', 'Singh', 'Production', 200, 50))
payroll.addEmployee(HourlyBasedEmployee('Jatin', 'Kumar', 'Testing', 150, 100))
payroll.addEmployee(HourlyBasedEmployee('Mahesh', 'Kumar', 'Production', 100, 150))

payroll.addEmployee(ContractBasedEmployee('Jatin', 'Kumar', 'HR', 3000))
payroll.addEmployee(ContractBasedEmployee('Mahesh', 'Kumar', 'Production', 4000))

payroll.printEmployee()
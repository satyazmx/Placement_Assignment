from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
class Laptop(Computer):
    pass

class Tablets(Computer):
    def process(self):
        print("Its running")
        
class Programmer:
    def work(self, tablet):
        print("Write Code")
        tablet.process()
        

#lappy = Laptop() => Gives Error ,As we can not create objects of Abstract class
#computer = Computer() => TypeError: Can't instantiate abstract class Computer with abstract method process
tab = Tablets()
programmer = Programmer()
programmer.work(tab)

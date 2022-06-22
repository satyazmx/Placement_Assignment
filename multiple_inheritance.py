class Phone:
    def __init__(self,price, brand,camera) -> None:
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
       
    def buy(self):
        print("Buying a Phone")
    
class Product:
    def buy(self):
        print("Buying a Product")

class SmartPhone(Phone,Product): ## Concept => Method Resolution Order(MRO)
    pass

s= SmartPhone(2500,'Nokia',12)
s.buy() # buy() of Phone class will be called, As SmartPhone class is inheriting from Phone first then Product

'''
O/P=>   Inside phone constructor
        Buying a Phone  
'''
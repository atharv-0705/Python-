# ENCAPSULATION
'''Modify the Car class to encapsulate the brand attribute,
making it private, and provide a getter method for it'''

class Car:
    def __init__(self, brand,model): #CONSTRACTOR
        self.__brand = brand         # "__" means make it Private so i can access it in Class bot not in Object, if we wanna to access through obj. use get func
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !" 
        
    def full_name(self): #FUNCTIONARTY
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
my_Tesla = ElectricCar("Tesla", "Model S", "85kWh")

#print(my_Tesla.__brand)                 Cannott access by object cuz it is Private attribute

print(my_Tesla.get_brand())
    
    
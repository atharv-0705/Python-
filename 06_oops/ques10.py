# MULTIPLE INHERITANCE
'''Create two classes Battery and Engine ,
and let the ElectricCar class inherite from both,
demonstrating multiple inheritance.'''


class Car:
   
    def __init__(self, brand,model): 
        self.__brand = brand
        self.__model = model
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
   
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery, Engine , Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model 3")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
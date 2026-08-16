# CLASS INHERITANCE and Isintance() function
'''Demostrate the use of isinstance() function to check
if my_tesla is an instance of ElectricCar and Car classes.'''


class Car:
   
    def __init__(self, brand,model): 
        self.__brand = brand
        self.__model = model
    
        
    def get_brand(self):
        return self.__brand + " !" 
        
    def full_name(self): 
        return f"{self.__brand} {self.__model}"  
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod   
    def General_description():     
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor."
    
    @property              
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
   
my_Tesla = ElectricCar("Tesla", "Model S", "85kWh")

isinstance(my_Tesla, ElectricCar)   # True  
isinstance(my_Tesla, Car)            # True 

      
print(isinstance(my_Tesla, Car))
print(isinstance(my_Tesla, ElectricCar))  

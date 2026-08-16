# PROPERTY DECORATOR
''' Use a property decorator in the Car class
to make attribute read-only'''


class Car:
   
    def __init__(self, brand,model): 
        self.__brand = brand
        self.__model = model
    
        
    def get_brand(self):
        return self.__brand + " !" 
        
    def full_name(self): 
        return f"{self.__brand} {self.__model}"  # Model attribute is also made private
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod   
    def General_description():     
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor."
    
    @property               # DECORATOR TO MAKE ATTRIBUTE READ-ONLY
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
   
#my_Tesla = ElectricCar("Tesla", "Model S", "85kWh")

my_car = Car("Tata", "Safari")
# my_car.model = "City"        will give error as model is read-only now
      
print(my_car.model)
# print(my_car.model())   will give error as model is private attribute now
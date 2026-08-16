# STATIC METHOD
'''Add a static method to the Car class 
that returns a generak description of a Car.'''


class Car:
   
    def __init__(self, brand,model): 
        self.__brand = brand
        self.model = model
    
        
    def get_brand(self):
        return self.__brand + " !" 
        
    def full_name(self): 
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod    # DECORATOR TO DEFINE STATIC METHOD
    def General_description():      # donot use SELF parameter in static method
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor."
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
   
my_Tesla = ElectricCar("Tesla", "Model S", "85kWh")
Car("Tata", "Safari")
Car("Tata", "Nexon")
ElectricCar("Tesla","Model x", "90kWh")


# print(my_car.General_description())            object cannot access static method directly
print(ElectricCar.General_description())         # object of child class can access static method of parent class
print(Car.General_description())                  # object of parent class can access static method of parent class

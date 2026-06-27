# class variables
'''Add a class variable to Car that keeps track of the number of cars created.'''


class Car:
    total_car = 0
    
    
    def __init__(self, brand,model): #CONSTRACTOR
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " !" 
        
    def full_name(self): #FUNCTIONARTY
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
   
my_Tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_Tesla.__brand)
print(my_Tesla.fuel_type())

Car("Tata", "Safari")
Car("Tata", "Nexon")


print(Car.total_car)
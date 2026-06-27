# POLYMORPHISM
'''Demonstrate polymorphism by defining a method
fuel_type in both Car and ElectricCar classes,
but with different behaviors.'''


class Car:
    def __init__(self, brand,model): #CONSTRACTOR
        self.__brand = brand
        self.model = model
        
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

safari = Car("Tata", "Safari")
print(safari.fuel_type())
    
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
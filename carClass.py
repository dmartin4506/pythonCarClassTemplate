class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def description(self):
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        return f"This car has {self.odometer} miles on it."
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage 
        else:
            print("You cant roll back negative miles!")
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer += miles
        else:
            print("you cant add negative miles!")


my_car = Car(make="Toyota", model="Corolla", year="2020")
my_car.update_odometer(15000)
print(my_car.read_odometer())

print(my_car.description())
my_car.increment_odometer(2000)
print(my_car.read_odometer())
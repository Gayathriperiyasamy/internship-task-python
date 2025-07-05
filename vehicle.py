class Vehicle:
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__("Car")
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__("Bike")
        self.brand = brand

car = Car("Honda")
bike = Bike("Yamaha")
print(f"{car.type} Brand: {car.brand}")
print(f"{bike.type} Brand: {bike.brand}")

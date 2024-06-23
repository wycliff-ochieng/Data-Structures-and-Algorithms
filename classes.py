class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(f"The car is a{self.year} {self.make} {self.model}")
    def read_odometer(self):
        print(f"This car {self.odometer_reading} miles on it")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot rool down an odometer")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

vehicle = Car("Benz", "E250", "2020")
vehicle.read_odometer()
vehicle.get_descriptive_name()
          

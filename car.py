class ModCar():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odoMeterReading = 0
    
    def getDescriptive(self):
        longName = (f"{self.year} {self.make} {self.model}")
        return longName.title()
    
    def readOdometer(self):
        print(f"This car has {self.odoMeterReading} miles on it.")
    
    def updateOdometer(self, mileage):
        if mileage >= self.odoMeterReading:
            self.odoMeterReading = mileage
        else:
            print('You cannot roll back an odometer!')
    
    def incrementOdometer(self, miles):
        self.odoMeterReading += miles
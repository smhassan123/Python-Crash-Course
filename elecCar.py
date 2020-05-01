from car import ModCar

class ModBattery():
    def __init__(self, batterySize=70):
        self.battery = batterySize
        
    def describeBattery(self):
        print(f"This car has {self.battery}-kWh battery")
    
        

class ModElectricCar(ModCar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batt = ModBattery()
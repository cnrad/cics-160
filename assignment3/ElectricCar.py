from Car import Car

class ElectricCar(Car):
    def __init__(self, makeAndModel="None assigned", numberOfDoors=4, maximumNumberOfPassengers=5, batterySize=-1) -> None:
        super().__init__(makeAndModel, numberOfDoors, maximumNumberOfPassengers)
        self.batterySize = batterySize

    def __str__(self):
        defaultStr = super().__str__()
        return f'{defaultStr}\nBattery size: {self.batterySize}'

    def getBatterySize(self):
        return self.batterySize
    
    def setBatterySize(self, newBatterySize):
        self.batterySize = newBatterySize

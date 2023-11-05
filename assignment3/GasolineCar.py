from Car import Car

class GasolineCar(Car):
    def __init__(self, makeAndModel="None assigned", numberOfDoors=4, maximumNumberOfPassengers=5, gasTankSize=-1) -> None:
        super().__init__(makeAndModel, numberOfDoors, maximumNumberOfPassengers)
        self.gasTankSize = gasTankSize

    def __str__(self):
        defaultStr = super().__str__()
        return f'{defaultStr}\nGas tank size: {self.gasTankSize}'

    def getGasTankSize(self):
        return self.gasTankSize
        
    def setGasTankSize(self, newGasTankSize):
        self.gasTankSize = newGasTankSize
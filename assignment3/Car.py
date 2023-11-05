class Car:
    def __init__(self, makeAndModel="None assigned", numberOfDoors=4, maximumNumberOfPassengers=5):
        self.makeAndModel = makeAndModel
        self.numberOfDoors = numberOfDoors
        self.maximumNumberOfPassengers = maximumNumberOfPassengers

    def __str__(self):
        return f'Make and Model: {self.makeAndModel}\nNumber of doors: {self.numberOfDoors}\nMaximum number of passengers: {self.maximumNumberOfPassengers}'
    
    def setMakeAndModel(self, model):
        self.makeAndModel = model

    def getMakeAndModel(self):
        return self.makeAndModel

    def getMaximumNumberOfPassengers(self):
        return self.maximumNumberOfPassengers
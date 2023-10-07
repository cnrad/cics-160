from Car import Car

class GasolineCar(Car):
    def __init__(self, make_model="None assigned", num_doors=4, max_passengers=5, gas_tank_size=-1) -> None:
        super().__init__(make_model, num_doors, max_passengers)
        self.gas_tank_size = gas_tank_size
        # pass

    def __str__(self):
        return super().__str__() + f'\nGas Tank Size: {self.gas_tank_size}\nELECTRIC CAR'

    def set_gas_tank_size(self, new_size):
        self.gas_tank_size = new_size

    def get_gas_tank_size(self):
        return self.gas_tank_size

electricCar1 = GasolineCar()
electricCar1.set_gas_tank_size(25)
print(electricCar1)
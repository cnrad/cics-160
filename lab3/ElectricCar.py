from Car import Car

class ElectricCar(Car):
    def __init__(self, make_model="None assigned", num_doors=4, max_passengers=5) -> None:
        super().__init__(make_model, num_doors, max_passengers)
        # pass

    def __str__(self):
        return super().__str__() + "\nELECTRIC CAR"

electricCar1 = ElectricCar()
electricCar1.set_make_model("Toyota Prius")
print(electricCar1)
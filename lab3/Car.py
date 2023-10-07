class Car:
    def __init__(self, make="None assigned", doors=4, passengers=5):
        self.make_model = make
        self.num_doors = doors
        self.max_passengers = passengers

    def __str__(self):
        return f'Make and Model:{self.make_model}\nNumber of doors: {self.num_doors}\nMaximum number of passengers: {self.max_passengers}'
    
    def set_make_model(self, model):
        self.make_model = model

    def get_make_model(self):
        return self.make_model

    def set_num_doors(self, num):
        self.num_doors = num

    def get_num_doors(self):
        return self.num_doors

    def set_max_passengers(self, num):
        self.max_passengers = num

    def get_max_passengers(self):
        return self.max_passengers


if __name__ == "__main__":
    car1 = Car()

    car1.set_make_model("Dodge Dart")
    car1.set_num_doors(5)
    car1.set_max_passengers(7)

    print(car1.get_make_model())
    print(car1.get_num_doors())
    print(car1.get_max_passengers())
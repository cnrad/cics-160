import unittest
from LinkedList import LinkedList
from Car import Car
from GasolineCar import GasolineCar
from ElectricCar import ElectricCar

class TestLinkedList(unittest.TestCase):
    def test_LinkedListInsertMethod(self):
        list = LinkedList()
        list.add(GasolineCar("Honda", 4, 4, 10))
        list.add(ElectricCar("Tesla", 4, 5, 4))
        carToInsert = Car("Toyota", 4, 4)
        list.insert(0, carToInsert)
        # Checks of the data at the position of the list matches the data we inserted at that position
        self.assertEqual(list.__getitem__(0), carToInsert)

    def test_LinkedListDeleteMethod(self):
        list = LinkedList()
        list.add(ElectricCar("Tesla", 4, 5, 4))

        # This object will be at index 1
        carToDelete = GasolineCar("Honda", 4, 4, 10)
        list.add(carToDelete)
        list.add(Car("Toyota", 4, 4))
        list.delete(1)
        # Checks if the data at the index that the car was inserted at ISN'T equal to the car, since it was deleted
        self.assertNotEqual(list.__getitem__(1), carToDelete)

if __name__ == "__main__":
    unittest.main()
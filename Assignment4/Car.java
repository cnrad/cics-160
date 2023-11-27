package Assignment4;
public class Car {
    String makeAndModel;
    int maximumNumberOfPassengers;
    int numberOfDoors;

    public Car(String makeModel, int numPassengers, int numDoors) {
        makeAndModel = makeModel;
        maximumNumberOfPassengers = numPassengers;
        numberOfDoors = numDoors;
    }

    public void setMakeAndModel(String m) {
        makeAndModel = m;
    }

    public String getMakeAndModel() {
        return makeAndModel;
    }

    public void setMaximumNumberOfPassengers(int m) {
        maximumNumberOfPassengers = m;
    }

    public int getMaximumNumberOfPassengers() {
        return maximumNumberOfPassengers;
    }

    public void setNumberOfDoors(int m) {
        numberOfDoors = m;
    }

    public int getNumberOfDoors() {
        return numberOfDoors;
    }

    public String toString() {
        return String.format("Make and model: %s\nMaximum number of passengers: %d\nNumber of doors: %d\n", makeAndModel, maximumNumberOfPassengers, numberOfDoors);
    }
}

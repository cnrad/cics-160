package Assignment4;
public class ElectricCar extends Car {
    double batterySize;

    public ElectricCar(String makeModel, int numPassengers, int numDoors, double battSize) {
        super(makeModel, numPassengers, numDoors);
        batterySize = battSize;
    }

    public void setBatterySize(double b) {
        batterySize = b;
    }

    public double getBatterySize() {
        return batterySize;
    }

    public String toString() {
        return super.toString() + "Battery size: " + batterySize;
    }
}


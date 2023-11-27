package Assignment4;
public class GasolineCar extends Car {
    double gasTankSize;

    public GasolineCar(String makeModel, int numPassengers, int numDoors, double tankSize) {
        super(makeModel, numPassengers, numDoors);
        gasTankSize = tankSize;
    }

    public void setGasTankSize(double g) {
        gasTankSize = g;
    }

    public double getGasTankSize() {
        return gasTankSize;
    }

    public String toString() {
        return super.toString() + "Gas tank size: " + gasTankSize;
    }
}


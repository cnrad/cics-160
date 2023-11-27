package Assignment4;
import java.util.ArrayList;

public class FleetOfCars {
    ArrayList<Car> fleet;
    int fleetSize;

    public FleetOfCars() {
        fleet = new ArrayList<Car>();
        fleetSize = 0;
    }

    public FleetOfCars search(String s) {
        FleetOfCars matchedCars = new FleetOfCars();
        
        for(int i = 0; i < fleetSize; i++) {
            Car currentCar = fleet.get(i);
            if(s.equals(currentCar.getMakeAndModel())) {
                matchedCars.add(currentCar);
            }
        }

        return matchedCars;
    }

    public void add(Car car) {
        fleet.add(car);
        fleetSize += 1;
    } 

    public int getSize() {
        return fleetSize;
    }

    public void delete(int i) {
        fleet.remove(i);
        fleetSize -= 1;
    }

    public Car get(int i) {
        return fleet.get(i);
    }

    public String toString() {
        String fleetString = "";

        for(int i = 0; i < fleetSize; i++) {
            fleetString += "Car " + i + " --------\n" + fleet.get(i).toString() + "\n";
        }

        return fleetString;
    }
}

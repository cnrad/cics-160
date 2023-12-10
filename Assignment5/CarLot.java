import java.util.ArrayList;
import java.util.List;

public class CarLot {
    Queue<Car> gasQueue;
    Queue<Car> hybridQueue;
    Queue<Car> electricQueue;

    public CarLot() {
        gasQueue = new Queue<Car>();
        hybridQueue = new Queue<Car>();
        electricQueue = new Queue<Car>();
    }

    public boolean addCar(Car car) {
        if (car.getPowerSource() == 1) {
            gasQueue.enqueue(car);
            return true;
        } else if (car.getPowerSource() == 2) {
            hybridQueue.enqueue(car);
            return true;
        } else if (car.getPowerSource() == 3) {
            electricQueue.enqueue(car);
            return true;
        } else {
            return false;
        }
    }

    public List<Car> processRequests(CarRequests carReqs) {
        List<Car> carResult = new ArrayList<Car>();

        while (carReqs.hasPendingRequests()) {
            int currCarType = carReqs.getRequest();

            if (currCarType == 1) {
                if(!gasQueue.isEmpty()) { 
                    carResult.add(gasQueue.dequeue()); 
                } else { 
                    carResult.add(new Car(0, 0, 0));
                } 
            } else if (currCarType == 2) {
                if(!hybridQueue.isEmpty()) { 
                    carResult.add(hybridQueue.dequeue()); 
                } else { 
                    carResult.add(new Car(0, 0, 0));
                } 
            } else if (currCarType == 3) {
                if(!electricQueue.isEmpty()) { 
                    carResult.add(electricQueue.dequeue()); 
                } else { 
                    carResult.add(new Car(0, 0, 0));
                } 
            }
        }

        return carResult;
    }
}

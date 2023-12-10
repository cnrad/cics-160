import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertArrayEquals;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class CarLotTests {
    @Test
    public void testCarLotConstructor() {
        CarLot carLot = new CarLot();
        
        assertFalse(carLot.addCar(new Car(0, 0, 0)));
    }

    @Test
    public void testCarLotAddCarSuccess() {
        CarLot carLot = new CarLot();
        assertTrue(carLot.addCar(new Car(2, 2, 2)));
    }

    @Test
    public void testCarLotAddCarFalse() {
        CarLot carLot = new CarLot();
        assertFalse(carLot.addCar(new Car(0, 0, 0)));
    }

    @Test
    public void testCarProcessRequests() {
        CarLot carLot = new CarLot();
        CarRequests carReqs = new CarRequests();

        List<Car> addedCars = new ArrayList<Car>();

        addedCars.add(new Car(10, 1, 3.33f));
        addedCars.add(new Car(11, 1, 3.33f));
        addedCars.add(new Car(12, 2, 2.33f));
        addedCars.add(new Car(13, 2, 2.33f));

        carLot.addCar(addedCars.get(0));
        carLot.addCar(addedCars.get(1));
        carLot.addCar(addedCars.get(2));
        carLot.addCar(addedCars.get(3));

        carReqs.addRequest(1);
        carReqs.addRequest(1);
        carReqs.addRequest(2);
        carReqs.addRequest(2);

        // Should remove all cars from queue and return the "same" list as addedCars
        assertArrayEquals(carLot.processRequests(carReqs).toArray(), addedCars.toArray());
    }
}

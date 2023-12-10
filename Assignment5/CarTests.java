import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CarTests {
    @Test
    public void testCarConstructor() {
        Car car = new Car(38, 1, 3.14f);
        assertEquals(car.getPricePerDay(), 3.14f, 0.01);
    }

    @Test
    public void testCarGetId() {
        Car car = new Car(38, 1, 3.14f);
        assertEquals(car.getId(), 38, 0.01);
    }

    @Test
    public void testCarSetId() {
        Car car = new Car(38, 1, 3.14f);
        car.setId(50);
        assertEquals(car.getId(), 50, 0.01);
    }

    @Test
    public void testCarGetPowerSource() {
        Car car = new Car(20, 3, 1.28f);
        assertEquals(car.getPowerSource(), 3, 0.01);
    }

    @Test
    public void testCarSetPowerSource() {
        Car car = new Car(20, 3, 1.28f);
        car.setPowerSource(1);
        assertEquals(car.getPowerSource(), 1, 0.01);
    }

    @Test
    public void testCarGetPricePerDay() {
        Car car = new Car(20, 3, 1.28f);
        assertEquals(car.getPricePerDay(), 1.28f, 0.01);
    }

    @Test
    public void testCarSetPricePerDay() {
        Car car = new Car(20, 3, 1.28f);
        car.setPricePerDay(20.4f);
        assertEquals(car.getPricePerDay(), 20.4f, 0.01);
    }
}

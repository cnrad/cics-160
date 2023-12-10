import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class MaxFinderTest {
    @Test
    public void testFindMaximum() {
        double[] A = {100, 0, 9, 22, -4, 6, 999};
        assertEquals(MaxFinder.findMaximum(A), 999, 0.01);
    }

    @Test
    public void testFindMaximumWithBiggestFirst() {
        double[] A = {100, 0, 9, 22, -4, 6};
        assertEquals(MaxFinder.findMaximum(A), 100, 0.01);
    }

    @Test
    public void testFindMaximumWithOnlyOneElement() {
        double[] A = {57};
        assertEquals(MaxFinder.findMaximum(A), 57, 0.01);
    }
}

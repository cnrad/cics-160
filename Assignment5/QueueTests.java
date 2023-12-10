import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class QueueTests {
    @Test
    public void testCheckConstructor() {
        Queue<Integer> testQueue = new Queue<Integer>();
        testQueue.enqueue(1);
        assertEquals(testQueue.peek(), 1, 0.01);
    }

    @Test
    public void testEnqueueTwoItems() {
        Queue<Integer> testQueue = new Queue<Integer>();
        testQueue.enqueue(13);
        testQueue.enqueue(25);
        assertEquals(testQueue.peek(), 13, 0.01);
    }

    @Test
    public void testDequeueFirstItem() {
        Queue<Integer> testQueue = new Queue<Integer>();
        testQueue.enqueue(20);
        testQueue.enqueue(45);
        testQueue.dequeue();
        assertEquals(testQueue.peek(), 45, 0.01);
    }

    @Test
    public void testPeekThirdItem() {
        Queue<Integer> testQueue = new Queue<Integer>();
        testQueue.enqueue(5);
        testQueue.enqueue(134);
        testQueue.enqueue(48);
        testQueue.dequeue();
        testQueue.dequeue();
        assertEquals(testQueue.peek(), 48, 0.01);
    }

    @Test
    public void testIsEmptyWhenNot() {
        Queue<Integer> testQueue = new Queue<Integer>();
        testQueue.enqueue(45);
        testQueue.enqueue(14);
        assertFalse(testQueue.isEmpty());
    }

    @Test
    public void testIsEmptyWhenIs() {
        Queue<Integer> testQueue = new Queue<Integer>();
        testQueue.enqueue(54);
        testQueue.enqueue(3);
        testQueue.dequeue();
        testQueue.dequeue();
        assertTrue(testQueue.isEmpty());
    }
}

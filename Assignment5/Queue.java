import java.util.ArrayList;
import java.util.List;

public class Queue<T> {
    private List<T> queue;

    public Queue() {
        queue = new ArrayList<T>();
    }

    public void enqueue(T item) {
        queue.add(item);
    }

    public T dequeue() {
        return queue.remove(0);
    }

    public T peek() {
        return queue.get(0);
    }

    public boolean isEmpty() {
        return queue.size() == 0;
    }
}

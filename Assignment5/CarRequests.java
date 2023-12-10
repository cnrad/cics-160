public class CarRequests {
    Queue<Integer> requests;

    public CarRequests() {
        requests = new Queue<Integer>();
    }

    public void addRequest(int x) {
        requests.enqueue(x);
    }

    public int getRequest() {
        return requests.dequeue();
    }

    public boolean hasPendingRequests() {
        return !requests.isEmpty();
    }
}

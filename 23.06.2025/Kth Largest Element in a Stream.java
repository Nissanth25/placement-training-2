class KthLargest {
    PriorityQueue<Integer> heap = new PriorityQueue<>();
    private final int k;
    public KthLargest(int k, int[] nums) {
        for (int num: nums) {
            heap.add(num);
            if (heap.size() > k) {
                heap.poll();
            }
        }
        this.k = k;
    }
    
    public int add(int val) {
        if (heap.size() < k) {
            heap.add(val);
        } else if (val > heap.peek()) {
            heap.poll();
            heap.add(val);
        }
        return heap.peek();
    }
    
}

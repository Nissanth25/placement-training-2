class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        if (root == null) return -1;

        Set<Integer> uniqueVals = new HashSet<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        traverse(root, uniqueVals, maxHeap);

        if (maxHeap.size() < 2)
            return -1;

        return maxHeap.peek(); 
    }
    private void traverse(TreeNode node, Set<Integer> uniqueVals, PriorityQueue<Integer> maxHeap) {
        if (node == null) return;

        if (!uniqueVals.contains(node.val)) {
            uniqueVals.add(node.val);
            maxHeap.offer(node.val);

            if (maxHeap.size() > 2) {
                maxHeap.poll(); 
            }
        }

        traverse(node.left, uniqueVals, maxHeap);
        traverse(node.right, uniqueVals, maxHeap);
    }
}

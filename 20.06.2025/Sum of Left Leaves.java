class Solution {
    int sum = 0;
    public int sumOfLeftLeaves(TreeNode root) {
        dfs(root);
        return sum;
    }

    public void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        if (node.left != null && node.left.left == null && node.left.right == null) {
            sum += node.left.val;
        } else {
            dfs(node.left);
        }
        dfs(node.right);
    }
}

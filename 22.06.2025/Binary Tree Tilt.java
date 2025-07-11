class Solution {
    int findSum(TreeNode root){
        if(root==null) return 0;
        return root.val + findSum(root.left) + findSum(root.right);
    }
    public int findTilt(TreeNode root) {
        if(root==null) return 0;
        
        int left = findTilt(root.left);
        int right = findTilt(root.right);
        
        return Math.abs(findSum(root.left)-findSum(root.right))+left+right;
        
    }
}

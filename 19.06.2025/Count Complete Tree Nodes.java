class Solution {
    int count = 0;
    public int countNodes(TreeNode root) {
                
        if(root==null)  return 0;

        return count(root);
    }

    public static int count(TreeNode node){
        
        if(node==null) return 0;


        if(node.left==null && node.right!=null) return 0;
        
        int left = count(node.left);
        int right = count(node.right);

        

        return 1 + left + right;
    }
}

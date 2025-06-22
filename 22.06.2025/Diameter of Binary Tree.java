class Solution {

    int max=0;
    public int diameterOfBinaryTree(TreeNode root) {

        heightChecker(root);
        return max;
    }

    public  int heightChecker(TreeNode root)
    {
        if(root==null)
        return 0;

   int left=heightChecker(root.left);
   int right=heightChecker(root.right);

   max=Math.max((left+right),max);

   return 1+Math.max(left,right);
    }
}

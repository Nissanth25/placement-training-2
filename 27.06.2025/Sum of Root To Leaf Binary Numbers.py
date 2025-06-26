class Solution(object):
    def __init__(self):
        self.ans = 0

    def search(self, node, pre=0):  
        if node.left is None and node.right is None:  
            self.ans += pre * 2 + node.val
            
        if node.left:  
            self.search(node.left, pre * 2 + node.val)
        if node.right:  
            self.search(node.right, pre * 2 + node.val)

    def sumRootToLeaf(self, root):
        self.search(root, 0)
        return self.ans

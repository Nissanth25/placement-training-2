class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        p, children = [cloned], []
        while p:
            for x in p:
                if x.val == target.val:
                    return x
                if x.left:
                    children.append(x.left)
                if x.right:
                    children.append(x.right)
            p, children = children, []

        return None

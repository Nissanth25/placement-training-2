class Solution(object):
    def heightChecker(self, heights):
        c=0
        a=sorted(heights)
        for i in range(len(heights)):
            if a[i]!=heights[i]:
                c+=1
        return c        

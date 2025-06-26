class Solution(object):
    def prefixesDivBy5(self, nums):
        x=0
        l=[]
        for i in range(len(nums)):
            x=(2*x)+nums[i]
            l.append(True) if x%5==0 else l.append(False)
        return l



        

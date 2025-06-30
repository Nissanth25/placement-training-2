class Solution(object):
    def minSubsequence(self, nums):
        a=nums.sort(reverse=True)
        for x in range(len(nums)):
            b=nums[0:x+1]
            c=nums[x+1:len(nums)]
            if sum(b)>sum(c):
                return b
        

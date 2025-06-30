class Solution:
    def kLengthApart(self, nums, k) :
        if nums[0]==1:
            prev=0
        else:
            prev=-1
            
        for i in range(1,len(nums)):
            if nums[i]==1:
                if prev!=-1 and (i-prev-1)<k:
                    return False
                else:
                    prev = i
        return True
  

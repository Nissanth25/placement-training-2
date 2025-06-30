class Solution(object):
    def minStartValue(self, nums):
        start_value = 1

        while start_value:
            if self.check(start_value, nums):
                return start_value
            start_value += 1
    
    
    def check(self, start_value, nums):
        temp = start_value
        for num in nums:
            temp += num
            if temp < 1:
                return False
            
        return True

class Solution(object):
    def sortByBits(self, arr):

        def count_ones(x):    
            return bin(x).count('1') 

        arr.sort(key=lambda x: (count_ones(x), x))  
        return arr                                  

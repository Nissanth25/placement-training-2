class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        j = len(arr)-1
        while(i < j):
            if(arr[i] == 0):
                arr.insert(i+1,0)
                arr.pop()
                i += 1
            i += 1
            
        

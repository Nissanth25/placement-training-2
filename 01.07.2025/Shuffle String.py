class Solution(object):
    def restoreString(self, s, indices):
        num = 0
        res = [None] * len(s) 
        while num < len(s):
            res[indices[num]] = s[num]
            num += 1
        return ''.join(res)

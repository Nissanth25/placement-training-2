class Solution(object):
    def reformat(self, s):
        l, d = [], []
        for char in s:
            if char.isalpha():
                l.append(char)
            else:
                d.append(char)
        
        if abs(len(l) - len(d)) > 1:
            return ""
        
        res = []
        start_with_letter = len(l) > len(d)
        while l or d:
            if start_with_letter:
                res.append(l.pop())
            else:
                res.append(d.pop())
            start_with_letter = not start_with_letter
        
        return ''.join(res)

class Solution(object):
    def removeDuplicates(self, chars):
        if len(chars) == 1:
            return chars

        s = []

        for ch in chars:
            if not s or s[-1] != ch:
                s.append(ch)
            else:
                s.pop()
        res = ""
        while s:
            res = s.pop() + res

        return res

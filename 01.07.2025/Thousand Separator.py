class Solution(object):
    def thousandSeparator(self, n):
        n = str(n)
        s = ""
        count = 0

        for i in n[::-1]:
            if count == 3:
                s+= "."
                count = 0
            count += 1
            s += i

        return s[::-1]

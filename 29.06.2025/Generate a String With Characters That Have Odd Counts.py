class Solution(object):
    def generateTheString(self, n):

        if n % 2 == 1:
            return "a" * n
        return "a" * (n-1) + "b"


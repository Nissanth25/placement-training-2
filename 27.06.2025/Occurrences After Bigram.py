class Solution:
    def findOcurrences(self, text, first, second):
        third = []
        sen = list(text.split())
        for i in range(1, len(sen)-1):
            if sen[i-1] == first and sen[i] == second:
                third.append(sen[i+1])
        return third

class Solution(object):
    def average(self, salary):
        salary.sort()
        salary.pop(0)
        salary.pop(-1)
        return sum(salary)*1.0/len(salary)

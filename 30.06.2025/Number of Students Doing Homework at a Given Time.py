class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        res = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                res += 1
        return res

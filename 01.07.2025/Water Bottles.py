class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):

        n = numBottles
        m = numExchange
        count = 0
        while n >= m:
            n -= m
            n += 1
            count += m
        return count + n

class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        sum = 0
        while n != 0:
            lastDigit = n % 10
            prod *= lastDigit
            sum += lastDigit
            n = n // 10
        return prod - sum

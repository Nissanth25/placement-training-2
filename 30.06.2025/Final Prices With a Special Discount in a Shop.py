class Solution(object):
    def finalPrices(self, prices):

        stack=[]

        for i in range(len(prices)):
            current= prices[i]

            while stack and prices[stack[-1]]>= current:
                prev_index= stack.pop()
                prices[prev_index]-= current

            stack.append(i)

        return prices

class Solution(object):
    def lastStoneWeight(self, stones):

        if len(stones)==1:
            return stones[0]
        if len(stones)==0:
            return 0
        x=max(stones)
        stones.remove(x)

        y=max(stones)
        stones.remove(y)

        if (x-y)!=0:
            stones.append((x-y))

        return self.lastStoneWeight(stones)
     
        

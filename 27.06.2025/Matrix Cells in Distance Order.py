class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):     
        ans = [[r,c] for c in range(C) for r in range(R)]
        return sorted(ans, key = lambda ans: abs(ans[0]- r0) +abs(ans[1]- c0))

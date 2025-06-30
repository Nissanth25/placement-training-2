class Solution(object):
    def mostVisited(self, n, rounds):
        d = {i:0 for i in range(1,n+1)}
        for i in range(len(rounds)-1):
            start = rounds[i]
            end = rounds[i+1]
            while start != end:
                if start > n:
                    start = 1
                else:
                    d[start]+=1
                    start+=1
        else:
            d[end]+=1
        l = sorted(d.items(),key = lambda x: x[1])
        return [i[0] for i in l if i[1] == l[-1][1]]

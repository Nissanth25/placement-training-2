class Solution(object):
    def minTimeToVisitAllPoints(self, points):

        n = len(points)
        time = 0
        for i in range(1,n) :
            time += max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
        return time
        

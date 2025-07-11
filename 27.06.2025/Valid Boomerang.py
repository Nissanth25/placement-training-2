class Solution(object):
    def isBoomerang(self, points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]      
        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return area != 0
        

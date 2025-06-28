class Solution(object):
    def checkStraightLine(self, coordinates):
        point1 = coordinates[0]
        point2 = coordinates[1]
        
        deltaX = point2[0] - point1[0]
        deltaY = point2[1] - point1[1]
        
        for i in range(2, len(coordinates)):
            currentPoint = coordinates[i]
            
            currentDeltaX = currentPoint[0] - point1[0]
            currentDeltaY = currentPoint[1] - point1[1]
            
            if deltaX * currentDeltaY != deltaY * currentDeltaX:
                return False
        
        return True

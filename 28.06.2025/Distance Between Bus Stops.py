class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start>destination:
            start,destination=destination,start
        if sum(distance[start:destination])<sum(distance[destination:])+sum(distance[:start]):
            return sum(distance[start:destination])
        else:
            return sum(distance[destination:])+sum(distance[:start])

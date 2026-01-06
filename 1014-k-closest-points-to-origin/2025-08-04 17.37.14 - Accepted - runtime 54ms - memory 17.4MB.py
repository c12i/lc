class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        sorted_points = sorted(points, key = lambda k: self.getDistanceFromOrigin(k[0], k[1]))

        return sorted_points[:k]

    
    def getDistanceFromOrigin(self, x, y):
        return math.sqrt(((x - 0)**2) + ((y - 0)**2))

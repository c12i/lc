class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        low = 1
        high = position[-1] - position[0]

        def canPlaceAllBalls(distance):
            prev = position[0]
            balls = 1

            for i in range(1, len(position)):
                if position[i] - prev >= distance:
                    balls += 1
                    prev = position[i]
                    if balls == m:
                        return True
            return False
            
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if canPlaceAllBalls(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
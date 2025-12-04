class Solution(object):
    def minEatingSpeed(self, piles, h):
        def canFinish(speed):
            hours = 0
            for pile in piles:
                time_for_pile = (pile + speed - 1) // speed
                hours += time_for_pile
            return hours <= h

        low, high = 1, max(piles)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if canFinish(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
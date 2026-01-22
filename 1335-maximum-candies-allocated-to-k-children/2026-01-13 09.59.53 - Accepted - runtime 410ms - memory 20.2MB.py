class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def is_feasible(mc):
            children = 0
            for c in candies:
                children += (c // mc)
            return children >= k

        low, high = 1, max(candies)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if is_feasible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
        
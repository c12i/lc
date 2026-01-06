class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def is_feasible(capacity):
            day_count = 1
            rem = capacity
            for i in range(len(weights)):
                if rem and rem >= weights[i]:
                    rem -= weights[i]
                else:
                    day_count += 1
                    rem = capacity - weights[i]
            return day_count <= days

        low, high = max(weights), sum(weights)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        
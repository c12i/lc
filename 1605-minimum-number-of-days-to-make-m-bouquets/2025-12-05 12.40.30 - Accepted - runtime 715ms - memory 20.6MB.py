class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        # added post
        if len(bloomDay) < m * k:
            return -1

        def is_feasible(days):
            count = 0
            flowers = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= days:
                    flowers += 1
                    if flowers == k:
                        count += 1
                        flowers = 0
                else:
                    flowers = 0
            return count >= m 

        low, high = min(bloomDay), max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        
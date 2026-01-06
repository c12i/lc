class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        low, high = 1, price[-1] - price[0]

        def is_feasible(tastiness):
            count = 1
            prev = price[0]

            for i in range(1, len(price)):
                if price[i] - prev >= tastiness:
                    prev = price[i]
                    count += 1
                    if count == k:
                        return True
            return False

        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if is_feasible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
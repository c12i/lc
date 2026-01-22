class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        def is_feasible(q):
            stores = 0
            for ptq in quantities:
                stores += math.ceil(ptq / float(q))
            return stores <= n

        low, high = 1, max(quantities)
        ans = high
        while low <= high:
            mid = (low + high) // 2

            if is_feasible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
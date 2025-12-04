class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        def is_feasible(time):
            # check how many cars can be repaired at this time?
            cars_repaired = 0
            for r in ranks:
                cars_repaired += int((time / r) ** 0.5)
            return cars_repaired >= cars

        low, high = 1, (max(ranks) * (cars**2))
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if is_feasible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
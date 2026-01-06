class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 1
        high = x

        while low <= high:
            mid = (high + low) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1

        return high

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2
            # since k*(k+1)/2 grows quadratically
            coin = mid * (mid + 1) // 2

            if coin == n:
                return mid
            elif coin < n:
                left = mid + 1
            else:
                right = mid - 1

        return right

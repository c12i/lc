class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res = res ^ n
            n = n >> 1
        return res
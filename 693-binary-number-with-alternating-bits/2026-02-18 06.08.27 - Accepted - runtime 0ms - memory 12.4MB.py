class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = -1

        while n > 0:
            curr = n & 1
            if prev == curr:
                return False
            prev = curr
            n = n >> 1

        return True
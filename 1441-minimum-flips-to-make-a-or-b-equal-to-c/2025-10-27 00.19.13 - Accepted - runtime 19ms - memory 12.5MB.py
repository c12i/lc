class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0

        n = (a | b) ^ c
        while n:
            count += n & 1
            n = n >> 1

        n = (a & b) & ~c
        while n:
            count += n & 1
            n = n >> 1

        return count
        
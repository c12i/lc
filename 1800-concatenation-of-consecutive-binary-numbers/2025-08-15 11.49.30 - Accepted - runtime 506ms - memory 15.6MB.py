
class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        num = 0
        bit_len = 0

        for d in range(1, n + 1):
            # increase bit length if d is power of 2
            if d & (d - 1) == 0:
                bit_len += 1
            num = ((num << bit_len) | d) % MOD

        return num

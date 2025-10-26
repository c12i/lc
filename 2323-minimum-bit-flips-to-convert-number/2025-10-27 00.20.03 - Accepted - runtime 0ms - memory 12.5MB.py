class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        xor = start ^ goal
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1
        return count
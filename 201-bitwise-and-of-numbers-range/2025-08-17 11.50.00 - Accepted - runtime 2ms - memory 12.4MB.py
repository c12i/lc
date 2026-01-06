class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shifts = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shifts += 1
        return left << shifts
        
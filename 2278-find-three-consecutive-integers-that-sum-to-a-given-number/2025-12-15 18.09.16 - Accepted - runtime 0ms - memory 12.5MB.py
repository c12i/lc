class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        x = num // 3
        if (x + (x - 1) + (x + 1)) == num:
            return [x - 1, x, x + 1]
        return []
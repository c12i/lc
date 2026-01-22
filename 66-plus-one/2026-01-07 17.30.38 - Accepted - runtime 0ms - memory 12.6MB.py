class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(d) for d in str(int("".join([str(n) for n in digits])) + 1)]
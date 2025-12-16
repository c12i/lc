class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        i = len(num) - 1

        while i >= 0:
            number = int(num[i])
            if number % 2 != 0:
                return num[:i+1]
            i -= 1

        return ""
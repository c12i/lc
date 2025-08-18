class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_signed = x < 0

        digits = []

        temp = abs(x)

        while temp > 0:
            digits.append(temp % 10)
            temp = temp // 10

        digits.reverse()

        l = len(digits) - 1
        res = 0

        while digits:
            digit = digits.pop()
            res += digit * (10 ** l)
            l -= 1

        if res > 2 ** 31:
            return 0

        return -res if is_signed else res

        
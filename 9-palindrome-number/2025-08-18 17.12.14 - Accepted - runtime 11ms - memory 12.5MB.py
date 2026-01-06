class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        signed = x < 0
        A = "".join(reversed(str(abs(x))))
        if signed:
            A += "-"

        B = str(abs(x))
        if signed:
            B = "-" + B

        return A == B
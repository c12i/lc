class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s

        chars = s[1:][::-1]
        curr_idx = 0

        while chars[:curr_idx + 1] + s != (chars[:curr_idx + 1] + s)[::-1]:
            curr_idx += 1

        return chars[:curr_idx + 1] + s
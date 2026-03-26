class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        count = 0
        i = 0

        for ch in t:
            if i < n and ch == s[i]:
                count += 1
                i += 1

        return count == n
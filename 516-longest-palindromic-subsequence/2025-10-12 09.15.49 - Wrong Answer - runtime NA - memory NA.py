class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.split().sort()
        c = Counter(s)
        k = max(c, key=c.get)
        return c[k]
        
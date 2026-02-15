class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cs = Counter(s)
        ct = Counter(t)

        for ch in t:
            if ch not in cs:
                return ch
            elif cs[ch] != ct[ch]:
                return ch

        return ""
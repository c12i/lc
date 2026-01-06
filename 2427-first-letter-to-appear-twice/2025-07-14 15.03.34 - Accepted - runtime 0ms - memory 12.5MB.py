class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        hm = {}

        for i, c in enumerate(s):
            if hm.get(c) is None:
                hm[c] = 1
            else:
                return c

        return s[0]
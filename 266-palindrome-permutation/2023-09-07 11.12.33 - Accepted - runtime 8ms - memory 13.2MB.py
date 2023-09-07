class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1: return True
        hm = {}
        for c in s:
            if c in hm: hm[c] += 1
            else: hm[c] = 1
        if len(hm) == 1: return True
        evens, odds = 0, 0
        for k in hm.keys():
            if hm[k] % 2 == 0: evens += hm[k]
            else: odds += hm[k]
        return evens > odds
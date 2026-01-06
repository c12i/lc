class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hm1 = collections.Counter(s)
        hm2 = collections.Counter(t)
        return hm1 == hm2

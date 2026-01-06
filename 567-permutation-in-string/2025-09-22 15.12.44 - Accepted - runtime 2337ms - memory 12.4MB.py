class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        p1, p2 = 0, len(s1)
        m1, m2 = {}, {}
        for c in s1:
            if not c in m1:
                m1[c] = 1
            else:
                m1[c] += 1
        while p2 <= len(s2): # O(n)
            subs2 = s2[p1:p2] 
            for c in subs2:
                if not c in m2:
                    m2[c] = 1
                else:
                    m2[c] += 1
            if m1 == m2:
                return True
            else:
                m2 = {}
                p1 += 1
                p2 += 1
        return False
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)

        def expand(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]

        best = s[0]

        for i in range(n):
            pal1 = expand(i, i)
            if len(pal1) > len(best):
                best = pal1

            pal2 = expand(i, i + 1)
            if len(pal2) > len(best):
                best = pal2

        return best



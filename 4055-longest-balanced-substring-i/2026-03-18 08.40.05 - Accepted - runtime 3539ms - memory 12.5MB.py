class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            hm = defaultdict(int)
            for j in range(i, len(s)):
                char = s[j]
                hm[char] += 1
                if len(set(hm.values())) == 1:
                    ans = max(ans, j - i + 1)

        return ans
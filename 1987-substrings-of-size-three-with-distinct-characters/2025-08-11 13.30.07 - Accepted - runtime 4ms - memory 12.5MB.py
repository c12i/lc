class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        count = 0

        for right, char in enumerate(s):
            if right - left + 1 == 3:
                uniq = set(s[left:right+1])
                if len(uniq) == 3:
                    count += 1
                left += 1

        return count
        
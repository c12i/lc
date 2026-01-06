class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0
        right = len(needle) - 1

        while right < len(haystack):
            substr = haystack[left:right + 1]
            if substr == needle:
                return left
            else:
                left += 1
                right += 1

        return -1
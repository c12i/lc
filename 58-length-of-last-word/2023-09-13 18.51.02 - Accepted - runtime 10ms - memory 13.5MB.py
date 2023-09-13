# time O(n)
# space O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                i -= 1
            else:
                break
        return len(s[i + 1:])
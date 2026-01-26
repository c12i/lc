class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_count = closed_count = 0

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                open_count += 1
            else:
                open_count -= 1

            if open_count < 0:
                return False

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")" or s[i] == "*":
                closed_count += 1
            else:
                closed_count -= 1

            if closed_count < 0:
                return False

        return True
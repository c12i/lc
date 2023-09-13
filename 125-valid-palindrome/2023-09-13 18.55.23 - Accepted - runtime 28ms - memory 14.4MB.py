class Solution:
    def isPalindrome(self, s):
        chars = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not chars[i].isalnum():
                i += 1
            elif not chars[j].isalnum():
                j -= 1
            elif chars[i].lower() == chars[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

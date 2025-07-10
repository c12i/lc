class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        non_star_chars = []

        for i in range(len(s)):
            if s[i] != '*':
                non_star_chars.append(s[i])
            else:
                non_star_chars.pop()
        
        return "".join(non_star_chars)
        
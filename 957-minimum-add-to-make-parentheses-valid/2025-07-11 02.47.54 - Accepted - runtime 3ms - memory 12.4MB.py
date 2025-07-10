class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        adds = 0
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and len(stack) > 0:
                stack.pop()
            elif s[i] == ')':
                adds += 1

        # account for any unmatched opening parentheses still
        # in stack
        for i in stack:
            adds += 1

        return adds
        
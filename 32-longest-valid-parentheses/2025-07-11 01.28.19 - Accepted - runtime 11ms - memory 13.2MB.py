class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        def is_opening_bracket(c):
            return c == '('

        def is_closing_bracket(c):
            return c == ')'

        stack = [-1]  # use -1 as base index
        max_len = 0

        for i in range(len(s)):
            if is_opening_bracket(s[i]):
                stack.append(i)

            elif is_closing_bracket(s[i]):
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)  # new base index
                else:
                    valid_len = i - stack[-1]
                    max_len = max(max_len, valid_len)

        return max_len

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        counter = 0

        if len(s) <= 1:
            return counter

        def is_opening_bracket(c):
            return c == '('

        def is_closing_bracket(c):
            return c == ')'

        for i in range(len(s)):
            if is_opening_bracket(s[i]):
                if len(stack) == 0:
                    stack.append(i)
                else:
                    peeked_idx = stack[-1]
                    if is_closing_bracket(s[peeked_idx]):
                        stack.append(i)

            elif is_closing_bracket(s[i]):
                if len(stack) == 0:
                    continue
                else:
                    peeked_idx = stack[-1]
                    if is_opening_bracket(s[peeked_idx]):
                        stack.append(i)
                    else:
                        counter = len(stack)
                        stack = []

        
        print(stack)
        if len(stack) > 0:
            return len(stack)
        else:
            return counter
                    
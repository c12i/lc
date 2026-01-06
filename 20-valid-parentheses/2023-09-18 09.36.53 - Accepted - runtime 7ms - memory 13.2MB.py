class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if is_left_bracket(c):
                stack.append(c)
            else:
                top = stack[-1] if stack else None
                if is_match(top, c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

def is_left_bracket(c):
    return c in ('(', '{', '[')

def is_match(l, r):
    print(l, r)
    return (
        l == '(' and r == ')' or
        l == '[' and r == ']' or
        l == '{' and r == '}'
    )
        
class Solution(object):
    # lee(t(c)o)de)
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_list = list(s)
        stack = []
        to_remove = []

        for i in range(len(char_list)):
            if char_list[i] == '(':
                stack.append(i)
            if char_list[i] == ')' and len(stack) > 0:
                stack.pop()
            elif char_list[i] == ')':
                char_list[i] = ''
        
        for i in stack:
            char_list[i] = ''

        return "".join(char_list)


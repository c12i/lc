class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for c in s:
            if c == '*':
                if result:
                    result.pop()
            elif c == '#':
                if result:
                    result.extend(result)
            elif c == '%':
                if result:
                    result = result[::-1]
            else:
                result.append(c)
    
        return "".join(result)
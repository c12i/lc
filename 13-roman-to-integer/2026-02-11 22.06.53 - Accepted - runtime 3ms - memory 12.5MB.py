class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        stack = []

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            num = hm[ch]
            if stack and num < stack[-1]:
                prev = stack.pop()
                new = prev - num
                stack.append(new)
            else:
                stack.append(num)

        return sum(stack)
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # decreasing monotonic stack
        # top is the smallest
        if k == len(num):
            return "0"

        stack = []
        for n in num:
            while stack and int(n) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)

        # if first loop finished still with k
        while k > 0:
            stack.pop()
            k -= 1
        
        return "".join(stack).lstrip("0") or "0"
        
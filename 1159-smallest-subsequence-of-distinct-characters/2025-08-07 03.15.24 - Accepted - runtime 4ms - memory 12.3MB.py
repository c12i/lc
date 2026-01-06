class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = {}

        for i, char in enumerate(s):
            seen[char] = i

        stack = []
        visited = set()

        for i, char in enumerate(s):
            if char in visited:
                continue

            while stack and stack[-1] > char and seen[stack[-1]] > i:
                visited.remove(stack.pop())

            visited.add(char)
            stack.append(char)

        return "".join(stack)
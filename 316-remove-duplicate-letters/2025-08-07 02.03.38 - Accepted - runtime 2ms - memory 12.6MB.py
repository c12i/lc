class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        last_seen = {}

        for i, char in enumerate(s):
            last_seen[char] = i

        stack = []
        visited = set()

        for i, char in enumerate(s):
            if char in visited:
                continue
                
            while stack and stack[-1] > char and last_seen[stack[-1]] > i: # we check last_seen to check if the char appears further ahead in the string
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return ''.join(stack)


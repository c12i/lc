class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n = len(digits)
        hm = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ans = []

        def backtrack(pos = 0, path = []):
            if len(path) == n:
                ans.append("".join(path))
                return
            for i in range(pos, n):
                num = digits[i]
                for ch in hm[num]:
                    path.append(ch)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack()

        return ans
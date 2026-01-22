class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(pos = 0, path = []):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(pos, n):
                path.append(i + 1)
                backtrack(i + 1, path)
                path.pop()

        backtrack()
        return result
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start = 1, path = []):
            if len(path) == k and sum(path) == n:
                result.append(path[:])
                return
            if sum(path) > n:
                return
            
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack()

        return result

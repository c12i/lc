class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def backtrack(pos = 0, path = []):
            if sum(path) == target:
                result.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack()

        return result

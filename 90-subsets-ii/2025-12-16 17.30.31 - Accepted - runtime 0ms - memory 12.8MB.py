class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        def backtrack(pos = 0, path = []):
            ans.append(path[:])

            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack()

        return ans
class Solution(object):
    def permuteUnique(self, nums):
        n = len(nums)
        perm = []
        used = [False] * n

        def backtrack(partial = []):
            if len(partial) == n:
                perm.append(partial[:])
                return 

            seen = set() # track values tried at this position
            for i in range(n):
                # skip if same num already used
                if used[i] or nums[i] in seen:
                    continue

                seen.add(nums[i])
                used[i] = True
                partial.append(nums[i])
                backtrack(partial)
                partial.pop()
                used[i] = False

        backtrack()

        return perm
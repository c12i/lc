class Solution(object):
    def permute(self, nums):
        ans = []
        partial = []

        def recursivelyPermute(res = []):
            if len(res) == len(nums):
                ans.append(res[:])
                return

            for n in nums:
                if n not in res:
                    res.append(n)
                    recursivelyPermute(res)
                    res.pop()

        recursivelyPermute(partial)
        return ans

        
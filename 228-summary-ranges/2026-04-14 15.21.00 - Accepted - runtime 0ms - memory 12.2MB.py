class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        used = set()
        res = []

        for n in nums:
            if n in used: continue
            curr = n
            while curr in set(nums):
                used.add(curr)
                curr += 1
            if curr - 1 != n:
                res.append(str(n) + "->" + str(curr - 1))
            else:
                res.append(str(n))
        return res

class Solution(object):
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts, key=lambda k : counts[k])
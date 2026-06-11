class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counter = Counter(nums)

        return [k for k, v in counter.items() if v > n // 3]
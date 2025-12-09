class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n % 2 != 0: return False
        counter = Counter(nums)
        for n in counter.values():
            if n > 2:
                return False
        return True
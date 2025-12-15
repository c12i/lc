class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0
        for n in nums:
            # check if we are begnining a new sequence
            if n + 1 not in nums:
                continue
            curr_len = 1
            next_num = n + 1
            while next_num in nums:
                curr_len += 1
                next_num += 1
            max_len = max(max_len, curr_len)
        return max_len
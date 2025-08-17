class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0

        for i in range(32 + 1):
            bit_count = 0
            for n in nums:
                bit_count += (n >> i) & 1

            total += bit_count * (len(nums) - bit_count)

        return total

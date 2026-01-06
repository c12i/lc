class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0

        for n in nums:
            diff = diff ^ n

        mask = diff & -diff

        a = 0
        b = 0
        
        for x in nums:
            if x & mask:
                a ^= x
            else:
                b ^= x

        return [a, b]
        
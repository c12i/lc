class Solution(object):
    def singleNumber(self, nums):
        res = 0

        # examine each bit
        for i in range(32): 
            bit_sum = 0
            for x in nums:
                # count 1s at bit i
                bit_sum += ((x >> i) & 1)         
            # leftover belongs to the single number
            if bit_sum % 3:                       
                res |= (1 << i)

        # convert to signed 32-bit
        if res >= 2**31:
            res -= 2**32
            
        return res

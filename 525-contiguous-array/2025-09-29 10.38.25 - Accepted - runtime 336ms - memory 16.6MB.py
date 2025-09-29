class Solution(object):
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        # mapping 0 to last index where we had equal number of 1s and 0s
        hm = {0: -1}

        prefix_sum = 0
        max_len = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum in hm:
                max_len = max(max_len, i - hm[prefix_sum])
            else:
                hm[prefix_sum] = i

        print(hm)

        return max_len

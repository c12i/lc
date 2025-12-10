class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        farthest = jumps = end = 0
        i = 0

        while i < n - 1:
            farthest = max(farthest, i + nums[i])

            # when we’ve scanned the whole current layer, we must take a jump
            if i == end:
                jumps += 1
                end = farthest
                if end >= n - 1:
                    return jumps
            i += 1

        return jumps
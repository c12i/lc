class Solution(object):
    def minimumAverageDifference(self, nums):
        n = len(nums)
        prefix_sum_arr = []
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_sum_arr.append(prefix_sum)

        best = float('inf')
        min_idx = 0
        for i in range(len(prefix_sum_arr)):
            left_av = prefix_sum_arr[i] // (i + 1)
            right_av = 0 if i == n - 1 else (prefix_sum_arr[n - 1] - prefix_sum_arr[i]) // (n - i - 1)
            diff = abs(right_av - left_av)
            if diff < best:
                best = diff
                min_idx = i

        return min_idx
class Solution(object):

    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        max_k = 0
        prev, curr = 0, 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                # Still climbing the same "hill" (increasing run)
                curr += 1
            else:
                # Hit a break in the increasing sequence
                
                # Two ways to form subarrays:
                # 1. Split current run
                # 2. Use previous and current runs
                max_k = max(max_k, curr // 2, min(prev, curr))
                
                # Prepare for next run
                prev = curr
                curr = 1  # Reset current run
        
        # Handle the last run (which might not trigger the else clause)
        max_k = max(max_k, curr // 2, min(prev, curr))
        
        return max_k
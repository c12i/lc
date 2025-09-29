class Solution(object):
    def subarraySum(self, nums, k):
        freq = collections.defaultdict(int)
        freq[0] = 1 # prefix sum of 0 will always appear once
        prefix = []
        prefix_sum = 0
		
        result = 0
	
        for i in range(len(nums)):
			prefix_sum += nums[i]
			# because k(target) = curr_prefix_sum - previous_prefix_sum
			# we are trying to evaluate what this potential previous_prefix_sum is.
			potential_prefix_sum = prefix_sum - k
		
			if potential_prefix_sum in freq:
				# add all other prev_prefix sums -> subarray occurrences that will yield k
				result += freq[potential_prefix_sum]
			
			freq[prefix_sum] += 1
						
        return result
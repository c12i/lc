class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hm = defaultdict(int)
        hm[0] = 1
        prefix_sum = 0
        ans = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            # (prefix_sum[i] - prefix_sum[j]) % k = 0
            # prefix_sum[i] % k  - prefix_sum[j] % k = 0
            x = prefix_sum % k

            if x in hm:
                ans += hm[x]

            hm[x] += 1
        
        return ans
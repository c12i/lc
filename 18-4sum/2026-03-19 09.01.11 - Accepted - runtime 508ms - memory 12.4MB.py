class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        quadruplets = []
        seen = set()

        for i in range(n):
            num_a = nums[i]
            for j in range(i+1, n):
                num_b = nums[j]
                goal = target - num_a - num_b
                left, right = j + 1, n - 1

                while left < right:
                    s = nums[left] + nums[right]
                    if s < goal:
                        left += 1
                    elif s > goal:
                        right -= 1
                    else:
                        q = (num_a, num_b, nums[left], nums[right])
                        if q not in seen:
                            quadruplets.append([num_a, num_b, nums[left], nums[right]])
                            seen.add(q)
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1

        return quadruplets

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        hm = {}
        i = 0
        loops = 0

        while loops < 2:
            while stack and nums[i] > nums[stack[-1]]:
                prev_i = stack.pop()
                hm[prev_i] = i

            if loops == 0:
                stack.append(i)

            if i == (len(nums) - 1):
                loops += 1
                i = 0
            else:
                i += 1

        result = []

        for i in range(len(nums)):
            if hm.get(i) is not None:
                result.append(nums[hm[i]])
            else:
                result.append(-1)

        return result
            

class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        start = 0

        inc_stack = []
        for i in range(n):
            if inc_stack and inc_stack[-1] >= nums[i]:
              start = i - 1
              break  
            inc_stack.append(nums[i])

        dec_stack = []
        for i in range(start, n):
            if dec_stack and dec_stack[-1] <= nums[i]:
                start = i - 1
                break
            dec_stack.append(nums[i])

        inc_stack2 = []
        for i in range(start, n):
            if inc_stack2 and inc_stack2[-1] >= nums[i]:
                return False
            inc_stack2.append(nums[i])

        return all(len(s) > 1 for s in [inc_stack, dec_stack, inc_stack2])
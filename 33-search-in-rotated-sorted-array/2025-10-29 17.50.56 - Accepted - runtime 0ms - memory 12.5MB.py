class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        rot = left

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
            if nums[real] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
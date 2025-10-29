class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        rot = low + 1
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
            if nums[real] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
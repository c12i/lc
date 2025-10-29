class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums = self.uniq(nums)
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
                return True
            if nums[real] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    
    def uniq(self, arr):
        """
        Get unique elements from arr in place
        O(n)
        """
        seen = set()
        i = 0
        j = 0

        for i in range(len(arr)):
            if arr[i] not in seen:
                seen.add(arr[i])
                arr[j] = arr[i]
                j += 1

        return arr[:j]
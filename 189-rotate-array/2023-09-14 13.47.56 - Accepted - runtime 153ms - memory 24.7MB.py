class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # get the rotatation start index
        k = k % len(nums)
        nums = reverse_arr(nums, 0, len(nums) - 1)
        nums[:k] = reverse_arr(nums[:k], 0, len(nums[:k]) - 1)
        nums[k:] = reverse_arr(nums[k:], 0, len(nums[k:]) - 1)
        return nums


def reverse_arr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
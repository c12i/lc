class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = self.quickSort(nums)
        n = len(nums)

        return sorted_nums[n - k]
        

    def quickSort(self, arr):
        if len(arr) < 2:
            return arr

        pivot = random.choice(arr)

        left = [n for n in arr if n < pivot]
        mid = [n for n in arr if n == pivot]
        right = [n for n in arr if n > pivot]

        return self.quickSort(left) + mid + self.quickSort(right)
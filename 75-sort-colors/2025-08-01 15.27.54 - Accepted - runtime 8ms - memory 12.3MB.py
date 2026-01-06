class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # return self.quickSortInPlace(nums, 0, len(nums) - 1)
        return self.bubbleSort(nums)


    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n):
            min_idx = i

            for j in range(i, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr

    
    def quickSortInPlace(self, arr, low, high):
        """
        Quick Sort implementation done in place
        """
        if low < high:
            # Partition the array, pivot is now in the right place
            pivot_index = self._partition(arr, low, high)
            # Recursively sort the left and right partitions
            self.quickSortInPlace(arr, low, pivot_index - 1)
            self.quickSortInPlace(arr, pivot_index + 1, high)


    def _partition(self, arr, low, high):
        pivot = arr[high]  # Lomuto: pivot is the last element
        i = low  # 'i' is the boundary for values < pivot

        for j in range(low, high):
            if arr[j] < pivot:
                # Swap arr[j] into the "less than pivot" zone
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        # Finally, place the pivot after the last smaller element
        arr[i], arr[high] = arr[high], arr[i]
        return i  # Return the pivot inde
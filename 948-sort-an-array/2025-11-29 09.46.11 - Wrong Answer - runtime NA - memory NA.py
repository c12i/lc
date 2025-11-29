class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.countSort(nums)

    
    def countSort(self, arr):
        if not arr:
            return []

        max_val = max(arr)
        count = [0] * (max_val + 1)

        for num in arr:
            count[num] += 1

        print(count)

        sorted_arr = []
        for num, freq in enumerate(count):
            sorted_arr.extend([num] * freq)
            print(sorted_arr)

        return sorted_arr


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
        return i  # Return the pivot index

    
    # def _partition(self, arr, start, end):
    #     pivot = arr[(start + end) // 2]  # Pivot element is the middle element
    #     i = start - 1
    #     j = end + 1

    #     while True:
    #         # Move `i` to the right until an element >= pivot is found
    #         while True:
    #             i += 1
    #             if arr[i] >= pivot:
    #                 break

    #         # Move `j` to the left until an element <= pivot is found
    #         while True:
    #             j -= 1
    #             if arr[j] <= pivot:
    #                 break

    #         # If `i` crosses `j`, return `j`
    #         if i >= j:
    #             return j

    #         # Swap elements at `i` and `j`
    #         arr[i], arr[j] = arr[j], arr[i]
            
    
    def quickSortAlloc(self, arr):
        """
        Quick sort implementation but left, right and mid are allocated
        """
        if len(arr) < 2:
            return arr

        pivot = random.choice(arr)

        left = [n for n in arr if n < pivot]
        mid = [n for n in arr if n == pivot]
        right = [n for n in arr if n > pivot]

        return self.quickSortAlloc(left) + mid + self.quickSortAlloc(right)
        

    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2

        arr_one = self.mergeSort(arr[0:mid])
        arr_two = self.mergeSort(arr[mid:])

        return self._merge(arr_one, arr_two)

    
    def _merge(self, arrA, arrB):
        merged = []
        i, j = 0, 0
        lenA, lenB = len(arrA), len(arrB)

        while i < lenA and j < lenB:
            if arrA[i] < arrB[j]:
                merged.append(arrA[i])
                i += 1
            else:
                merged.append(arrB[j])
                j += 1

        while i < lenA:
            merged.append(arrA[i])
            i += 1

        while j < lenB:
            merged.append(arrB[j])
            j += 1

        return merged

    
    def heapSort(self, arr):
        heapq.heapify(arr)              

        return [heapq.heappop(arr) for _ in range(len(arr))]


    def insertionSort(self, arr):
        n = len(arr)

        for i in range(n):
            j = i

            while j > 0:
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]

                j -= 1

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

    
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr 

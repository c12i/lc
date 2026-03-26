class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        min_diff = float('inf')
        values = []
        arr.sort()

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                values = []
                values.append([arr[i], arr[i + 1]])
            elif diff == min_diff:
                values.append([arr[i], arr[i + 1]])


        return sorted(values)
        
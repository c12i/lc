class Solution(object):
    def maxTurbulenceSize(self, arr):
        max_size = 1
        left = right = 0

        while right < len(arr) - 1:
            if right == 0 or (arr[right - 1] == arr[right] ):
                # reset left pointer if (prev == right == next) or just (right == prev)
                left = right + 1 if arr[right] == arr[right + 1] else right
                right += 1
            elif (
                (arr[right - 1] < arr[right] > arr[right + 1]) or 
                (arr[right - 1] > arr[right] < arr[right + 1])
            ):
                right += 1
            else:
                left = right
                right += 1
            
            max_size = max(max_size, right - left + 1)

        return max_size
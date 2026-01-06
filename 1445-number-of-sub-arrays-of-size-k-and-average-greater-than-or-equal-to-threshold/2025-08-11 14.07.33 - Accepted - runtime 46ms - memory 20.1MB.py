class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        left = 0
        rolling_sum = 0
        count = 0

        for right, x in enumerate(arr):
            rolling_sum += x

            if right - left + 1 == k:
                av = rolling_sum / k
                if av >= threshold:
                    count += 1
                rolling_sum -= arr[left]
                left += 1

        return count


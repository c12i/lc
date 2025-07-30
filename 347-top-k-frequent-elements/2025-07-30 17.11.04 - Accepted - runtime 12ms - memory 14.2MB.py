class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        keys = sorted(counter.items(), key=lambda x: x[1])
        result = []

        for _ in range(k):
            k, _ = keys.pop()
            result.append(k)

        return result
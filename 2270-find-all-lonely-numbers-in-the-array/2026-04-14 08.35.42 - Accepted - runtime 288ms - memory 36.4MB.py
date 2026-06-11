class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        res = []

        for k in counter.keys():
            if counter[k] > 1:
                continue
            if k - 1 not in counter and k + 1 not in counter:
                res.append(k)

        return res
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for num in range(n + 1):
            # count num of set bits in i
            count = 0
            while num:
                count += num & 1
                num = num >> 1
            res.append(count)

        return res


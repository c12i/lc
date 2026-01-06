class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        digits = []

        while temp > 0:
            d = temp % 10
            digits.append(d)
            temp = temp // 10

        freq_map = defaultdict(int)

        for d in digits:
            freq_map[d] += 1

        smallest = (float('inf'), 0)
        
        for k in freq_map.keys():
            smallest = min(smallest, (freq_map[k], k))

        return smallest[1]
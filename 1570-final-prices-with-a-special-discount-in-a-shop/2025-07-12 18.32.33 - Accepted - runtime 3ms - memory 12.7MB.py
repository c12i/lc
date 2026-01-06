class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        hm = {}

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                val = stack.pop()
                hm[val] = i
            stack.append(i)

        result = []
        for i in range(len(prices)):
            if hm.get(i) is not None:
                result.append(prices[i] - prices[hm[i]])
            else:
                result.append(prices[i])

        return result
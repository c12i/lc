class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """

        min_need = min(need1, need2)
        min_cost = min(costBoth, cost1 + cost2)
        res = min_need * min_cost

        rem1 = need1 - min_need
        rem2 = need2 - min_need

        res += rem1 * min(cost1, costBoth)
        res += rem2 * min(cost2, costBoth)

        return res
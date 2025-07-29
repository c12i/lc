class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        count = 0

        for c in sorted(coins, reverse=True):
            while amount >= c:
                amount -= c
                count += 1

        if amount != 0:
            return -1

        return count
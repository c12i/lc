class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [None] * n
        
        def minCost(i):
            if i < 0: return 0
            if i == 0 or i == 1: return cost[i]
            if dp[i] is not None: return dp[i]
            
            dp[i] = cost[i] + min(minCost(i - 1), minCost(i - 2))

            return dp[i]


        return min(minCost(n - 1), minCost(n - 2))
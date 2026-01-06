class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        dp = [None] * n
        
        def steps(i = 0):
            if i == n:
                return 1
            if i > n:
                return 0
            if dp[i]:
                return dp[i]
            dp[i] = steps(i + 1) + steps(i + 2)
            return dp[i]

        return steps()


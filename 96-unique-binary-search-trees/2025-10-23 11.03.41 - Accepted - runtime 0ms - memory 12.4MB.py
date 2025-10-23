class Solution(object):
    def numTrees(self, n):
        # dp[i] represents the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        dp[0] = 1 # empty tree
        dp[1] = 1 # single node
        
        for nodes in range(2, n + 1):
            # try each value as root
            for root in range(1, nodes + 1):
                left = root - 1 # nodes in left subtree
                right = nodes - root # nodes in right subtree
                dp[nodes] += (dp[left] * dp[right])

        return dp[n]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Steps:
# - initialize global max (needs to be the smallest possible number to ensure any real path will beat it)
# - define recursive dfs helper: if node is None return 0 -> base case when we hit a null node
# - recursively get the best gain from left and right -> ignoring any child whose contribution is negative, since it would lower the total sum
# - compute the full path sum through this node -> this is the fork path, only considered here and not bubbled up since we cant split paths when doing this
# - update global max sum -> track best total path sum we've seen, regardless if it passes through root.
# - return ons side's gain to parent -> we can only choose one direction (L or R), otherwise we form a cycle
# - call dfs and return the result

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = root.val

        def dfs(node):
            if not node:
                return 0
            
            self.max_sum = max(self.max_sum, node.val)
            if not node.left and not node.right:
                return node.val

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.max_sum = max(self.max_sum, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)

        return self.max_sum
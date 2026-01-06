# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## use max height as the base
# the heights of a balanced binary tree subtrees should be equal or only offset by 1. Anything greater indicates an imbalanced tree
# calculate the max height on both sides. if the diff between the heights is > 1, the tree is unbalanced, communicate this upwards

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.dfs(root) != -1

    def dfs(self, root):
        if root is None:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if -1 in [left, right]: return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, is_left = False):
            if not node:
                return 0

            if is_left and not node.left and not node.right:
                return node.val
            
            left = dfs(node.left, True)
            right = dfs(node.right, False)

            return left + right

        return dfs(root)
        
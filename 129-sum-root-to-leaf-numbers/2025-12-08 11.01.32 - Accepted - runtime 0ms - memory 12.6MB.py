# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0
        def dfs(node, curr = 0):
            if not node:
                return

            if not node.left and not node.right:
                self.result += ((curr * 10) + node.val)
            if node.left:
                dfs(node.left, (curr * 10) + node.val)
            if node.right:
                dfs(node.right, (curr * 10) + node.val)
        
        dfs(root)

        return self.result
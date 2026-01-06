# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.dfs(root, result)
        return result

    
    def dfs(self, node, values = []):
        if node is None:
            return
        self.dfs(node.left, values)
        self.dfs(node.right, values)
        values.append(node.val)
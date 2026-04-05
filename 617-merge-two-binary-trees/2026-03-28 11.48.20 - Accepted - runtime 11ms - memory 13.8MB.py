# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def dfs(node1, node2):
            if not node1 and not node2:
                return

            new_node = TreeNode()
            if node1 and node2:
                new_node.val = node1.val + node2.val
            elif node1 and not node2:
                new_node.val = node1.val
            elif node2 and not node1:
                new_node.val = node2.val

            new_node.left = dfs(node1.left if node1 else None, node2.left if node2 else None)
            new_node.right = dfs(node1.right if node1 else None, node2.right if node2 else None)

            return new_node

        return dfs(root1, root2)
        
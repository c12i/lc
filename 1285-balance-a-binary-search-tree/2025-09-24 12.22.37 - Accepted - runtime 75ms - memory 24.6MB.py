# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        vals = []
        def inorder(node, vals):
            if not node:
                return
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)
            
        inorder(root, vals)

        def reconstructTree(values, start, end):
            if start > end:
                return

            mid = (start + end) // 2
            node = TreeNode(values[mid])

            node.left = reconstructTree(values, start, mid - 1)
            node.right = reconstructTree(values, mid + 1, end)

            return node

        return reconstructTree(vals, 0, len(vals) - 1)
        
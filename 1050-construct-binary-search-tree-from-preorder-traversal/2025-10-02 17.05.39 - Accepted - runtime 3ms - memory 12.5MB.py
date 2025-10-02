# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        self.index = 0
        n = len(preorder)
        def reconstruct(lower = float('-inf'), upper = float('inf')):
            if self.index == n:
                return
            val = preorder[self.index]
            if val < lower or val > upper:
                return
            self.index += 1
            node = TreeNode(val)
            node.left = reconstruct(lower, val)
            node.right = reconstruct(val, upper)
            return node

        return reconstruct()
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(root, lower = float('-inf'), upper = float('inf')):
            if not root:
                return True

            if root.val <= lower or root.val >= upper:
                return False

            return valid(root.left, lower, root.val) and valid(root.right, root.val, upper)

        return valid(root)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        self.vals = []

        def inorder(node):
            if not node:
                return
            
            if node.left:
                inorder(node.left)

            if node.val != key:
                self.vals.append(node.val)

            if node.right:
                inorder(node.right)

        inorder(root)

        def reconstruct(l, r):
            #missing
            if l > r:
                return
            mid = (l + r) // 2
            node = TreeNode(self.vals[mid])
            # use mid to set range
            node.left = reconstruct(l, mid - 1)
            node.right = reconstruct(mid + 1, r)
            return node

        return reconstruct(0, len(self.vals) - 1)

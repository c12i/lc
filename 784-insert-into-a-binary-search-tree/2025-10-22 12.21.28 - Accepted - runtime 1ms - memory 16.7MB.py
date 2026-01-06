# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
    
        current = root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
        
        return root
        # vals = []
        # def levelorder(node):
        #     if not node:
        #         return
        #     levelorder(node.left)
        #     vals.append(node.val)
        #     levelorder(node.right)
        
        # levelorder(root)
        # vals.append(val)
        # vals.sort()

        # def reconstruct(l, r):
        #     if l > r:
        #         return
        #     mid = (l + r) // 2
        #     node = TreeNode(vals[mid])
        #     node.left = reconstruct(l, mid - 1)
        #     node.right = reconstruct(mid + 1, r)
        #     return node

        # return reconstruct(0, len(vals) - 1)
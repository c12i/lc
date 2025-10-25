# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        vals = []
        def levelorder(node):
            if not node:
                return
            levelorder(node.left)
            vals.append(node.val)
            levelorder(node.right)
            
        levelorder(root)

        l = r = 0

        for i in range(len(vals)):
            if vals[i] == low:
                l = i
            if vals[i] == high:
                r = i
        
        return sum(vals[l:r+1])
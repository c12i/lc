# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()
        
        def dfs(root):
            if not root:
                return False

            if k - root.val in seen:
                return True
                
            seen.add(root.val)

            left = dfs(root.left)
            right = dfs(root.right)

            return left or right

        return dfs(root)

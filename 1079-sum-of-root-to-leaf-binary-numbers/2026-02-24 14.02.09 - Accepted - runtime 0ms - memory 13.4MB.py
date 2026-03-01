# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        nums = []

        def dfs(root, digits = []):
            if not root:
                return None
            
            digits.append(str(root.val))

            if not root.left and not root.right:
                num = int("".join(digits), 2)
                nums.append(num)

            dfs(root.left, digits)
            dfs(root.right, digits)

            digits.pop()
        
        dfs(root)

        return sum(nums)

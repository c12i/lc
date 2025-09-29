# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        results = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            if not node.left and not node.right and remaining == 0:
                results.append(path[:])
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            path.pop()  # backtrack

        dfs(root, targetSum, [])
        return results
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths = []

        def dfs(root, path):
            if not root:
                return

            path.append(str(root.val))

            if not root.left and not root.right:
                paths.append(path[:])
            else:
                dfs(root.left, path)
                dfs(root.right, path)

            path.pop()

        dfs(root, [])

        return ["->".join(p) for p in paths]
        
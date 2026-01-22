# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.min_path = None

        def dfs(node, path = []):
            if not node:
                return
            path.append(alphabet[node.val])
            if not node.left and not node.right:
                curr = "".join(path[::-1])
                if self.min_path is None or curr < self.min_path:
                    self.min_path = curr
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()    

        dfs(root)

        return self.min_path

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        roots = [root]

        def dfs(node):
            if not node:
                return None

            should_delete = node.val in to_delete
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if should_delete:
                if node.left:
                    roots.append(node.left)
                if node.right:
                    roots.append(node.right)
                return None
            
            return node

        root = dfs(root)
        
        return roots
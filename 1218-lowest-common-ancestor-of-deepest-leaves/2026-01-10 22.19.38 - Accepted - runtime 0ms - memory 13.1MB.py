# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        queue = deque([root])
        deepest_nodes = []

        while queue:
            deepest_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                deepest_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        def lca(node, targets):
            if not node: return None
            if node in targets:
                return node

            left = lca(node.left, targets)
            right = lca(node.right, targets)
            
            if left and right:
                return node
            return left or right

        return lca(root, set(deepest_nodes))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_map = {root: None}
        queue = deque([root])

        while p not in parent_map or q not in parent_map:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

        ancestors = set()
        curr = p
        while curr:
            ancestors.add(curr)
            curr = parent_map[curr]

        curr = q
        while curr not in ancestors:
            curr = parent_map[curr]
        return curr
        
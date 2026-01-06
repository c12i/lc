# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        q = deque([root])
        count = 0
        while q:
            n = q.popleft()
            count += 1

            if n and n.left:
                q.append(n.left)

            if n and n.right:
                q.append(n.right)

        return count
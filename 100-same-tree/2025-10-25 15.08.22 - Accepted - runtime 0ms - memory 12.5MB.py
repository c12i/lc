# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([(p, q)])

        while queue:
            p, q = queue.popleft()

            if not p and not q:
                continue
            elif not p or not q:
                return False
            elif p and q and p.val != q.val:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True

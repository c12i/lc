# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        q = deque([(root, targetSum)])

        while q:
            node, curr_sum = q.popleft()
            next_sum = curr_sum - node.val
            if next_sum == 0 and not (node.left or node.right):
                return True

            if node.left:
                q.append((node.left, next_sum))
            if node.right:
                q.append((node.right, next_sum))
            

        return False
        
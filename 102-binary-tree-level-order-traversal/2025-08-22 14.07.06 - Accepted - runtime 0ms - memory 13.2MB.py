# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append(root)

        result = []

        while queue:
            vals = []

            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    vals.append(node.val)

                if node and node.left:
                    queue.append(node.left)

                if node and node.right:
                    queue.append(node.right)

            if vals:
                result.append(vals)

        return result

        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = deque([(root, None)]) # (node, parent) -> parent as value
        while queue:
            x_parent = y_parent = None
            for _ in range(len(queue)):
                curr, parent_val = queue.popleft()
                if curr.val == x:
                    x_parent = parent_val
                if curr.val == y:
                    y_parent = parent_val

                if curr.left:
                    queue.append((curr.left, curr.val))
                if curr.right:
                    queue.append((curr.right, curr.val))

            if x_parent and y_parent:
                return x_parent != y_parent
        
        return False
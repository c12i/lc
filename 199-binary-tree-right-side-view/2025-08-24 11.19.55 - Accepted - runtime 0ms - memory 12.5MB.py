# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        values = self.bfs(root)
        result = []

        for v in values:
            result.append(v.pop())
        
        return result


    def bfs(self, root):
        result = []
        if not root:
            return result
        queue = deque([root])

        while queue:
            subarr = []

            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    subarr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            result.append(subarr)

        return result
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """
        def dfs(node):
            if not node:
                return -1
            return 1 + max(dfs(node.left), dfs(node.right))
        height = dfs(root)

        rows = height + 1
        cols = (2 ** (height + 1)) - 1

        matrix = [["" for _ in range(cols)] for _ in range(rows)]

        q = deque([(root, (0, cols - 1))])
        curr_row = 0

        while q:
            for _ in range(len(q)):
                node, pos = q.popleft()
                start, end = pos
                mid = (start + end) // 2

                matrix[curr_row][mid] = str(node.val)

                if node.left:
                    q.append((node.left, (start, mid - 1)))
                if node.right:
                    q.append((node.right, (mid + 1, end)))

            curr_row += 1

        return matrix
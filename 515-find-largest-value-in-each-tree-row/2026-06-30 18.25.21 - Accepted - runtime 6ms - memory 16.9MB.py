# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        q = deque([root])
        ans = []

        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if vals:
                ans.append(max(vals))
        
        return ans
        
        
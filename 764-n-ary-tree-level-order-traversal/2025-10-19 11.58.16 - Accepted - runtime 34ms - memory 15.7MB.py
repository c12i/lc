"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            level_size = len(q)

            partial = []
            for i in range(level_size):
                node = q.popleft()
                if node:
                    partial.append(node.val)

                for child in node.children:
                    q.append(child)

            if partial:
                res.append(partial)
                
        return res


        
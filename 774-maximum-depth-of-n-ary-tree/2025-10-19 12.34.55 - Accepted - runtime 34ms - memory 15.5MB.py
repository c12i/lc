"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            if not node.children:
                return 1

            child_max_d = 0

            for child in node.children:
                child_max_d = max(dfs(child), child_max_d)

            return child_max_d + 1
        
        return dfs(root)
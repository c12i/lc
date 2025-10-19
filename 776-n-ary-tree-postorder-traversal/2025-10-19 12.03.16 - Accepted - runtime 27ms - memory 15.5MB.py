"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        result = []
        self.dfs(root, result)
        return result


    def dfs(self, node, values = []):
        if node is None:
            return

        for child in node.children:
            self.dfs(child, values)

        values.append(node.val)
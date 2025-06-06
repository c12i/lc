# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##  Steps:
# - traverse left subtree and get the height then traverse right subtree and get teh height, then we return the sum of the both


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        self.height(root)
        return self.max_diameter


    def height(self, node):
        if node is None:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        # Diameter at this node = longest path through it
        self.max_diameter = max(self.max_diameter, left + right)

        # Return height to parent
        return 1 + max(left, right)


        
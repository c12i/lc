# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        queue = deque([(root, None)]) # (node, parent)
        root.val = 0
        while queue:
            m = defaultdict(list)
            for _ in range(len(queue)):
                curr, parent = queue.popleft()
                if curr.left:
                    m[curr].append(curr.left)
                    queue.append((curr.left, curr))
                if curr.right:
                    m[curr].append(curr.right)
                    queue.append((curr.right, curr))

            level_sum = sum(node.val for children in m.values() for node in children)
            
            # for each parent's children, set their value to total minus their sibling group sum
            for parent, children in m.items():
                sibling_sum = sum(child.val for child in children)
                for child in children:
                    child.val = level_sum - sibling_sum
                
        return root
              
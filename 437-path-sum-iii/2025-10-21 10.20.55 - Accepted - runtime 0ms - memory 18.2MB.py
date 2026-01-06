# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = 0
            # number of valid paths ending at this node
            if (curr_sum - targetSum) in prefix_count:
                count += prefix_count[curr_sum - targetSum]

            # update prefix_count with current sum
            prefix_count[curr_sum] += 1

            # recurse
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # backtrack (remove current sum before returning up)
            prefix_count[curr_sum] -= 1

            return count

        return dfs(root, 0)
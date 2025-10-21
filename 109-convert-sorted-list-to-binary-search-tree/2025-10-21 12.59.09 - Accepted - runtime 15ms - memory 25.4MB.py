# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        vals = []
        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next

        
        def reconstruct(l, r):
            if l > r:
                return

            mid = (l + r) // 2
            node = TreeNode(vals[mid])
            node.left = reconstruct(l, mid - 1)
            node.right = reconstruct(mid + 1, r)
            return node

        return reconstruct(0, len(vals) - 1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = ListNode(0)
        curr = node

        while curr and curr.next:
            prev = curr
            next_node = curr.next
            temp = curr.val

            curr.val = next_node.val
            next_node.val = temp

            curr = curr.next

        prev.next = None    
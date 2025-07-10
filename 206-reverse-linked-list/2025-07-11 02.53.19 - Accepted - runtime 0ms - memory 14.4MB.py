# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        r = None

        while current_node:
            next_node = current_node.next
            current_node.next = r
            r = current_node
            current_node = next_node

        return r
        
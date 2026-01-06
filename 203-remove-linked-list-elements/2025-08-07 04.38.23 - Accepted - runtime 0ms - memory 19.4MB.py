# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        current = head
        dummy = ListNode(0, head)
        prev = dummy

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next

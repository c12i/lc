# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = head

        while current:
            prev = dummy
            next_node = current.next

            # Find the right place to insert current
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            current.next = prev.next
            prev.next = current
            current = next_node

        return dummy.next
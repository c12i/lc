# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        prev = ListNode(0)

        while fast and fast.next:
            prev.next = slow
            slow = slow.next
            fast = fast.next.next

        if prev and prev.next:
            prev = prev.next
            prev.next = slow.next
        else:
            return prev.next

        return head

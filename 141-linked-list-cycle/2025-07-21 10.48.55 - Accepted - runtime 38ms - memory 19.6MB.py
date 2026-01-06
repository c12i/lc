# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if hare == tortoise:
                return True

        return False
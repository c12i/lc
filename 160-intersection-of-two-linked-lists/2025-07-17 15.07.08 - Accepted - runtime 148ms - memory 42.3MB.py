# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA or ptrB

        # seen = set()

        # current = headA
        # while current:
        #     seen.add(current)
        #     current = current.next

        # current = headB
        # while current:
        #     if current in seen:
        #         break
        #     current = current.next

        # return current 
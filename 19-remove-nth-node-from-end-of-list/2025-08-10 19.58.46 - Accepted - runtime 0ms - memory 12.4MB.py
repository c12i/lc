# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        list_len = self.getLen(head)
        real_n = list_len - n
        
        prev = dummy
        for _ in range(real_n):
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next

    
    def getLen(self, node):
        if not node:
            return 0
        l = 0
        while node:
            node = node.next
            l += 1
        return l

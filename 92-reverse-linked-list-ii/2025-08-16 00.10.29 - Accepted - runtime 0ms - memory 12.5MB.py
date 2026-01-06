# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        pos = 1
        curr_node = head
        while pos < left:
            prev = curr_node
            curr_node = curr_node.next
            pos += 1

        temp = curr_node
        rev = None
        for _ in range(right - left + 1):
            next_node = curr_node.next
            curr_node.next = rev
            rev = curr_node
            curr_node = next_node

        prev.next = rev
        temp.next = curr_node

        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy_l = ListNode(0, head)
        dummy_r = ListNode(0, head)

        list_len = self.getLen(head)

        # process left side
        k_left = k
        prev_l = dummy_l
        for _ in range(k_left):
            prev_l = prev_l.next

        # process right side
        k_right = (list_len - k) + 1
        prev_r = dummy_r
        for _ in range(k_right):
            prev_r = prev_r.next

        # swap
        temp = prev_l.val
        prev_l.val = prev_r.val
        prev_r.val = temp

        return head


    def getLen(self, node):
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        return cnt
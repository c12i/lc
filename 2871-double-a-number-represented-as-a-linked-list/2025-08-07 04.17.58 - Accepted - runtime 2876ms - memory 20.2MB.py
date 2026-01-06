# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list_len = self.getLen(head)
        list_num = self.getListNum(head, list_len)
        doubled = list_num * 2

        self.buildList(doubled, head)
        
        return self.reverseList(head)

        
    def getLen(self, head):
        curr = 0
        current_node = head

        while current_node:
            current_node = current_node.next
            curr += 1

        return curr

    def getListNum(self, head, n):
        digits = 10 ** (n - 1)
        num = 0
        current_node = head

        while current_node:
            res = current_node.val * digits
            num += res

            current_node = current_node.next
            digits /= 10
            
        return num


    def buildList(self, num, current_node):
        prev = None

        while current_node and num > 0:
            digit = num % 10
            current_node.val = digit

            prev = current_node
            current_node = current_node.next
            num = num // 10

        if num > 0 and prev:
            prev.next = ListNode(num)
            

    def reverseList(self, current_node):
        r = None

        while current_node:
            next_node = current_node.next
            current_node.next = r
            r = current_node
            current_node = next_node

        return r
        
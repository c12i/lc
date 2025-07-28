# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0 , head)
        currentNode = dummy.next
        prev = dummy

        while currentNode and currentNode.next:
            nextNode = currentNode.next
            temp = nextNode.next
            nextNode.next = currentNode
            
            prev.next = nextNode

            prev = currentNode
            currentNode.next = temp

            currentNode = temp

        return dummy.next
 

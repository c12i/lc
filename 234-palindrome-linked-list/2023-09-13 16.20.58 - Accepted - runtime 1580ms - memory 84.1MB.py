# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse = reverse_linked_list(clone(head))
        while head and reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next
        return True

def reverse_linked_list(node):
    current_node = node
    reverse = None
    while current_node is not None:
        next_node = current_node.next
        current_node.next = reverse
        reverse = current_node
        current_node = next_node
    return reverse
    
def clone(head):
    if head is None:
        return None
    new_head = ListNode(head.val)
    current = head
    cloned_node = new_head
    while current.next is not None:
        cloned_node.next = ListNode(current.next.val)
        current = current.next
        cloned_node = cloned_node.next

    return new_head

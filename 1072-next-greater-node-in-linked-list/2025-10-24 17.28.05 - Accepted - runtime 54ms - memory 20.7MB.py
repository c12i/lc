# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next

        stack = []
        res = [0] * len(temp)

        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                idx = stack.pop()
                res[idx] = temp[i]
            stack.append(i)

        return res


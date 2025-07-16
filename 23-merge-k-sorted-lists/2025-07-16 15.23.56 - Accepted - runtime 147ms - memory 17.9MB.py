# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if not lists:
            return None

        while len(lists) > 1:
            merged = self.mergeTwoLists(lists[0], lists[1])

            lists.append(merged)

            lists = lists[2:]

        return lists[0]

    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            merged_head = list1
            list1 = list1.next
        else:
            merged_head = list2
            list2 = list2.next

        current = merged_head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return merged_head
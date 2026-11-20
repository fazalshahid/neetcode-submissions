# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = last = ListNode(-1)

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    node = list1
                    list1 = list1.next
                else:
                    node = list2
                    list2 = list2.next
            elif list1:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            last.next = node
            last = node
        last.next = None
        return dummy.next 
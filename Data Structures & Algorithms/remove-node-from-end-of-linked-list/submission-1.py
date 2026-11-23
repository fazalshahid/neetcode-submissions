# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def get_count():
            h = head
            count = 0
            while h:
                count += 1
                h = h.next
            return count
        
        count = get_count()
        print(count)
        dummy = last = ListNode(-1)
        
        i = 0
        while head and i < (count - n):
            last.next = head
            last = head
            head = head.next
            i += 1
        print(last.val)
        if head:
            last.next = head.next
        
        return dummy.next





        
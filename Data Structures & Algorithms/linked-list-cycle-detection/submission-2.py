# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None or head.next is None:
            return False
        fast = head
        slow = head

        start = True

        while((fast is not None and fast.next is not None) and slow is not None):
            if fast == slow:
                if start == True:
                    start = False
                else:
                    return True
            
            fast = fast.next.next
            slow = slow.next
        
        return False
        
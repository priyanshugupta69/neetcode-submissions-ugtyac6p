# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0

        while(temp != None):
            size += 1
            temp = temp.next


        it = size - n

        dummy = ListNode()
        dummy.next = head
        
        temp = dummy
        count = 0

        print(it)

        while(count < it):
            temp = temp.next
            count += 1

        temp.next = temp.next.next

        return dummy.next

               
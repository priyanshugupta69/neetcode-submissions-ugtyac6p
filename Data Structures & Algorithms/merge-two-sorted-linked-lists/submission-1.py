# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        newList = ListNode()
        head = newList

        while(head1 is not None and head2 is not None):
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
                head = head.next
            
            elif head2.val < head1.val:
                head.next = head2
                head2 = head2.next
                head = head.next

        if head1:
            head.next = head1
        else:
            head.next = head2
            
        return newList.next

            
        
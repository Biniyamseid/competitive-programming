# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = ListNode(head.val)
        second = ListNode(head.next.val)
        third = head.next.next
        first.next = self.swapPairs(third)
        second.next = first
        return second
        
                
                
        
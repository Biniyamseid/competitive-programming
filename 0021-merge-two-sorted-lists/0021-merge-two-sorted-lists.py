# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a or (b and a.val >b.val):
            a,b = b,a
        if a:
            a.next = self.mergeTwoLists(a.next,b)
        return a
            
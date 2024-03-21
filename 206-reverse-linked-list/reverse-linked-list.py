# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ [1,2,3,4,5]

        
        """
        if not head:
            return 
        dm = prev = ListNode(head.val)
        head = head.next
        while head:
            prev = ListNode(head.val,prev)
            head = head.next
        return prev
    

 





        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr,prev):
            if not curr:
                return prev
            nextNode = curr.next
            curr.next = prev
            return reverse(nextNode,curr)
        return reverse(head,None)
            
       
            
#         dummy= node1= ListNode(None)
#         stack = []
#         while head:
#             stack.append(ListNode(head.val))
#             head = head.next
#         while stack:
#             dummy.next = stack.pop()
#             dummy = dummy.next
       
#         return node1.next
            
            

        
        
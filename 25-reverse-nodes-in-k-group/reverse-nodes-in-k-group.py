# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head,k):
            prev = None
            curr = head
            while k>0:
                next_curr = curr.next
                curr.next = prev
                prev = curr
                curr = next_curr
                k-=1
            return prev,curr
        count = 0
        curr = head
        while curr and count<k:
            curr = curr.next
            count +=1
        if count == k:
            reversed_head,next_head = reverse(head,k)
            head.next = self.reverseKGroup(next_head,k)
            return reversed_head
        else:
            return head
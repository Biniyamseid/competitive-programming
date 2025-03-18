# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while(curr and count!=k):
            curr = curr.next
            count +=1
        if count ==k:
            curr = self.reverseKGroup(curr,k)
            # count -=1
            while count>0:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                count -=1
            head = curr
        return head
       
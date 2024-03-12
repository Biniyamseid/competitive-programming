# Definition for singly-linked list.
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        a = dummy
        while dummy:
            end = dummy.next
            prefix_sum = 0
            while end is not None:
                prefix_sum+=end.val
                if prefix_sum ==0:
                    dummy.next= end.next
                end = end.next
            dummy = dummy.next
        return a.next
                    

        
        
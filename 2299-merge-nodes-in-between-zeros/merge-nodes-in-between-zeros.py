# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = solution  = ListNode(0)
        carry = 0
        while head:
            
            if head.val == 0:
                solution.next = ListNode(carry)
                solution = solution.next
                carry = 0
                pass
            else:
                carry += head.val




            head = head.next
        return ans.next.next
        
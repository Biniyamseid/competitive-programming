# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        cur = None
        prev = None->5->2
        prevn = 2
        curn = 13
        """
        stac = []
        while head:
            if not stac:
                stac.append(head.val)
            elif stac:
                while stac and stac[-1]<head.val:
                    stac.pop()
                stac.append(head.val)
                

            head = head.next
        dummy = ans = ListNode(None)
        for node in stac:
            ans.next = ListNode(node)
            ans = ans.next

        return dummy.next
        
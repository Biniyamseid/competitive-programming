# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution(object):
    def middleNode(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
        
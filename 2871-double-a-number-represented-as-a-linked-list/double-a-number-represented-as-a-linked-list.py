# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.set_int_max_str_digits(1000000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = ""
        cur = head
        while cur:
            num += str(cur.val)
            cur = cur.next
        num = str(int(num)*2)
        d = a = dummy = head
        for i in range(len(num)):
            c = ListNode(int(num[i]))
            d.next = c
            d = d.next
        return a.next

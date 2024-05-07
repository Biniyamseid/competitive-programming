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
        print(num)
        i = 0
        d = a = dummy = head
        print("hello")
        ans = ListNode()

        # while dummy:
        #     ans.next = ListNode(int(num[i]))
        #     ans = ans.next
        #     dummy.val = int(num[i])
        #     print(dummy)
        #     i+=1
        #     dummy = dummy.next
        # i = 0
        for i in range(len(num)):
            c = ListNode(int(num[i]))
            d.next = c
            d = d.next
        # return head


        print(d)
        print("hello")
        return a.next
        return head
        # 
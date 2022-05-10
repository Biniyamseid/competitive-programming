class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class solution(object):
    def addTwoNumbers(self,l1,l2):
        prev = result = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = Listnode(carry % 10)
            prev = prev.next
            carry //= 10
        return result.next
print(ord("a"))
print(chr(67))  


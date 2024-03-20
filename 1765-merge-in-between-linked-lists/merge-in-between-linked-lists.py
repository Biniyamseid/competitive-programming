# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        dumy = dummy = ListNode(0)
        while list1:
            if i>=a and i<=b:
                i+=1
                list1 = list1.next
                continue
            # print(i,list1)
            if i == a-1:
                dummy.next = ListNode(list1.val)
                dummy= dummy.next
                while list2:
                    dummy.next = ListNode(list2.val)
                    list2 = list2.next
                    dummy = dummy.next


                print(list1)
            elif i == b+1:
                dummy.next = ListNode(list1.val)
                dummy = dummy.next
            else:
                dummy.next = ListNode(list1.val)
                dummy = dummy.next

            
            i+=1
            list1 = list1.next
        return dumy.next
        # print(list1)
        # dummy = list1
        # ans = novice = ListNode(0)
        # flag =True
        # while list1 and list1.next:
        #     print(ans)
        #     if i==a:
        #         while list2.next:
        #             novice.next = list2
        #             list2 = list2.next
        #             novice = novice.next
        #     elif i ==b+4:
        #         print(i,b)
        #         flag = False
        #         while list1:
        #             novice.next = list1.next
        #             list1 = list1.next
        #             novice = novice.next
        #             break
        #         # print(i,b)
        #         # print(novice,list1.next.val)
        #         # novice.next = list1.next
        #     else:
        #         if flag:
        #             novice.next = ListNode(list1.val)
        #         else:
        #             print(novice)
        #             print("after")
        #             novice.next = ListNode(list1.next.val)
        #     novice = novice.next
        #     list1 = list1.next
        #     i+=1
        # return ans.next
        

        
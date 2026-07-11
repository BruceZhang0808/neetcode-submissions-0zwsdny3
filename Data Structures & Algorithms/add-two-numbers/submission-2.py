# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        n1, n2 = 0, 0
        while l1:
            num1 += l1.val * (10 ** n1)
            n1 += 1
            l1 = l1.next
        while l2:
            num2 += l2.val * (10 ** n2)
            n2 += 1
            l2 = l2.next
        res = num1 + num2
        dum = ListNode(0)
        cur = dum
        if not res:
            return dum
        while res:
            node = ListNode(res % 10)
            cur.next = node
            cur = cur.next
            res //= 10
        return dum.next
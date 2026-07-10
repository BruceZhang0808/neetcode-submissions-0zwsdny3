# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = 0
        cur = head
        while cur:
            num += 1
            cur = cur.next

        ind = num - n
        if ind == 0:
            return head.next
        cur = head
        for i in range(num):
            if i == ind - 1:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
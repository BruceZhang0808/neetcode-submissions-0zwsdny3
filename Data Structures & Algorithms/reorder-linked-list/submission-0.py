# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        pre, cur = None, slow.next
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        i, j = head, pre
        while i and j:
            nexti, nextj = i.next, j.next
            i.next = j
            j.next = nexti
            i, j = nexti, nextj
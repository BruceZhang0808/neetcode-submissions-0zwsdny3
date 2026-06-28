# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        将链表后一半反转，接着前后节点依次相连
        """

        # 快慢指针寻找中点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 切断两半链表，反转后一半链表
        pre, cur = None, slow.next
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # 前后依次相连
        i, j = head, pre
        while j:
            nexti, nextj = i.next, j.next
            i.next = j
            j.next = nexti
            i, j = nexti, nextj
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [ListNode()]
        while head:
            nodes.append(head)
            head = head.next
        nodes[-n-1].next = nodes[-n].next
        nodes.pop(-n)
        return nodes[1] if len(nodes) > 1 else None
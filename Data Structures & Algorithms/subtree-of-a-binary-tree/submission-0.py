# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            return False

        stack = [root]
        while stack:
            node = stack.pop()
            if isSame(node, subRoot):
                return True
            if node:
                stack.extend([node.left, node.right])
        return False
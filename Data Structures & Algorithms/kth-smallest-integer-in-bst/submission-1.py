# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0
        ans = None
        def inorder(node):
            nonlocal num, ans
            if not node or ans is not None:
                return
            inorder(node.left)
            num += 1
            if num == k:
                ans = node.val
            inorder(node.right)
        inorder(root)
        return ans
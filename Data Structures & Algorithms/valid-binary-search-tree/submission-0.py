# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = float('-inf')
        def valid(node):
            nonlocal pre
            if not node:
                return True
            if not valid(node.left):
                return False
            if not pre < node.val:
                return False
            pre = node.val
            return valid(node.right)
        return valid(root)
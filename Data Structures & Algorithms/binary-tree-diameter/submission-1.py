# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        if not root:
            return 0
        l_depth = depth(root.left)
        r_depth = depth(root.right)
        diameter = l_depth + r_depth
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
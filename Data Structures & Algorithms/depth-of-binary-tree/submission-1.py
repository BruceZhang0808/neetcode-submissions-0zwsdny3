# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            ans = max(ans, depth)
            stack.extend([(node.left, depth + 1), (node.right, depth + 1)])
        return ans
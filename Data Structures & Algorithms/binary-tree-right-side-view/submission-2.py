# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        ans = []
        while q:
            level_size = len(q)
            for i in range(level_size):
                cur = q.popleft()
                if cur:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    if i == level_size - 1:
                        ans.append(cur.val)
        return ans
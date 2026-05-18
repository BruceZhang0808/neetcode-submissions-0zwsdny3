class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                j = max(seen[c] + 1, j)
            seen[c] = i
            res = max(res, i - j + 1)
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                res = max(res, len(seen))
                while s[j] != c:
                    del seen[s[j]]
                    j += 1
                j += 1
            seen[c] = i
        return max(res, len(seen))
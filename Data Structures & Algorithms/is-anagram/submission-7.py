class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s, counts_t = [0] * 26, [0] * 26
        for l in s:
            counts_s[ord(l) - ord('a')] += 1
        for l in t:
            counts_t[ord(l) - ord('a')] += 1
        return counts_s == counts_t
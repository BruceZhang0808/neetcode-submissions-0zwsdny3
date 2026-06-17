class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        length = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                length[i][j] = length[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(length[i-1][j], length[i][j-1])
        return length[m][n]
    
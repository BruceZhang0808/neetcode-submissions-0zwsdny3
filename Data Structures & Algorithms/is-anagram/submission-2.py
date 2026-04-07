class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = {}
        tLetters = {}
        for l in s:
            if l in sLetters.keys():
                sLetters[l] += 1
            else:
                sLetters[l] = 1
        for l in t:
            if l in tLetters.keys():
                tLetters[l] += 1
            else:
                tLetters[l] = 1
        return sLetters == tLetters
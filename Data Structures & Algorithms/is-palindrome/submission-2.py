class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ""
        for l in s:
            if l.isalnum():
                converted += l.lower()
        return converted == converted[::-1]
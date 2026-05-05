class Solution:
    def isValid(self, s: str) -> bool:
        combo = (('(', ')'), ('[', ']'), ('{', '}'))
        stack = []
        for bracket in s:
            if stack and (stack[-1], bracket) in combo:
                stack.pop()
            else: stack.append(bracket)
        return not stack
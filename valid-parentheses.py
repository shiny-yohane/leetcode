class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parensMap = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        
        for c in s:
            if c in parensMap and len(stack) > 0 and stack[-1] == parensMap[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0

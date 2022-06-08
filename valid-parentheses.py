class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parensMap = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        
        for c in s:
            if c in parensMap: #if closing 
                if stack and stack[-1] == parensMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

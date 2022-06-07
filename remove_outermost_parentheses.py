class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        res = ""
        for c in s:
            if c == "(":
                depth += 1
                if depth > 1:
                    res += c
            elif c == ")":
                if depth > 1:
                    res += c
                depth -= 1
                
        return res

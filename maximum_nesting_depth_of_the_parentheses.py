class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
                stack.append(c)
            elif c == ')':
                max_depth = max(max_depth, depth)
                depth -= 1
                stack.pop()
        return max_depth

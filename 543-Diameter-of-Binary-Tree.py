# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_dia = 0
        
        def dfs(node):
            nonlocal max_dia
            
            if not node:
                return 0

            dia_l = dfs(node.left)
            dia_r = dfs(node.right)

            max_dia = max(max_dia, dia_l + dia_r)
            
            return 1 + max(dia_l, dia_r)
        
        dfs(root)
        
        return max_dia

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)
            
            res_l = dfs(node.left)
            res_r = dfs(node.right)
            
            h = 1 + max(res_l[1], res_r[1])
            
            if res_l[0] == False or res_r[0] == False or abs(res_l[1] - res_r[1]) > 1:
                return (False, h)
            else:
                return(True, h)
            
        return dfs(root)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (True, 0)

            bala_l, h_l = dfs(root.left)
            bala_r, h_r = dfs(root.right)
            h = 1 + max(h_l, h_r)

            if bala_l and bala_r and abs(h_l - h_r) <= 1:
                return (True, h) 
            else:
                return (False, h)
            
        return dfs(root)[0]

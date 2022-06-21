# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(r, s):
            if not r and not s:
                return True
            if r and s and r.val == s.val:
                return same_tree(r.left, s.left) and same_tree(r.right, s.right)
            return False
        
        if not root:
            return False
        
        if same_tree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, curr):
            if (i >= len(nums)):
                res.append(curr.copy())
                return
            
            n = nums[i]
            
            curr.append(n)
            dfs(i + 1, curr)
            
            curr.pop()
            dfs(i + 1, curr)
            
        dfs(0, [])
        return res    

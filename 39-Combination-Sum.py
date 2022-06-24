class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        
        def dfs(i):
            if i >= len(candidates):
                return
            
            if sum(combo) > target:
                return
            
            if sum(combo) == target:
                res.append(combo.copy())
                return
            
            combo.append(candidates[i])
            dfs(i)
            
            combo.pop()
            dfs(i + 1)
            
        dfs(0)
        return res

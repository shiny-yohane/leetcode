class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, curr):
            if i >= len(candidates): return

            n = candidates[i]
            curr_sum = n + sum(curr)
            if curr_sum > target: return


            if curr_sum == target:
                new_curr = curr.copy()
                new_curr.append(n)
                res.append(new_curr)
                return
            elif curr_sum > target:
                return
            elif curr_sum < target:
                curr.append(n)
                dfs(i, curr)
                curr.pop()
                dfs(i+1, curr)
        
        dfs(0, [])

        return res

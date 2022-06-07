class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {} # diff, index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffDict:
                return [diffDict[diff], i]
            else:
                diffDict[n] = i

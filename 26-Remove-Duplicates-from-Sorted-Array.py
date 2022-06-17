class Solution:
    def removeDuplicates(self, nums):
        l, r = 0, 1

        while r < len(nums):
            if nums[l] != nums[r]:
                nums[l+1] = nums[r]
                l += 1
            r += 1

        return l + 1

# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return
        
        p1, p2 = m - 1, n - 1
        curr_p = len(nums1) - 1
        
        while curr_p >= 0:
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[curr_p] = nums1[p1]
                    p1 -= 1
                elif nums1[p1] < nums2[p2]:
                    nums1[curr_p] = nums2[p2]
                    p2 -= 1
                elif nums1[p1] == nums2[p2]:
                    nums1[curr_p] = nums1[p1]
                    p1 -= 1
            elif p1 >= 0 and p2 < 0:
                nums1[curr_p] = nums1[p1]
                p1 -= 1
            elif p1 < 0 and p2 >= 0:
                nums1[curr_p] = nums2[p2]
                p2 -= 1

            curr_p -= 1

        return nums1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def water(n1, n2):
            h1 = height[n1]
            h2 = height[n2]
            w  = n2 - n1
            return w * min(h1, h2)
            
        
        max_area = 0
        
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         max_area = max(max_area, water(i, j))
        
        l, r = 0, len(height) - 1
        
        while l < r:
            h1 = height[l]
            h2 = height[r]
            
            area = water(l, r)
            max_area = max(max_area, area)

            if h1 <= h2:
                l += 1
            else:
                r -= 1
                            
        return max_area

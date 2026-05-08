class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights) * 1
        else:
            max_cap = 0
            left , right = 0 , len(heights) - 1
            while (left < right):
                max_cap = max(max_cap , (min(heights[left],heights[right]) * (right - left)))
                if heights[left] < heights[right]:
                    left += 1
                else: 
                    right -= 1        
            return max_cap
                
        
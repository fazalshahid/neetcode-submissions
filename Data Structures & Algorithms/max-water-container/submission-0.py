class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxArea = - math.inf

        while left < right:
            h = min(heights[left], heights[right])


            area = h * (right - left)

            maxArea = max(maxArea, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea